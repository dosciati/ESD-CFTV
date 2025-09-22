# Comissionamento & Instrumentação de Campo — CFTV Analógico (Coaxial)

> **Objetivo:** Guia prático para **detecção, correção e validação** de problemas causados por **descargas eletrostáticas (ESD)** e **loops de terra** em **cabeamento coaxial** de sistemas de monitoramento **totalmente analógicos** (câmera → DVR).

---

## 📌 Escopo
- Enlaces coaxiais (câmera ↔ DVR/placa de captura)
- Aterramento, equipotencialização, proteção e roteamento
- Ensaios de continuidade, isolação, diferença de potencial e análise de ruído

---

## 🔒 0) Segurança e Preparativos
- [ ] **EPI:** óculos, luvas isolantes, bota; atenção a escadas e telhados.
- [ ] **Bloqueio/etiquetagem:** desligar fontes locais quando necessário.
- [ ] **Mapeamento do enlace:** percurso do cabo, caixas de passagem, DG/DCP, eletrocalhas, trechos externos, proximidade a EMI (motores, inversores, luminárias, rádios).
- [ ] **Condições ambientais:** registrar temperatura/umidade (umidade < 40% favorece ESD).

---

## 🧰 1) Instrumentos e Materiais
- [ ] **Multímetro TRMS** (continuidade / queda de tensão)
- [ ] **Megômetro** 250–500 V (isolação condutor central ↔ malha)
- [ ] **Osciloscópio portátil** (20 MHz+) para picos/transientes e ondulação 50/60 Hz
- [ ] **Localizador de cabos** e **TDR** (opcional)
- [ ] **Alicate terrômetro de garra** (opcional)
- [ ] **Barras de equipotencial**, **condutor verde-amarelo** (≥ 4 mm²), terminais, abraçadeiras
- [ ] **SPD coaxial** com **GDT** (BNC, DC–6 GHz) — um na câmera e outro no DVR
- [ ] **SPD de energia** para fontes/rack
- [ ] **Conectores BNC** (compressão/crimp), **fita autofusão** e **termorretrátil**
- [ ] **Ferrites** para supressão de RF (quando indicado)
- [ ] **Baluns isoladores** (se houver conversão pontual para UTP)
- [ ] **Materiais de aterramento** (haste/barramento/cabos)

---

## 🔎 2) Sintomas Típicos (anote ocorrências)
- [ ] **Picos/estalos** aleatórios na imagem, riscos diagonais (ESD)
- [ ] **Barras rolando** ou **ondulação 50/60 Hz** (loop de terra)
- [ ] **Ruído granulado** que piora em clima seco/vento
- [ ] **Artefatos ao tocar/manusear** cabo/carcaça

---

## 🧪 3) Diagnóstico — Passo a Passo

### 3.1 Inspeção Física
- [ ] Continuidade e integridade da **malha** do coax
- [ ] Emendas mal feitas, conectores frouxos, umidade/oxidação
- [ ] Rotas paralelas a **cabos de potência**/drivers/inversores (garantir afastamento)
- [ ] Fonte da câmera (comum/individual), polaridade e **referência de terra**

### 3.2 Ensaios Elétricos
- [ ] **Continuidade** (malha e condutor central): referência **< 2–3 Ω/100 m**
- [ ] **Isolação** condutor ↔ malha (megômetro 250–500 V): **> 100 MΩ**
- [ ] **Diferença de potencial** (terra carcaça câmera ↔ chassi DVR): **< 1 V DC** e **< 0,5 V AC** (ideal).  
      Se DP > 1–2 V → provável falha de **equipotencialização** / retorno de **corrente de fuga**

### 3.3 Osciloscópio
- [ ] Verificar **picos rápidos** (μs–ms) sobre o sinal de vídeo (ESD)
- [ ] Conferir **ondulação 50/60 Hz** (loop de terra)

### 3.4 Isolamento por Segmentos
- [ ] Teste local com **patch coax curto** direto no DVR
- [ ] Resultado limpo localmente e ruim no trajeto → **cabo/rota** é o problema  
- [ ] Resultado ruim localmente → **câmera/fonte**

---

## 🛠️ 4) Correção e Mitigação

