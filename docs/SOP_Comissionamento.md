# SOP — Comissionamento & Instrumentação (CFTV Analógico Coaxial)

Este documento descreve o **procedimento operacional padrão** para comissionamento, diagnóstico e mitigação de **ESD** e **loops de terra** em enlaces coaxiais analógicos.

## 0) Segurança
- EPI, bloqueio/etiquetagem, avaliação de risco em altura e intempéries.
- Registro inicial de temperatura/umidade.

## 1) Instrumentos e Materiais
Multímetro TRMS, Megômetro (250–500 V), Osciloscópio (20 MHz+), TDR (opcional), terrômetro (opcional), SPDs (coax/energia), conectores BNC de compressão, fita autofusão/termorretrátil, ferrites, materiais de aterramento.

## 2) Sintomas
- Estalos/picos e riscos diagonais (ESD)
- Barras rolando / 50-60 Hz (loop de terra)
- Ruído granulado que piora em clima seco

## 3) Diagnóstico
1. **Inspeção física** (malha, emendas, umidade, rota).  
2. **Ensaios elétricos**: continuidade (<2–3 Ω/100 m), isolação (>100 MΩ), DP terras (ideal <1 V DC e <0,5 V AC).  
3. **Osciloscópio**: picos/transientes e ondulação 50/60 Hz.  
4. **Isolamento por segmentos** (patch curto no DVR).

## 4) Correções
- Conectividade/terminação (BNC 360°, vedação).
- Aterramento e equipotencialização (ponto único, bonding).
- Proteção (SPDs coax em ambas as pontas + SPD de energia).
- Roteamento/separação (cruzar a 90°; afastar de fontes de EMI).
- Alternativas de isolamento (balun isolado/isoladores de vídeo).

## 5) Comissionamento
- Vídeo estável 24h; sem ondulação visível.
- Ensaios dentro dos limites (registrar).
- SPDs aterrados (trajeto curto ao terra).
- Relatório fotográfico e "as built".

## 6) Registros
Ver planilhas em **forms/**. Os dados coletados alimentam os scripts de validação/relatório em **scripts/**.
