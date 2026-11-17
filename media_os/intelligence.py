"""
Inteligencia Estratégica, Investigación Clínica y QA Editorial — CPAZ Media OS.

¿Qué es?
Capa diferenciadora que reutiliza la base de conocimiento clínica existente de Centro Paz
(`blog_clinical_knowledge.py` + `content_engine.py`), conecta opcionalmente con `Ollama` local
(licencia MIT) sin exposición PII y aplica control de calidad clínico y de identidad.

¿Para qué lo usamos?
Generar briefs estratégicos, ángulos de campaña y variaciones de copy validadas frente al
Registro SIS Nº 667344, arancel oficial ($45.000 CLP), teléfono oficial (+56 9 6516 3893) y
ética clínica (cero diagnósticos automáticos ni promesas de cura) antes de pasar al calendario.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol

from agent import blog_clinical_knowledge, content_engine
from media_os.privacy import assert_no_pii, sanitize_for_llm
from media_os.storage import get_connection, utc_now_iso

CANONICAL_SIS = "667344"
CANONICAL_PHONE = "+56 9 6516 3893"
CANONICAL_FEE_CLP = 45000
FORBIDDEN_CLINICAL_CLAIMS = (
    "cura definitiva",
    "cura garantizada",
    "100% curado",
    "diagnostico definitivo en reel",
    "diagnóstico definitivo en un video",
    "receta medica",
    "receta médica",
    "sin terapia profesional",
)
OUTDATED_FEE_REGEX = re.compile(r"\$(?:30|35|40|50)\.000")


class TextGeneratorAdapter(Protocol):
    """Interfaz desacoplada para enriquecimiento local de texto sin acoplar el motor."""

    engine_name: str

    def generate(self, prompt: str, *, fallback_text: str) -> str:
        ...


@dataclass
class OllamaAdapter:
    """Adaptador HTTP hacia Ollama local (127.0.0.1:11434, licencia MIT) con fallback seguro."""

    base_url: str = field(default_factory=lambda: os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434"))
    model: str = field(default_factory=lambda: os.getenv("CPAZ_OLLAMA_MODEL", "qwen2.5-coder:1.5b"))
    timeout_sec: float = 8.0
    engine_name: str = "ollama-local"

    def is_available(self) -> bool:
        try:
            req = urllib.request.Request(f"{self.base_url.rstrip('/')}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=1.5) as resp:
                return resp.status == 200
        except Exception:
            return False

    def generate(self, prompt: str, *, fallback_text: str) -> str:
        safe_prompt = sanitize_for_llm(prompt)
        try:
            payload = json.dumps(
                {
                    "model": self.model,
                    "prompt": safe_prompt,
                    "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 180},
                }
            ).encode("utf-8")
            req = urllib.request.Request(
                f"{self.base_url.rstrip('/')}/api/generate",
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=self.timeout_sec) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            text = (data.get("response") or "").strip()
            if not text:
                return fallback_text
            assert_no_pii(text, field_path="ollama_output")
            return text
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
            return fallback_text


@dataclass
class DeterministicKBAdapter:
    """Motor determinista sin red ni costo externo apoyado en la biblioteca clínica CPAZ."""

    engine_name: str = "cpaz-kb-deterministic"

    def generate(self, prompt: str, *, fallback_text: str) -> str:
        sanitize_for_llm(prompt)
        return fallback_text


@dataclass
class QAResult:
    passed: bool
    issues: List[str]
    warnings: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {"passed": self.passed, "issues": self.issues, "warnings": self.warnings}


def run_clinical_qa(
    *,
    title: str,
    caption: str,
    require_cta: bool = True,
) -> QAResult:
    """
    Control de calidad ético, clínico y de coherencia NAP específico de Centro Paz.
    """
    assert_no_pii({"title": title, "caption": caption}, field_path="clinical_qa")
    issues: List[str] = []
    warnings: List[str] = []

    full = f"{title}\n{caption}".strip()
    low = full.lower()

    if len(caption.strip()) < 40:
        issues.append("Copy demasiado corto (mínimo 40 caracteres).")

    for bad_claim in FORBIDDEN_CLINICAL_CLAIMS:
        if bad_claim in low:
            issues.append(f"Afirmación clínica prohibida detectada: '{bad_claim}'.")

    if OUTDATED_FEE_REGEX.search(full):
        issues.append("Arancel obsoleto detectado (solo se admite arancel oficial $45.000 CLP).")

    if " .000" in full:
        issues.append("Formato roto de monto (' .000') detectado en el copy.")

    has_cta = (
        CANONICAL_PHONE in full
        or "56965163893" in full
        or "centropaz.cl" in low
        or "whatsapp" in low
    )
    if require_cta and not has_cta:
        issues.append(f"Falta CTA verificable hacia web oficial o WhatsApp ({CANONICAL_PHONE}).")

    if "salvador 2302" not in low and "ñuñoa" not in low and "online" not in low:
        warnings.append("Sugerencia: precisar modalidad Online Chile y/o Presencial en Ñuñoa.")

    if CANONICAL_SIS not in full:
        warnings.append(f"Nota editorial: mencionar Registro SIS Nº {CANONICAL_SIS} cuando corresponda.")

    return QAResult(passed=(len(issues) == 0), issues=issues, warnings=warnings)


class StrategicIntelligenceEngine:
    """
    Reutiliza la base clínica CPAZ y adapta propuestas editoriales con Ollama (o fallback determinista).
    """

    def __init__(
        self,
        *,
        db_path: Optional[Path | str] = None,
        generator: Optional[TextGeneratorAdapter] = None,
    ) -> None:
        self.db_path = db_path
        self.generator: TextGeneratorAdapter = generator or OllamaAdapter()

    def audit_existing_knowledge(self) -> Dict[str, Any]:
        topics = content_engine.TOPICS
        articles = blog_clinical_knowledge.CLINICAL_ARTICLES
        reels = content_engine.REELS_SCRIPTS
        threads = content_engine.THREADS_POSTS
        community = content_engine.FACEBOOK_COMMUNITY_POSTS

        missing_articles = [k for k in topics if k not in articles]
        qa_flags = {}
        for k, t in topics.items():
            qa = run_clinical_qa(title=t["title"], caption=t["caption"], require_cta=True)
            if not qa.passed:
                qa_flags[k] = qa.issues

        return {
            "topics_count": len(topics),
            "clinical_articles_count": len(articles),
            "reels_scripts_count": len(reels),
            "threads_count": len(threads),
            "community_posts_count": len(community),
            "topics_missing_article": missing_articles,
            "topics_qa_issues": qa_flags,
            "brand_fee_clp": CANONICAL_FEE_CLP,
            "brand_sis": CANONICAL_SIS,
            "brand_phone": CANONICAL_PHONE,
        }

    def generate_strategic_brief(
        self,
        topic_key: str,
        *,
        audience: str = "Adultos en Chile que buscan psicoterapia y reembolso Isapre",
        objective: str = "Educación clínica y conversión ética a consulta por WhatsApp",
        use_llm: bool = False,
    ) -> Dict[str, Any]:
        if topic_key not in content_engine.TOPICS:
            raise KeyError(f"Tópico desconocido '{topic_key}'. Disponibles: {len(content_engine.TOPICS)}")

        assert_no_pii({"audience": audience, "objective": objective}, field_path="brief_input")

        topic = content_engine.TOPICS[topic_key]
        article = blog_clinical_knowledge.CLINICAL_ARTICLES.get(topic_key, {})

        deterministic_summary = (
            f"Ángulo central: {topic['title']}. {topic['hook']} "
            f"Puntos clave: {'; '.join(topic['points'][:3])}. "
            f"Cierre ético: Modalidad Online todo Chile / Presencial Ñuñoa, boleta reembolsable Isapre ($45.000 CLP), "
            f"Registro SIS Nº {CANONICAL_SIS}, WhatsApp {CANONICAL_PHONE}."
        )

        used_engine = "cpaz-kb-deterministic"
        summary = deterministic_summary
        if use_llm:
            prompt = (
                "Resume en máximo 2 oraciones cálidas, neuroafirmativas y éticas en español de Chile "
                "(sin prometer curas ni diagnósticos definitivos y sin datos de pacientes) este tema clínico:\n"
                f"Título: {topic['title']}\nGancho: {topic['hook']}\nPuntos: {', '.join(topic['points'][:3])}"
            )
            generated = self.generator.generate(prompt, fallback_text=deterministic_summary)
            summary = generated
            if generated != deterministic_summary:
                used_engine = getattr(self.generator, "engine_name", "custom-llm")

        qa = run_clinical_qa(title=topic["title"], caption=topic["caption"], require_cta=True)
        brief = {
            "brief_id": f"brf-{uuid.uuid4().hex[:10]}",
            "topic_key": topic_key,
            "category": topic["category"],
            "title": topic["title"],
            "hook": topic["hook"],
            "audience": audience,
            "objective": objective,
            "strategic_summary": summary,
            "key_points": list(topic["points"]),
            "clinical_foundation_present": bool(article),
            "clinical_faqs_count": len(article.get("faqs", [])),
            "recommended_cta": f"Agenda con Valentina Castro Núñez (SIS Nº {CANONICAL_SIS}) por WhatsApp {CANONICAL_PHONE} o www.centropaz.cl",
            "suggested_hashtags": list(topic["hashtags"]),
            "source_engine": used_engine,
            "qa": qa.to_dict(),
            "created_at": utc_now_iso(),
        }

        with get_connection(self.db_path, write=True) as conn:
            conn.execute(
                """
                INSERT INTO research_briefs (
                    brief_id, topic_key, audience, objective, source_engine,
                    brief_json, qa_passed, qa_notes_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    brief["brief_id"],
                    topic_key,
                    audience,
                    objective,
                    used_engine,
                    json.dumps(brief, ensure_ascii=False),
                    1 if qa.passed else 0,
                    json.dumps(qa.to_dict(), ensure_ascii=False),
                    brief["created_at"],
                ),
            )
        return brief

    def list_briefs(self, *, limit: int = 20) -> List[Dict[str, Any]]:
        with get_connection(self.db_path) as conn:
            rows = conn.execute(
                "SELECT brief_json FROM research_briefs ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [json.loads(r["brief_json"]) for r in rows]
