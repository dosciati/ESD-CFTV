"""
generate_report.py
Gera um relatório consolidado (Markdown) a partir de Ficha_Medicoes_log.csv e alertas_validacao.json.
Uso:
    python generate_report.py forms/Ficha_Medicoes_log.csv
Saída:
    forms/Relatorio_Comissionamento.md
"""
import sys, csv, json, os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Uso: python generate_report.py forms/Ficha_Medicoes_log.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    alertas_path = os.path.join(os.path.dirname(csv_path), "alertas_validacao.json")
    out_md = os.path.join(os.path.dirname(csv_path), "Relatorio_Comissionamento.md")

    # Ler medições
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    # Ler alertas
    alerts = []
    if os.path.exists(alertas_path):
        with open(alertas_path, "r", encoding="utf-8") as f:
            alerts = json.load(f)

    # Construir relatório
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"# Relatório de Comissionamento — CFTV Analógico\n\nGerado em: **{now}**\n\n"
    header += "## Sumário\n- Leituras registradas: **{}**\n".format(len(rows))
    total_alerts = sum(len(x.get("alertas", [])) for x in alerts)
    header += "- Alertas totais: **{}**\n\n".format(total_alerts)

    # Tabela simples (MD)
    table = "| Data | Câmera | Ponto | Cont. Malha (Ω) | Isolação (MΩ) | DP Terras VDC/VAC | Picos | 50/60 Hz | Obs |\n"
    table += "|---|---|---:|---:|---:|---:|---|---|---|\n"
    for r in rows:
        table += "| {Data} | {CameraID} | {Ponto} | {Cont_Malha_Ohm} | {Isolacao_MOhm} | {DP_Terras_VDC}/{DP_Terras_VAC} | {Osc_Picos(Yes/No)} | {Ondul_50_60Hz(Yes/No)} | {Observacoes} |\n".format(**r)

    # Alertas detalhados
    alert_md = "\n## Alertas de Validação\n"
    if not alerts or total_alerts == 0:
        alert_md += "Nenhum alerta encontrado.\n"
    else:
        for a in alerts:
            if a.get("alertas"):
                alert_md += f"- Linha **{a['linha']}** (Câmera **{a.get('camera','')}**):\n"
                for item in a["alertas"]:
                    alert_md += f"  - {item}\n"

    with open(out_md, "w", encoding="utf-8") as f:
        f.write(header + "\n## Leituras\n\n" + table + alert_md)

    print(f"Relatório gerado em {out_md}")

if __name__ == "__main__":
    main()
