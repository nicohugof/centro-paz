"""
CPAZ Media OS — Plataforma Desacoplada de Marketing, Contenido y Atribución sin PII.

Cumple la Regla Permanente de Integración Inteligente:
INVESTIGAR ANTES DE CONSTRUIR. INTEGRAR ANTES DE DUPLICAR. MEDIR ANTES DE AFIRMAR. OPTIMIZAR ANTES DE ESCALAR.
"""

from media_os.privacy import PrivacyViolationError, assert_no_pii, assert_path_not_clinical, sanitize_for_llm

__all__ = [
    "PrivacyViolationError",
    "assert_no_pii",
    "assert_path_not_clinical",
    "sanitize_for_llm",
]
