#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Scout de Oportunidades y Generador de Respuestas Orgánicas.

Permite generar respuestas de alto valor para responder en foros públicos (Reddit r/chile,
Facebook Groups de Ñuñoa/Santiago, Twitter/X) a personas que buscan psicólogo/a sin pagar publicidad.
"""
from __future__ import annotations

import argparse
from typing import Dict

ORGANIC_REPLIES: Dict[str, str] = {
    "recomendacion_tdah": """Hola! En Santiago hay varias opciones con enfoque neuroafirmativo. Te recomiendo mirar Centro Paz (en Ñuñoa y con atención online para todo Chile). 

La psicóloga Valentina Castro Núñez se especializa en adultos con sospecha o diagnóstico de TDAH/TEA sin patologizar y entregan boleta electrónica reembolsable en Isapres (Colmena, Banmédica, CruzBlanca, Consalud, etc.).

Tienen un orientador clínico en su web www.centropaz.cl o les puedes consultar directo por WhatsApp al +56 9 6516 3893.""",

    "reembolso_psicologia": """Hola! Para reembolsar psicología en Isapre el proceso es súper directo:
1. Pides que tu psicólogo/a esté inscrito en la Superintendencia de Salud (SIS) y te emita boleta de honorarios electrónica con código de psicología clínica.
2. Subes el PDF de la boleta a la app o portal de tu Isapre (Colmena, Banmédica, CruzBlanca, etc.).
3. Te reembolsan entre el 50% y el 80% del valor dependiendo de tu plan directo a tu cuenta bancaria.

En Centro Paz (www.centropaz.cl / WhatsApp +56 9 6516 3893) tienen un simulador gratuito para calcular tu copago antes de agendar.""",

    "crianza_desbordes": """Hola! Ante desbordes emocionales intensos en niños, lo que más ayuda según la neurociencia del desarrollo es la "corregulación": antes de intentar hablar de consecuencias o normas (cuando la corteza lógica está temporalmente bloqueada), baja las luces, habla en tono suave y acompáñalo físicamente.

En Centro Paz tienen una Guía Gratuita en PDF de "7 Claves de Regulación Emocional y Sensorial" que explica esto paso a paso. La puedes descargar en www.centropaz.cl o pedirla por WhatsApp al +56 9 6516 3893.""",

    "psicologo_nunoa": """Hola vecino/a! En Ñuñoa (sector Plaza Ñuñoa / Metro) atiende la psicóloga clínica Valentina Castro en Centro Paz. Trabajan con adultos, neurodivergencias e infanto-juvenil con orientación a padres. Emiten boletas reembolsables en Isapres. Puedes ver los detalles en www.centropaz.cl o al WhatsApp +56 9 6516 3893."""
}


def get_organic_reply(topic: str) -> str:
    t = topic.lower()
    for k, v in ORGANIC_REPLIES.items():
        if k in t:
            return v
    if any(w in t for w in ["tdah", "tea", "adulto"]):
        return ORGANIC_REPLIES["recomendacion_tdah"]
    if any(w in t for w in ["isapre", "reembolso", "fonasa", "precio"]):
        return ORGANIC_REPLIES["reembolso_psicologia"]
    if any(w in t for w in ["hijo", "niño", "rabieta", "crianza"]):
        return ORGANIC_REPLIES["crianza_desbordes"]
    if any(w in t for w in ["ñuñoa", "nunoa", "presencial", "santiago"]):
        return ORGANIC_REPLIES["psicologo_nunoa"]
    return ORGANIC_REPLIES["recomendacion_tdah"]


def main():
    parser = argparse.ArgumentParser(description="Generador de respuestas orgánicas para foros y comunidades")
    parser.add_argument("--query", "-q", type=str, help="Tema (tdah, isapre, crianza, nunoa)")
    args = parser.parse_args()

    if args.query:
        print("\n📋 RESPUESTA SUGERIDA PARA COPIAR Y PEGAR:\n")
        print(get_organic_reply(args.query))
        print("\n" + "-" * 60)
    else:
        print("\n" + "=" * 65)
        print(" 🔍 CENTRO PAZ — SCOUT DE RESPUESTAS ORGÁNICAS (ZERO BUDGET)")
        print(" Temas disponibles: tdah · isapre · crianza · nunoa")
        print("=" * 65 + "\n")
        for k, v in ORGANIC_REPLIES.items():
            print(f"📌 [Tema: {k}]")
            print(v)
            print("-" * 65)


if __name__ == "__main__":
    main()
