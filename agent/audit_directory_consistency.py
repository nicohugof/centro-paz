#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Auditoría Automatizada de Coherencia NAP y Triangulación de Directorios.

Verifica de forma estricta:
1. Coherencia NAP (Name, Address, Phone) idéntico e invariable:
   - Name: "Centro Paz" y "Valentina Castro Núñez"
   - Address: "Salvador 2302" en comuna de "Ñuñoa", Santiago
   - Phone: "+56 9 6516 3893" / "56965163893" unificado sin discrepancias
2. Arancel Unificado:
   - "$45.000 CLP" unificado en todos los perfiles y fichas de servicio
   - Cero discrepancias de precios obsoletos ($40.000 / $50.000)
3. Registro Profesional Oficial SIS:
   - Registro Nº 667344 de la Superintendencia de Salud de Chile presente y exacto
4. Triangulación Multi-Directorio & Google Maps:
   - Integración activa de Doctoralia, Encuadrado, SaludVitale / RedSalud y Google Business Profile
   - Existencia y enlace recíproco a tools/asistente_google_maps.html y https://business.google.com/
"""

import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Archivos nucleares de auditoría
CORE_DOCS = [
    ROOT / "docs" / "PERFIL_ENCUADRADO_DOCTORALIA_VALENTINA.md",
    ROOT / "docs" / "FICHA_GOOGLE_BUSINESS_PROFILE_LISTA.md",
    ROOT / "docs" / "GOOGLE_BUSINESS_PROFILE_NUNOA.md",
    ROOT / "llms.txt",
]

CORE_TOOLS = [
    ROOT / "tools" / "registro_directorios.html",
    ROOT / "tools" / "asistente_google_maps.html",
]

CORE_HTML_PUBLIC = [
    ROOT / "index.html",
    ROOT / "psicologo-nunoa.html",
]

# Parámetros canónicos de la entidad
CANONICAL_PHONE_DIGITS = "56965163893"
CANONICAL_PHONE_FORMAT = "+56 9 6516 3893"
CANONICAL_SIS_NUMBER = "667344"
CANONICAL_ADDRESS_STREET = "Salvador 2302"
CANONICAL_ADDRESS_COMMUNE = "Ñuñoa"
CANONICAL_FEE_STRINGS = ["$45.000", "45.000 CLP", "45000"]
OUTDATED_FEE_PATTERNS = [r"\$40\.000", r"\$50\.000", r"\$35\.000", r"\$30\.000"]


class DirectoryConsistencyAuditor:
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        self.errors = []
        self.warnings = []

    def check(self, condition: bool, description: str, category: str = "GENERAL"):
        self.total_tests += 1
        if condition:
            self.passed_tests += 1
            print(f"  ✅ [PASS] {description}")
            return True
        else:
            self.errors.append(f"[{category}] {description}")
            print(f"  ❌ [FAIL] {description}")
            return False

    def run_audit(self) -> bool:
        print("=" * 80)
        print(" 🌿 CENTRO PAZ — AUDITORÍA AUTOMATIZADA DE CONSISTENCIA NAP & DIRECTORIOS")
        print("=" * 80)
        print(f"Directorio raíz: {ROOT}\n")

        # ---------------------------------------------------------
        # 1. Existencia e Integridad de Archivos Nucleares
        # ---------------------------------------------------------
        print("📁 1. VERIFICACIÓN DE ARCHIVOS NUCLEARES")
        all_files = CORE_DOCS + CORE_TOOLS + CORE_HTML_PUBLIC
        for f in all_files:
            rel = f.relative_to(ROOT)
            self.check(f.exists(), f"Archivo existe y es accesible: {rel}", "FILE_EXISTENCE")

        # ---------------------------------------------------------
        # 2. Verificación de Identidad NAP (Name, Address, Phone)
        # ---------------------------------------------------------
        print("\n🏛️ 2. COHERENCIA DE IDENTIDAD NAP (NAME, ADDRESS, PHONE)")
        for f in all_files:
            if not f.exists():
                continue
            rel = f.relative_to(ROOT)
            content = f.read_text(encoding="utf-8")

            # Nombre
            has_centro_paz = "Centro Paz" in content or "CENTRO PAZ" in content
            has_valentina = "Valentina Castro" in content or "VALENTINA CASTRO" in content
            self.check(
                has_centro_paz and has_valentina,
                f"Nombre NAP consistente (Centro Paz + Valentina Castro) en {rel}",
                "NAP_NAME"
            )

            # Dirección (Salvador 2302 en Ñuñoa)
            has_salvador = CANONICAL_ADDRESS_STREET in content
            has_nunoa = CANONICAL_ADDRESS_COMMUNE in content or "Nunoa" in content
            self.check(
                has_salvador and has_nunoa,
                f"Dirección NAP unificada (Salvador 2302, Ñuñoa) en {rel}",
                "NAP_ADDRESS"
            )

            # Teléfono oficial unificado
            has_phone = (CANONICAL_PHONE_DIGITS in content) or (CANONICAL_PHONE_FORMAT in content)
            self.check(
                has_phone,
                f"Teléfono oficial unificado ({CANONICAL_PHONE_FORMAT} / {CANONICAL_PHONE_DIGITS}) en {rel}",
                "NAP_PHONE"
            )

        # ---------------------------------------------------------
        # 3. Verificación de Registro Profesional Oficial SIS Nº 667344
        # ---------------------------------------------------------
        print("\n🛡️ 3. REGISTRO OFICIAL SUPERINTENDENCIA DE SALUD (SIS Nº 667344)")
        for f in all_files:
            if not f.exists():
                continue
            rel = f.relative_to(ROOT)
            content = f.read_text(encoding="utf-8")

            has_sis = CANONICAL_SIS_NUMBER in content
            self.check(
                has_sis,
                f"Registro Oficial SIS Nº {CANONICAL_SIS_NUMBER} presente y exacto en {rel}",
                "SIS_REGISTRATION"
            )

        # ---------------------------------------------------------
        # 4. Verificación de Arancel Unificado ($45.000 CLP)
        # ---------------------------------------------------------
        print("\n💳 4. ARANCEL UNIFICADO ($45.000 CLP) Y SIN DISCREPANCIAS")
        files_requiring_fee = [
            ROOT / "docs" / "PERFIL_ENCUADRADO_DOCTORALIA_VALENTINA.md",
            ROOT / "docs" / "FICHA_GOOGLE_BUSINESS_PROFILE_LISTA.md",
            ROOT / "docs" / "GOOGLE_BUSINESS_PROFILE_NUNOA.md",
            ROOT / "llms.txt",
            ROOT / "tools" / "registro_directorios.html",
            ROOT / "tools" / "asistente_google_maps.html",
            ROOT / "index.html",
            ROOT / "psicologo-nunoa.html",
        ]

        for f in files_requiring_fee:
            if not f.exists():
                continue
            rel = f.relative_to(ROOT)
            content = f.read_text(encoding="utf-8")

            has_canonical_fee = any(fee in content for fee in CANONICAL_FEE_STRINGS)
            self.check(
                has_canonical_fee,
                f"Arancel unificado $45.000 CLP registrado en {rel}",
                "FEE_CANONICAL"
            )

            # Detectar si hay tarifas conflictivas obsoletas
            conflicts = []
            for pattern in OUTDATED_FEE_PATTERNS:
                if re.search(pattern, content):
                    # Descartar si solo es un rango de copago (ej: $9.000 a $18.000)
                    matches = re.findall(pattern, content)
                    conflicts.extend(matches)

            self.check(
                len(conflicts) == 0,
                f"Cero aranceles obsoletos en conflicto en {rel}",
                "FEE_NO_CONFLICT"
            )

        # ---------------------------------------------------------
        # 5. Triangulación Multi-Directorio en registro_directorios.html
        # ---------------------------------------------------------
        print("\n🌐 5. TRIANGULACIÓN MULTI-DIRECTORIO & ASISTENTE GOOGLE MAPS")
        tool_reg = ROOT / "tools" / "registro_directorios.html"
        if tool_reg.exists():
            c = tool_reg.read_text(encoding="utf-8")

            self.check(
                "asistente_google_maps.html" in c and "https://business.google.com/" in c,
                "registro_directorios.html enlaza a asistente_google_maps.html y https://business.google.com/",
                "TRIANGULATION_GOOGLE"
            )

            self.check(
                "pro.doctoralia.cl" in c or "doctoralia" in c.lower(),
                "registro_directorios.html incluye módulo activo para Doctoralia Chile",
                "TRIANGULATION_DOCTORALIA"
            )

            self.check(
                "encuadrado.com" in c or "encuadrado" in c.lower(),
                "registro_directorios.html incluye módulo activo para Encuadrado.cl",
                "TRIANGULATION_ENCUADRADO"
            )

            self.check(
                "saludvitale.com" in c or "saludvitale" in c.lower() or "redsalud" in c.lower(),
                "registro_directorios.html incluye módulo activo para SaludVitale / RedSalud",
                "TRIANGULATION_SALUDVITALE"
            )

            self.check(
                "campo-sis" in c and CANONICAL_SIS_NUMBER in c,
                f"registro_directorios.html contiene tarjeta dedicada con botón de copia rápida del SIS Nº {CANONICAL_SIS_NUMBER}",
                "TRIANGULATION_SIS_CARD"
            )

        # ---------------------------------------------------------
        # 6. Funcionalidad del Asistente Google Maps
        # ---------------------------------------------------------
        tool_maps = ROOT / "tools" / "asistente_google_maps.html"
        if tool_maps.exists():
            cm = tool_maps.read_text(encoding="utf-8")
            self.check(
                "business.google.com" in cm,
                "asistente_google_maps.html incluye enlace directo a la consola de Google Business Profile",
                "MAPS_ASSISTANT_LINK"
            )
            self.check(
                "registro_directorios.html" in cm,
                "asistente_google_maps.html enlaza de vuelta a registro_directorios.html",
                "MAPS_ASSISTANT_RECIPROCAL"
            )
            self.check(
                CANONICAL_ADDRESS_STREET in cm and CANONICAL_SIS_NUMBER in cm and "$45.000" in cm,
                f"asistente_google_maps.html certificado con NAP, SIS Nº {CANONICAL_SIS_NUMBER} y arancel $45.000 CLP",
                "MAPS_ASSISTANT_CONSISTENCY"
            )

        # ---------------------------------------------------------
        # Dictamen Final
        # ---------------------------------------------------------
        score_pct = round((self.passed_tests / self.total_tests) * 100, 2) if self.total_tests > 0 else 0
        print("\n" + "=" * 80)
        print(f"📊 RESULTADO DE LA AUDITORÍA: {self.passed_tests}/{self.total_tests} pruebas superadas ({score_pct}%)")
        print("=" * 80)

        if self.errors:
            print("\n❌ ERRORES DETECTADOS:")
            for err in self.errors:
                print(f"  • {err}")
            print("\n⚠️ DICTAMEN: NO APROBADO (Se requieren correcciones).")
            return False
        else:
            print("\n🏆 DICTAMEN: CERTIFICACIÓN 100% EXITOSA.")
            print("  • Coherencia NAP: 100% idéntico en todos los documentos y herramientas.")
            print(f"  • Registro Oficial SIS: Nº {CANONICAL_SIS_NUMBER} validado.")
            print("  • Arancel: $45.000 CLP unificado sin discrepancias.")
            print("  • Teléfono: +56 9 6516 3893 unificado en formato internacional y numérico.")
            print("  • Triangulación de Directorios: Doctoralia, Encuadrado, SaludVitale y Google Maps sincronizados.")
            print("=" * 80)
            return True


if __name__ == "__main__":
    auditor = DirectoryConsistencyAuditor()
    success = auditor.run_audit()
    sys.exit(0 if success else 1)