### 4.1 Conectividade e Terminação
- [ ] Refazer conectores **BNC** (compressão/crimp) garantindo **360° de malha**
- [ ] Vedação externa com **autofusão + termorretrátil**
- [ ] Evitar **loops de shield** (malha aterrada em múltiplos pontos sem controle)

### 4.2 Aterramento e Equipotencialização
- [ ] **Bonding** de carcaças, caixas e suportes à **barra equipotencial** local
- [ ] **Ponto único** de referência de terra para rack/DVR
- [ ] Medir/registrar a **impedância do sistema de terra** (se aplicável)
- [ ] **Equalizar potenciais** entre fonte da câmera e DVR (condutor dedicado)

### 4.3 Proteção contra Surtos/ESD
- [ ] Instalar **SPD coaxial (GDT)** na **câmera** e no **DVR** com **aterramento curto** (≤ 30 cm)
- [ ] **SPD de energia** para fontes e rack
- [ ] Em ambientes muito secos, considerar **controle de umidade**/ionização

### 4.4 Roteamento e Separação
- [ ] Reposicionar trechos paralelos a **potência**; cruzar a **90°**
- [ ] Afastar de **inversores, motores, luminárias LED** e rádios
- [ ] Usar **ferrites** próximos ao equipamento se persistirem acoplamentos RF

### 4.5 Alternativas de Isolamento
- [ ] Em trechos críticos, avaliar **balun com isolamento** (UTP) se não houver perda de qualidade
- [ ] Considerar **isoladores de vídeo** (transformadores/ópticos)

---

## ✅ 5) Comissionamento — Testes de Aceitação
- [ ] **Vídeo estável** por 24 h (sem estalos/linhas) nas condições típicas
- [ ] **Sem ondulação** 50/60 Hz visível
- [ ] **Isolação** > 100 MΩ e **continuidade** dentro dos limites (registrar valores)
- [ ] **DP de terras** dentro do ideal (DC < 1 V; AC < 0,5 V)
- [ ] **SPDs** montados e **aterrados**; checagem de aperto/torque
- [ ] **Registro fotográfico** e **as built** do trajeto/aterramentos

---

## 🗂️ 6) Documentos de Campo (modelos sugeridos)
- [ ] **Ficha de Medições** (antes/depois): continuidade, isolação, DP de terras, observações
- [ ] **Checklist de Conectores**: tipo, padrão de crimpagem/compressão, vedação
- [ ] **Diagrama de Aterramento/Equipotencial**: barras, condutores, pontos de ligação
- [ ] **Lista de Materiais** aplicados (SPD, cabos, conectores, ferrites)
- [ ] **Relatório Fotográfico** (pontos críticos/correções/rotas)
- [ ] **Termo de Comissionamento** (data, equipe, resultados, aceite)

> **Cenário de referência:** ocorrência de **descarga eletrostática** em enlace coaxial de sistema **totalmente analógico** de monitoramento de imagens (gravação analógica), com atuação voltada a **detecção, correção e estabilização**.

---

## 🧾 Checklist “de Bolso” (resumo imprimível)

**Diagnóstico**  
- [ ] Inspeção física (conector, emenda, umidade)  
- [ ] Continuidade / Isolação do coax  
- [ ] Diferença de potencial entre terras  
- [ ] Osciloscópio: picos / ondulação 50/60 Hz  
- [ ] Isolar trecho (patch curto)

**Correção**  
- [ ] Recrimpar/vedar conectores  
- [ ] Bonding + barra equipotencial  
- [ ] SPD coax nas duas pontas + SPD de energia  
- [ ] Roteamento longe de potência/EMI  
- [ ] Ferrites / isoladores (se necessário)

**Aceitação**  
- [ ] Vídeo 24 h sem artefatos  
- [ ] Sem barras 50/60 Hz  
- [ ] Isolação > 100 MΩ  
- [ ] DP terra dentro do ideal  
- [ ] Registro completo + fotos

---

## 🧩 Notas
- Em **dias secos/ventosos**, intensificar verificação de ESD.  
- **Suportes metálicos** de câmera sem bonding podem concentrar descarga — sempre interligar à barra local.  
- **SPD coax** com cabo de aterramento **curto** é mais efetivo.  
- Conectores **de compressão** (malha 360°) reduzem problemas frente a crimp simples.

---

### Licença
Este material é disponibilizado sob **MIT License**. Sinta-se à vontade para adaptar à sua realidade de campo.
