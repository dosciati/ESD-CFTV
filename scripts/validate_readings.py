"""
validate_readings.py
Valida leituras de medições segundo faixas recomendadas.
Uso:
    python validate_readings.py forms/Ficha_Medicoes_log.csv
Saída:
    Console + arquivo JSON com alertas.
"""
import sys, csv, json, os

LIMITS = {
    "cont_ohm_per_100m_max": 3.0,     # ohm/100m (referência prática)
    "isolacao_mohm_min": 100.0,       # MΩ
    "dp_vdc_max": 1.0,                # VDC
    "dp_vac_max": 0.5                 # VAC
}

def parse_float(x):
    try:
        return float(str(x).replace(",", ".").strip())
    except:
        return None

def validate_row(row):
    alerts = []

    cont_malha = parse_float(row.get("Cont_Malha_Ohm"))
    cont_centro = parse_float(row.get("Cont_Centro_Ohm"))
    length_m = parse_float(row.get("ComprimentoEstimado_m"))
    isol_mohm = parse_float(row.get("Isolacao_MOhm"))
    dp_vdc = parse_float(row.get("DP_Terras_VDC"))
    dp_vac = parse_float(row.get("DP_Terras_VAC"))

    # Continuidade (Ohm por 100 m)
    if cont_malha is not None and length_m and length_m > 0:
        ohm_per_100m = cont_malha / (length_m/100.0)
        if ohm_per_100m > LIMITS["cont_ohm_per_100m_max"]:
            alerts.append(f"Malha: {ohm_per_100m:.2f} Ω/100m > {LIMITS['cont_ohm_per_100m_max']} Ω/100m")
    if cont_centro is not None and length_m and length_m > 0:
        ohm_per_100m = cont_centro / (length_m/100.0)
        if ohm_per_100m > LIMITS["cont_ohm_per_100m_max"]:
            alerts.append(f"Centro: {ohm_per_100m:.2f} Ω/100m > {LIMITS['cont_ohm_per_100m_max']} Ω/100m")

    # Isolação
    if isol_mohm is not None and isol_mohm < LIMITS["isolacao_mohm_min"]:
        alerts.append(f"Isolação {isol_mohm} MΩ < {LIMITS['isolacao_mohm_min']} MΩ")

    # DP de terras
    if dp_vdc is not None and dp_vdc > LIMITS["dp_vdc_max"]:
        alerts.append(f"DP Terras DC {dp_vdc} V > {LIMITS['dp_vdc_max']} V")
    if dp_vac is not None and dp_vac > LIMITS["dp_vac_max"]:
        alerts.append(f"DP Terras AC {dp_vac} V > {LIMITS['dp_vac_max']} V")

    # Osciloscópio / Ondulação
    if (row.get("Osc_Picos(Yes/No)") or "").strip().lower() == "yes":
        alerts.append("Osciloscópio: picos/transientes detectados")
    if (row.get("Ondul_50_60Hz(Yes/No)") or "").strip().lower() == "yes":
        alerts.append("Ondulação 50/60 Hz detectada")

    return alerts

def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_readings.py forms/Ficha_Medicoes_log.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"Arquivo não encontrado: {csv_path}")
        sys.exit(1)

    alerts_all = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            alerts = validate_row(row)
            alerts_all.append({"linha": i, "camera": row.get("CameraID"), "alertas": alerts})

    out_json = os.path.join(os.path.dirname(csv_path), "alertas_validacao.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(alerts_all, f, ensure_ascii=False, indent=2)

    print(f"Validação concluída. Alertas salvos em {out_json}")
    # Mostrar resumo
    total_alerts = sum(len(x["alertas"]) for x in alerts_all)
    print(f"Leituras: {len(alerts_all)} | Alertas totais: {total_alerts}")
    for x in alerts_all:
        if x["alertas"]:
            print(f"- Linha {x['linha']} (Câmera {x['camera']}):")
            for a in x["alertas"]:
                print(f"  • {a}")

if __name__ == "__main__":
    main()
