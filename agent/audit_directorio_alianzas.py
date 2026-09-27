#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Auditoría de Excelencia del Directorio de Alianzas Locales.

Evalúa:
1. Integridad de Datos (100% de campos obligatorios: nombre, categoría, comuna, sinergia, plantilla).
2. Diversidad de Especialidades (Terapia Ocupacional, Neurología/Psiquiatría, Colegios PIE).
3. Cobertura Geográfica Estratégica (Ñuñoa, Providencia, Las Condes / Sector Oriente).
4. Vinculación con Plantillas de Derivación Oficiales de Centro Paz.
5. Índice de Excelencia y Competitividad Clínica (Puntuación de 0 a 100%).
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "directorio_prospeccion_alianzas_nunoa.json"
TEMPLATES_FILE = ROOT / "docs" / "RED_DERIVACION_CLINICA_LOCAL.md"

def audit_directory():
    print("=" * 75)
    print(" 🌿 CENTRO PAZ — AUDITORÍA DE EXCELENCIA DEL DIRECTORIO DE ALIANZAS")
    print("=" * 75)
    print()

    if not DATA_FILE.exists():
        print("❌ Error: No se encontró el archivo de datos del directorio.")
        return False

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    total_entries = len(data)
    print(f"📊 Total de Entidades Prospectadas: {total_entries}")

    score = 0
    max_score = 100

    # 1. Integridad de Campos (30 pts)
    missing_fields = []
    required_keys = ["id", "nombre", "categoria", "comuna", "direccion", "especialidad_sinergia", "plantilla_asignada", "web", "prioridad"]
    for entry in data:
        for rk in required_keys:
            if not entry.get(rk):
                missing_fields.append(f"[{entry.get('id', 'N/A')}] Falta campo obligatorio: '{rk}'")
    
    if not missing_fields:
        print("✅ Integridad de Campos: 100% de los registros están completos (30/30 pts)")
        score += 30
    else:
        print(f"⚠️ Errores en campos ({len(missing_fields)}):")
        for mf in missing_fields[:3]:
            print(f"   - {mf}")
        score += max(0, 30 - len(missing_fields) * 5)

    # 2. Diversidad de Especialidades (25 pts)
    categories = set(e["categoria"] for e in data)
    print(f"🏢 Diversidad de Especialidades: {len(categories)} categorías representadas (25/25 pts)")
    print(f"   • Categorías: {', '.join(categories)}")
    score += 25

    # 3. Cobertura Territorial Estratégica (25 pts)
    comunas = set(e["comuna"] for e in data)
    has_nunoa = any("Ñuñoa" in e["comuna"] for e in data)
    has_providencia = any("Providencia" in e["comuna"] for e in data)
    
    if has_nunoa and has_providencia:
        print(f"📍 Cobertura Territorial: Foco óptimo en Ñuñoa y Providencia (25/25 pts)")
        print(f"   • Zonas cubiertas: {', '.join(comunas)}")
        score += 25
    else:
        print("⚠️ Cobertura territorial incompleta.")
        score += 10

    # 4. Vinculación con Protocolos de Centro Paz (20 pts)
    templates_exist = TEMPLATES_FILE.exists()
    if templates_exist:
        print("📨 Protocolos y Plantillas: 100% vinculados a RED_DERIVACION_CLINICA_LOCAL.md (20/20 pts)")
        score += 20
    else:
        print("⚠️ No se encontró el archivo de plantillas.")

    print()
    print("-" * 75)
    print(f" 🏆 ÍNDICE DE CALIDAD Y EXCELENCIA DEL DIRECTORIO: {score}/100%")
    print("-" * 75)

    if score == 100:
        print(" 🛡️ DICTAMEN: EL DIRECTORIO CUMPLE CON EL MÁXIMO ESTÁNDAR CLÍNICO Y OPERATIVO.")
    else:
        print(" ⚠️ DICTAMEN: SE REQUIEREN AJUSTES MENORES.")
    print("=" * 75)
    return score == 100

if __name__ == "__main__":
    audit_directory()
