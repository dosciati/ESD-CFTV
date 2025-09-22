<div align="center">

# 🔧⚡ CFTV Analógico — Comissionamento & Instrumentação (Coaxial)

**Detecte, corrija e valide** problemas de **ESD** e **loops de terra** em enlaces **coaxiais analógicos** (câmera → DVR) com um workflow **claro**, **medível** e **reprodutível**.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#-licen%C3%A7a)
[![Built with](https://img.shields.io/badge/Toolkit-Python%20%7C%20PowerShell-blue.svg)](#-scripts)
[![Field Ready](https://img.shields.io/badge/Field-Ready-orange.svg)](#-deploy-r%C3%A1pido)
[![Issues Welcome](https://img.shields.io/badge/Issues-Welcome-purple.svg)](.github/ISSUE_TEMPLATE)

</div>

> **Por que isso importa?** Em sistemas analógicos, pequenas falhas de **aterramento, blindagem ou terminação** se traduzem em **artefatos visuais**, **picos**, **barras 50/60 Hz** e **indisponibilidade**. Este repositório entrega **procedimento**, **modelos** e **scripts** para fechar o ciclo **diagnóstico → correção → validação → evidência**.

---

## 📚 Sumário
- [Visão Geral](#-visão-geral)
- [Destaques](#-destaques)
- [Arquitetura do Fluxo](#-arquitetura-do-fluxo)
- [Deploy Rápido](#-deploy-rápido)
- [Procedimento (SOP)](#-procedimento-sop)
- [Formulários & Modelos](#-formulários--modelos)
- [Scripts](#-scripts)
- [Relatórios & Evidências](#-relatórios--evidências)
- [Boas Práticas](#-boas-práticas)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🧭 Visão Geral
Este projeto oferece:
- **SOP** enxuto para **comissionamento** e **instrumentação** em **CFTV analógico** (coaxial).
- **Formulários** prontos (XLSX/MD) para registrar medições e aceite.
- **Scripts** para **log**, **validação** de limites técnicos e **geração de relatório**.
- **Templates de issues** para melhoria contínua no campo.

> Resultado: um processo **audível** e **defensável** — do **checklist** à **evidência** final.

---

## ✨ Destaques
- ✅ **Checklist operacional** com limites de referência (isolação, continuidade, DP de terras)  
- ⚡ **Mitigação de ESD**: **SPD coax** + **bonding/equipotencialização** + **terminação 360°**  
- 🧪 **Validação objetiva** via scripts (alertas automáticos)  
- 🧾 **Relatório em Markdown** pronto para anexar ao chamado/OS  
- 🧩 **Modular**: use só o que precisa (SOP, forms, scripts)

---

## 🧱 Arquitetura do Fluxo
```text
[ Diagnóstico ]
   ├─ Inspeção física (malha, emendas, umidade, rota)
   ├─ Ensaios (continuidade, isolação, DP de terras)
   └─ Osciloscópio (picos/ESD, ondulação 50/60 Hz)
        ↓
[ Correção ]
   ├─ Conectividade/terminação (BNC 360°, vedação)
   ├─ Aterramento & equipotencialização (ponto único)
   ├─ Proteção (SPD coax nas duas pontas + SPD energia)
   └─ Roteamento (cruzar a 90°, afastar de EMI)
        ↓
[ Comissionamento ]
   ├─ 24 h de vídeo estável + sem ondulação visível
   ├─ Limites atendidos (Isolação/Continuidade/DP)
   └─ Evidências (fotos, leituras, as built, relatório)
```

---

## ⚙️ Deploy Rápido
```bash
# 1) (opcional) criar um ambiente virtual
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) validar medições coletadas em CSV
python scripts/validate_readings.py forms/Ficha_Medicoes_log.csv

# 3) gerar relatório consolidado em Markdown
python scripts/generate_report.py forms/Ficha_Medicoes_log.csv
```
> Alternativa em campo: usar `scripts/log_medicoes.ps1` para registrar leituras interativamente (gera `forms/Ficha_Medicoes_log.csv`).

---

## 📘 Procedimento (SOP)
O procedimento completo está em **`docs/SOP_Comissionamento.md`**.  
Use-o como **guia de execução** e base de treinamento.

<details>
<summary><b>Checklist essencial (resumo)</b></summary>

**Diagnóstico**  
- Inspeção física → malha/emendas/umidade/rota  
- Continuidade/Isolação (≥ 100 MΩ) / DP terras (ideal: DC < 1 V; AC < 0,5 V)  
- Osciloscópio → picos/ESD e ondulação 50/60 Hz  
- Isolamento por segmento com patch curto

**Correção**  
- BNC de compressão (malha 360°) e vedação externa  
- Bonding e barra equipotencial (ponto único)  
- SPD coax nas duas pontas + SPD de energia  
- Cruzar cabos a 90°, afastar de fontes de EMI  
- Ferrites/isoladores quando indicado

**Aceitação (24 h)**  
- Estabilidade de vídeo, sem ondulação  
- Ensaios dentro dos limites  
- Registros + fotos + as built
</details>

---

## 🗂️ Formulários & Modelos
- **`forms/Ficha_Medicoes.xlsx`** — registro estruturado de leituras.  
- **`forms/Checklist_Conectores.xlsx`** — conformidade dos BNC/vedação.  
- **`forms/Termo_Comissionamento.md`** — aceite final do cliente.

> Dica: mantenha um **código de câmera/ponto** consistente para cruzar evidências e histórico.

---

## 🧪 Scripts
- **`scripts/log_medicoes.ps1`** — coleta interativa de leituras → `Ficha_Medicoes_log.csv`
- **`scripts/validate_readings.py`** — valida leituras (limites de referência) e gera `alertas_validacao.json`
- **`scripts/generate_report.py`** — compila **Relatório de Comissionamento** em Markdown

**Limites de referência (padrões práticos):**
| Métrica                        | Limite recomendado        |
|-------------------------------|---------------------------|
| Continuidade (Ω / 100 m)      | ≤ 3,0 Ω / 100 m           |
| Isolação (MΩ, 250–500 V)      | ≥ 100 MΩ                  |
| DP de terras (DC)             | ≤ 1,0 V                   |
| DP de terras (AC)             | ≤ 0,5 V                   |

> Ajuste limites conforme norma interna/contrato/ambiente (ex.: trechos muito longos).

---

## 🧾 Relatórios & Evidências
- **Markdown consolidado** em `forms/Relatorio_Comissionamento.md` (tabela + alertas).
- **Arquivos brutos** (`Ficha_Medicoes_log.csv`, `alertas_validacao.json`) mantêm **rastreabilidade**.
- Recomendado anexar **fotos** de conectores/SPDs/aterramentos e diagrama **as built**.

---

## ✅ Boas Práticas
- Use **conectores de compressão** (malha 360°) e **vedação** adequada em intempéries.  
- Minimize o comprimento do **condutor ao terra** em SPDs (≤ 30 cm).  
- Evite **múltiplos aterramentos** de shield sem controle (loops).  
- **Cruzamentos a 90°** e afastamento de **drivers/inversores/rádios** reduzem EMI.  
- Em clima seco, monitore **ESD** com mais atenção (proceder com controle de umidade quando possível).

---

## 🤝 Contribuindo
- Abra uma **issue** (bug/feature) usando os templates em `.github/ISSUE_TEMPLATE`.  
- Pull requests são bem-vindos com **descrição do cenário de campo** e evidências.

---

## 📄 Licença
Distribuído sob **MIT License**. Consulte `LICENSE`.
