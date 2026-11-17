"""
Firewall de Privacidad Clínica y Aislamiento (Ley N° 19.628) — CPAZ Media OS.

¿Qué es?
Barrera determinista de validación de datos y rutas que garantiza que ninguna pieza de
marketing, inteligencia LLM local, automatización n8n o analítica de atribución acceda
a fichas de pacientes, números personales ni registros sensibles.

¿Para qué lo usamos?
Cumplir estrictamente con la separación entre marketing, atribución comercial anónima
y fichas clínicas (`data/patient_intakes.json`), bloqueando fugas antes de que ocurran.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

# Canales públicos oficiales permitidos de Centro Paz (no constituyen PII de pacientes)
PUBLIC_OFFICIAL_PHONE_DIGITS = frozenset({"56965163893"})
PUBLIC_OFFICIAL_EMAILS = frozenset({"contacto.centropaz@gmail.com"})

# Archivos/carpetas clínicos estrictamente prohibidos para CPAZ Media OS
FORBIDDEN_CLINICAL_FILENAMES = frozenset(
    {
        "patient_intakes.json",
        "fichas_clinicas.json",
        "pacientes.db",
        "clinical_records.db",
    }
)

FORBIDDEN_CLINICAL_KEYS = frozenset(
    {
        "rut",
        "paciente_rut",
        "patient_name",
        "nombre_paciente",
        "diagnostico_paciente",
        "historia_clinica",
        "clinical_notes",
        "notas_clinicas",
        "telefono_paciente",
        "patient_phone",
        "email_paciente",
        "patient_email",
        "ficha_clinica",
        "patient_id",
        "isapre_afiliado",
    }
)

_RUT_PATTERN = re.compile(r"\b\d{1,2}(?:\.\d{3}){2}-[\dkK]\b|\b\d{7,8}-[\dkK]\b")
_PHONE_CL_PATTERN = re.compile(r"(?<!\d)(?:\+?56\s?9\s?\d{4}\s?\d{4}|9\s?\d{8})(?!\d)")
_EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


class PrivacyViolationError(ValueError):
    """Excepción lanzada cuando se detecta información sensible de pacientes o ruta clínica."""


def assert_path_not_clinical(path: Path | str) -> None:
    """Impide leer, escribir o referenciar archivos de fichas clínicas desde `media_os`."""
    raw = str(path)
    name = Path(raw).name.lower()
    norm = raw.replace("\\", "/").lower()
    if name in FORBIDDEN_CLINICAL_FILENAMES or "patient_intakes" in norm or "fichas_clinicas" in norm:
        raise PrivacyViolationError(
            f"Acceso bloqueado por aislamiento clínico (Ley 19.628): ruta prohibida '{path}'."
        )


def _scan_text_for_pii(text: str, field_path: str) -> None:
    if not text:
        return
    if _RUT_PATTERN.search(text):
        raise PrivacyViolationError(
            f"PII detectado en '{field_path}': formato tipo RUT chileno no permitido en Media OS."
        )
    for match in _PHONE_CL_PATTERN.finditer(text):
        digits = re.sub(r"\D", "", match.group(0))
        if len(digits) == 9 and digits.startswith("9"):
            digits = "56" + digits
        if digits not in PUBLIC_OFFICIAL_PHONE_DIGITS:
            raise PrivacyViolationError(
                f"PII detectado en '{field_path}': teléfono personal ajeno al canal oficial CPAZ."
            )
    for match in _EMAIL_PATTERN.finditer(text):
        email = match.group(0).lower()
        if email not in PUBLIC_OFFICIAL_EMAILS:
            raise PrivacyViolationError(
                f"PII detectado en '{field_path}': correo personal no permitido en Media OS."
            )


def assert_no_pii(payload: Any, *, field_path: str = "payload") -> None:
    """Valida recursivamente strings, dicts y listas rechazando PII o llaves clínicas."""
    if payload is None or isinstance(payload, (int, float, bool)):
        return
    if isinstance(payload, (os.PathLike, Path)):
        assert_path_not_clinical(payload)
        return
    if isinstance(payload, str):
        if "patient_intakes" in payload.lower():
            assert_path_not_clinical(payload)
        _scan_text_for_pii(payload, field_path)
        return
    if isinstance(payload, dict):
        for k, v in payload.items():
            k_str = str(k).strip().lower()
            if k_str in FORBIDDEN_CLINICAL_KEYS:
                raise PrivacyViolationError(
                    f"Campo clínico restringido '{k}' rechazado en '{field_path}' (aislamiento estricto)."
                )
            assert_no_pii(v, field_path=f"{field_path}.{k}")
        return
    if isinstance(payload, (list, tuple, set)):
        for idx, item in enumerate(payload):
            assert_no_pii(item, field_path=f"{field_path}[{idx}]")
        return


def sanitize_for_llm(text: str) -> str:
    """
    Asegura que cualquier prompt enviado a Ollama local cumpla aislamiento clínico.
    Si contiene PII explícito falla cerrado con PrivacyViolationError.
    """
    assert_no_pii(text, field_path="llm_prompt")
    return text.strip()
