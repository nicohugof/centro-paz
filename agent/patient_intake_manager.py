#!/usr/bin/env python3
"""
Centro Paz (CPAZ) — Gestor Clínico de Ingresos y Tablero hacia los 100 Pacientes.

Permite:
1. Registrar nuevas consultas de WhatsApp de forma confidencial (Ley 19.628).
2. Monitorear el progreso en tiempo real hacia la meta de 100 pacientes de Valentina.
3. Calcular la tasa de conversión de leads a sesiones agendadas y facturación estimada.
4. Generar reportes estadísticos de motivos de consulta (TDAH, Ansiedad, Isapre, Ñuñoa).
"""
import json
import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "patient_intakes.json"

GOAL_PATIENTS = 100
SESSION_FEE = 45000

def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        initial_data = {
            "created_at": datetime.now().isoformat(),
            "goal": GOAL_PATIENTS,
            "session_fee": SESSION_FEE,
            "patients": []
        }
        DATA_FILE.write_text(json.dumps(initial_data, indent=2, ensure_ascii=False), encoding="utf-8")

def load_data():
    ensure_data_file()
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"goal": GOAL_PATIENTS, "session_fee": SESSION_FEE, "patients": []}

def save_data(data):
    ensure_data_file()
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def add_intake(patient_alias, category, modality, isapre, status="agendado", notes=""):
    data = load_data()
    intake = {
        "id": len(data["patients"]) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "alias": patient_alias,
        "category": category, # TDAH, Ansiedad, Crianza, Infanto-juvenil, etc.
        "modality": modality, # Presencial Ñuñoa / Online
        "isapre": isapre,     # Colmena, CruzBlanca, Banmédica, Consalud, Fonasa, Particular
        "status": status,     # contactado, agendado, en_tratamiento, finalizado
        "notes": notes
    }
    data["patients"].append(intake)
    save_data(data)
    print(f"\n✅ Ingreso #{intake['id']} registrado: {patient_alias} ({category} · {modality})")

def show_dashboard():
    data = load_data()
    patients = data.get("patients", [])
    total = len(patients)
    
    agendados = sum(1 for p in patients if p["status"] in ["agendado", "en_tratamiento"])
    en_tratamiento = sum(1 for p in patients if p["status"] == "en_tratamiento")
    contactados = sum(1 for p in patients if p["status"] == "contactado")
    
    progress_pct = (agendados / GOAL_PATIENTS) * 100 if GOAL_PATIENTS > 0 else 0
    estimated_revenue = agendados * SESSION_FEE
    ltv_estimated = agendados * (SESSION_FEE * 8)

    print("\n" + "=" * 75)
    print(" 🌿 CENTRO PAZ — TABLERO DE ADQUISICIÓN Y META DE 100 PACIENTES")
    print("=" * 75)
    print(f" 🎯 Meta de Pacientes Activos:        {GOAL_PATIENTS}")
    print(f" 👥 Total de Consultas Recibidas:    {total}")
    print(f" 📅 Pacientes Agendados / Activos:   {agendados} ({progress_pct:.1f}% de la meta)")
    print(f" 🌱 En Tratamiento Continuo:         {en_tratamiento}")
    print(f" 💬 En Seguimiento WhatsApp:         {contactados}")
    print("-" * 75)
    print(f" 💵 Facturación Estimada (Ingresos): ${estimated_revenue:,.0f} CLP".replace(",", "."))
    print(f" 📈 Proyección de Valor Total (LTV):  ${ltv_estimated:,.0f} CLP (8 sesiones prom.)".replace(",", "."))
    print("=" * 75)

    if patients:
        print("\n📋 Últimos 5 Ingresos Registrados:")
        for p in patients[-5:]:
            print(f"  • [#{p['id']}] {p['date']} | {p['alias']} | {p['category']} | {p['modality']} | Isapre: {p['isapre']} | Estado: {p['status'].upper()}")
    print()

def interactive_intake():
    while True:
        show_dashboard()
        print("Acciones disponibles:")
        print(" 1. ✍️  Registrar nueva consulta / paciente de WhatsApp")
        print(" 2. 🔄  Actualizar estado de un paciente")
        print(" 3. 📊  Ver desglose estadístico por Especialidad e Isapre")
        print(" 0. 🔙  Volver al menú principal")
        
        choice = input("\n👉 Selecciona una opción (0-3): ").strip()
        if choice == "1":
            alias = input("Alias o Iniciales del Paciente (Confidencial, ej: 'P. González' o 'Paciente #1'): ").strip()
            if not alias:
                print("⚠️ El alias no puede estar vacío.")
                continue
            
            print("\nEspecialidad / Motivo de Consulta:")
            print(" 1. TDAH / TEA Adultos")
            print(" 2. Ansiedad / Sobrecarga / Autoestima")
            print(" 3. Infanto-Juvenil & Crianza")
            print(" 4. Consulta General")
            cat_choice = input("Selecciona (1-4): ").strip()
            cat_map = {"1": "TDAH/TEA Adultos", "2": "Ansiedad y Estrés", "3": "Infanto-Juvenil/Crianza", "4": "Consulta General"}
            category = cat_map.get(cat_choice, "Consulta General")

            print("\nModalidad:")
            print(" 1. Presencial en Ñuñoa (Santiago)")
            print(" 2. Online (Videollamada Chile)")
            mod_choice = input("Selecciona (1-2): ").strip()
            modality = "Presencial Ñuñoa" if mod_choice == "1" else "Online Chile"

            print("\nPrevisión de Salud:")
            print(" 1. Colmena | 2. CruzBlanca | 3. Banmédica/Vida Tres | 4. Consalud | 5. Fonasa/Particular")
            isa_choice = input("Selecciona (1-5): ").strip()
            isa_map = {"1": "Colmena", "2": "CruzBlanca", "3": "Banmédica/Vida Tres", "4": "Consalud", "5": "Particular/Fonasa"}
            isapre = isa_map.get(isa_choice, "Particular")

            print("\nEstado Inicial:")
            print(" 1. Agendado (Primera sesión confirmada)")
            print(" 2. En Tratamiento (Proceso activo)")
            print(" 3. Contactado (Evaluando horarios en WhatsApp)")
            st_choice = input("Selecciona (1-3): ").strip()
            st_map = {"1": "agendado", "2": "en_tratamiento", "3": "contactado"}
            status = st_map.get(st_choice, "agendado")

            notes = input("Notas breves (opcional): ").strip()
            add_intake(alias, category, modality, isapre, status, notes)

        elif choice == "2":
            data = load_data()
            if not data["patients"]:
                print("⚠️ No hay pacientes registrados aún.")
                continue
            pid = input("Ingresa el ID del paciente a actualizar: ").strip()
            found = False
            for p in data["patients"]:
                if str(p["id"]) == pid:
                    found = True
                    print(f"\nPaciente seleccionado: {p['alias']} (Estado actual: {p['status']})")
                    print("Nuevo estado: 1. Agendado | 2. En Tratamiento | 3. Finalizado / Alta | 4. Contactado")
                    nst = input("Selecciona (1-4): ").strip()
                    nst_map = {"1": "agendado", "2": "en_tratamiento", "3": "finalizado", "4": "contactado"}
                    p["status"] = nst_map.get(nst, p["status"])
                    save_data(data)
                    print("✅ Estado actualizado con éxito.")
                    break
            if not found:
                print("⚠️ ID no encontrado.")

        elif choice == "3":
            data = load_data()
            patients = data.get("patients", [])
            if not patients:
                print("\n⚠️ No hay datos suficientes para estadísticas.")
                continue
            
            categories = {}
            isapres = {}
            modalities = {}

            for p in patients:
                categories[p["category"]] = categories.get(p["category"], 0) + 1
                isapres[p["isapre"]] = isapres.get(p["isapre"], 0) + 1
                modalities[p["modality"]] = modalities.get(p["modality"], 0) + 1

            print("\n" + "=" * 50)
            print(" 📊 DISTRIBUCIÓN CLÍNICA DE PACIENTES")
            print("=" * 50)
            print("Motivos de Consulta:")
            for k, v in categories.items():
                print(f"  • {k}: {v} pacientes ({(v/len(patients))*100:.1f}%)")
            print("\nPrevisión de Salud:")
            for k, v in isapres.items():
                print(f"  • {k}: {v} pacientes ({(v/len(patients))*100:.1f}%)")
            print("\nModalidad:")
            for k, v in modalities.items():
                print(f"  • {k}: {v} pacientes ({(v/len(patients))*100:.1f}%)")
            print("=" * 50 + "\n")
            input("Presiona Enter para continuar...")

        elif choice == "0":
            break

if __name__ == "__main__":
    interactive_intake()
