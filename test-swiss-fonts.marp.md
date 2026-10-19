---
marp: true
theme: nobeamer-swiss
paginate: true
size: 16:9
title: "Swiss Font Shootout: Geist vs SUSE vs Liter vs Questrial"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800;900&family=Liter&family=Questrial&family=SUSE:wght@400;500;600;700;800&family=IBM+Plex+Mono:ital,wght@0,400;0,600;0,700;1,400&display=swap');

  section.font-geist {
    --font-heading: "Geist", sans-serif;
    --font-lead-title: "Geist", sans-serif;
    --font-sans: "Geist", sans-serif;
    --font-mono: "IBM Plex Mono", monospace;
  }
  section.font-suse {
    --font-heading: "SUSE", sans-serif;
    --font-lead-title: "SUSE", sans-serif;
    --font-sans: "SUSE", sans-serif;
    --font-mono: "IBM Plex Mono", monospace;
  }
  section.font-liter {
    --font-heading: "Liter", sans-serif;
    --font-lead-title: "Liter", sans-serif;
    --font-sans: "Liter", sans-serif;
    --font-mono: "IBM Plex Mono", monospace;
  }
  section.font-questrial {
    --font-heading: "Questrial", sans-serif;
    --font-lead-title: "Questrial", sans-serif;
    --font-sans: "Questrial", sans-serif;
    --font-mono: "IBM Plex Mono", monospace;
  }

  .shootout-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 14px;
  }
  .shootout-col {
    background: #ffffff;
    border: 1.5px solid #111111;
    padding: 14px 14px 16px 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .shootout-col h3 {
    margin: 0 0 6px 0;
    font-size: 1.05rem;
    border-bottom: 2px solid #E30613;
    padding-bottom: 4px;
  }
  .shootout-col .mini-metric {
    font-size: 38px;
    font-weight: 900;
    line-height: 1;
    margin: 8px 0;
    color: #111111;
    letter-spacing: -0.04em;
  }
  .shootout-col p {
    font-size: 0.78rem;
    line-height: 1.4;
    margin: 4px 0 8px 0;
  }
  .tag-pill {
    display: block;
    background: #111111;
    color: #ffffff;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.62rem;
    font-weight: 700;
    padding: 3px 6px;
    margin-top: 4px;
    text-align: center;
  }

  .specimen-card {
    background: #ffffff;
    border: 1.5px solid #111111;
    padding: 12px 18px;
    margin-bottom: 12px;
  }
  .specimen-card .specimen-label {
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.65rem;
    font-weight: 700;
    color: #E30613;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
  }
  .specimen-card .specimen-title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.04em;
    text-transform: uppercase;
    line-height: 1.1;
    margin: 0 0 4px 0;
  }
  .specimen-card .specimen-body {
    font-size: 0.82rem;
    line-height: 1.4;
    color: #333333;
    margin: 0;
  }

  .table-compact {
    font-size: 0.66em !important;
    margin: 2px 0 6px 0 !important;
    line-height: 1.2 !important;
  }
  .table-compact th, .table-compact td {
    padding: 3px 8px !important;
  }
---

<!-- _class: lead -->

# <!--fit--> SWISS FONT <br> **SHOOTOUT**

### BENCHMARK TIPOGRÁFICO: GEIST vs SUSE vs LITER vs QUESTRIAL

- *ESTILO*: SWISS MODERNISM
- *MOTOR*: NOBEAMER-SWISS
- *AVALIAÇÃO*: PESO, IMPACTO & RIGOR
- *ANO*: 2026

---

## 4-Way Direct Overview

<div class="shootout-grid">

  <div class="shootout-col" style="font-family: 'Geist', sans-serif;">
    <div>
      <h3 style="font-family: 'Geist', sans-serif;">01 // GEIST</h3>
      <div class="mini-metric" style="font-family: 'Geist', sans-serif; font-weight: 900;">99.4%</div>
      <p>Tributo direto da Vercel ao movimento suíço. Black 900 nativo ultra-impactante.</p>
    </div>
    <div>
      <div class="tag-pill">PESOS: 100–900 (VAR)</div>
      <div class="tag-pill" style="background: #E30613;">IMPACTO: EXTREMO</div>
    </div>
  </div>

  <div class="shootout-col" style="font-family: 'SUSE', sans-serif;">
    <div>
      <h3 style="font-family: 'SUSE', sans-serif;">02 // SUSE</h3>
      <div class="mini-metric" style="font-family: 'SUSE', sans-serif; font-weight: 800;">99.4%</div>
      <p>Híbrido de geometria com toque monoespaçado por René Bieder. Muito técnico.</p>
    </div>
    <div>
      <div class="tag-pill">PESOS: 100–800 (VAR)</div>
      <div class="tag-pill" style="background: #E30613;">IMPACTO: ALTO</div>
    </div>
  </div>

  <div class="shootout-col" style="font-family: 'Liter', sans-serif;">
    <div>
      <h3 style="font-family: 'Liter', sans-serif;">03 // LITER</h3>
      <div class="mini-metric" style="font-family: 'Liter', sans-serif; font-weight: 700;">99.4%</div>
      <p>Neo-grotesca suave para telas. No Google Fonts, há apenas o peso Regular 400.</p>
    </div>
    <div>
      <div class="tag-pill">PESOS: APENAS 400</div>
      <div class="tag-pill" style="background: #666666;">IMPACTO: MODERADO</div>
    </div>
  </div>

  <div class="shootout-col" style="font-family: 'Questrial', sans-serif;">
    <div>
      <h3 style="font-family: 'Questrial', sans-serif;">04 // QUESTRIAL</h3>
      <div class="mini-metric" style="font-family: 'Questrial', sans-serif; font-weight: 700;">99.4%</div>
      <p>Grotesca de curvas circulares inspirada na Bauhaus. Apenas peso Regular 400.</p>
    </div>
    <div>
      <div class="tag-pill">PESOS: APENAS 400</div>
      <div class="tag-pill" style="background: #666666;">IMPACTO: SUAVE</div>
    </div>
  </div>

</div>

---

## Direct Headline & Body Specimen Comparison

<div class="specimen-card" style="font-family: 'Geist', sans-serif;">
  <div class="specimen-label">01 // GEIST SANS (PESO 900 / 400)</div>
  <div class="specimen-title" style="font-family: 'Geist', sans-serif; font-weight: 900;">MÖBEL & ARCHITEKTUR: DIE NEUE TYPOGRAFIE ZÜRICH</div>
  <p class="specimen-body" style="font-family: 'Geist', sans-serif;">Rigor matemático, terminais retos, neutralidade absoluta e contraste brutal de escala.</p>
</div>

<div class="specimen-card" style="font-family: 'SUSE', sans-serif;">
  <div class="specimen-label">02 // SUSE (PESO 800 / 400)</div>
  <div class="specimen-title" style="font-family: 'SUSE', sans-serif; font-weight: 800;">MÖBEL & ARCHITEKTUR: DIE NEUE TYPOGRAFIE ZÜRICH</div>
  <p class="specimen-body" style="font-family: 'SUSE', sans-serif;">Geometria moderna com estabilidade monoespaçada para alta legibilidade técnica.</p>
</div>

<div class="specimen-card" style="font-family: 'Liter', sans-serif;">
  <div class="specimen-label">03 // LITER (PESO 400 / FAUX-BOLD)</div>
  <div class="specimen-title" style="font-family: 'Liter', sans-serif; font-weight: 700;">MÖBEL & ARCHITEKTUR: DIE NEUE TYPOGRAFIE ZÜRICH</div>
  <p class="specimen-body" style="font-family: 'Liter', sans-serif;">Neo-grotesca equilibrada com baixa altura de caixa para interfaces e navegação.</p>
</div>

<div class="specimen-card" style="font-family: 'Questrial', sans-serif;">
  <div class="specimen-label">04 // QUESTRIAL (PESO 400 / FAUX-BOLD)</div>
  <div class="specimen-title" style="font-family: 'Questrial', sans-serif; font-weight: 700;">MÖBEL & ARCHITEKTUR: DIE NEUE TYPOGRAFIE ZÜRICH</div>
  <p class="specimen-body" style="font-family: 'Questrial', sans-serif;">Curvatura circular marcante com atmosfera Bauhaus e proporções amplas.</p>
</div>

---

<!-- _class: font-geist cols-2 -->

## Teste 01: Geist (Vercel / Swiss Rationalism)

<div style="padding-top: 6px;">
  <div class="metric">99.4%</div>
  <div class="metric-label">GEIST BLACK 900</div>
  <p style="margin-top: 20px; font-size: 0.92rem; line-height: 1.5; color: #333;">
    Geist entrega peso <strong>Black 900 nativo</strong> para títulos e números gigantes, aliado a pesos 400 e 600 ultra-nítidos para parágrafos.
  </p>
</div>

![split]()

> [](#card) **Rigor Construtivista**
> Tipografia neutra com terminação reta nos caracteres, tracking condensado e escala monumental.

| Camada | Amostra ($N$) | Avaliação |
| :--- | :--- | :--- |
| **H1 Display** | $45,000$ | **PESO 900 NATIVO** |
| **Corpo & Listas** | $28,400$ | **ÓTICA PRECISA** |

<div class="callout-specs" style="margin-top: 12px;">
FONTE: GEIST (VARIABLE 100-900)<br>
IMPACTO DISPLAY: ⭐⭐⭐⭐⭐ (MÁXIMO)
</div>

---

<!-- _class: font-suse cols-2 -->

## Teste 02: SUSE (René Bieder / Geometric Hybrid)

<div style="padding-top: 6px;">
  <div class="metric">99.4%</div>
  <div class="metric-label">SUSE EXTRA-BOLD 800</div>
  <p style="margin-top: 20px; font-size: 0.92rem; line-height: 1.5; color: #333;">
    SUSE possui personalidade técnica com larguras consistentes que lembram interfaces industriais, engenharia e terminais modernos.
  </p>
</div>

![split]()

> [](#card) **Estabilidade Geométrica**
> Desenho híbrido com toques monoespaçados, garantindo separação nítida de glifos em slides densos.

| Camada | Amostra ($N$) | Avaliação |
| :--- | :--- | :--- |
| **H1 Display** | $45,000$ | **PESO 800 NATIVO** |
| **Corpo & Listas** | $28,400$ | **TÉCNICO / ROBUSTO** |

<div class="callout-specs" style="margin-top: 12px;">
FONTE: SUSE (VARIABLE 100-800)<br>
IMPACTO DISPLAY: ⭐⭐⭐⭐☆ (MUITO FORTE)
</div>

---

<!-- _class: font-liter cols-2 -->

## Teste 03: Liter (Neo-Grotesca Contemporânea)

<div style="padding-top: 6px;">
  <div class="metric">99.4%</div>
  <div class="metric-label">LITER (REGULAR 400)</div>
  <p style="margin-top: 20px; font-size: 0.92rem; line-height: 1.5; color: #333;">
    Liter é equilibrada e neutra, mas no Google Fonts conta <strong>apenas com o peso 400</strong>. Em títulos e métricas, depende do faux-bold do navegador.
  </p>
</div>

![split]()

> [](#card) **Proporção Equilibrada**
> Proporções suaves ideais para leitura contínua, interfaces e corpos de texto editoriais.

| Camada | Amostra ($N$) | Avaliação |
| :--- | :--- | :--- |
| **H1 Display** | $45,000$ | **FAUX-BOLD SINTÉTICO** |
| **Corpo & Listas** | $28,400$ | **SUAVE / FLUIDO** |

<div class="callout-specs" style="margin-top: 12px;">
FONTE: LITER (APENAS REGULAR 400)<br>
IMPACTO DISPLAY: ⭐⭐☆☆☆ (SUAVE)
</div>

---

<!-- _class: font-questrial cols-2 -->

## Teste 04: Questrial (Grotesca Circular / Bauhaus)

<div style="padding-top: 6px;">
  <div class="metric">99.4%</div>
  <div class="metric-label">QUESTRIAL (REGULAR 400)</div>
  <p style="margin-top: 20px; font-size: 0.92rem; line-height: 1.5; color: #333;">
    Questrial tem forte influência circular da Bauhaus. No Google Fonts, também está disponível <strong>apenas em peso 400</strong>.
  </p>
</div>

![split]()

> [](#card) **Curvatura Circular**
> Formas circulares nos caracteres e ritmo aberto, gerando uma atmosfera mais amigável e menos brutalista.

| Camada | Amostra ($N$) | Avaliação |
| :--- | :--- | :--- |
| **H1 Display** | $45,000$ | **FAUX-BOLD SINTÉTICO** |
| **Corpo & Listas** | $28,400$ | **ABERTO / AMIGÁVEL** |

<div class="callout-specs" style="margin-top: 12px;">
FONTE: QUESTRIAL (APENAS REGULAR 400)<br>
IMPACTO DISPLAY: ⭐⭐☆☆☆ (SUAVE)
</div>

---

## Matriz Técnica Comparativa

<table class="table-compact">
  <thead>
    <tr>
      <th>Fonte</th>
      <th>Pesos no Google Fonts</th>
      <th>Impacto em Títulos (H1 / Big Numbers)</th>
      <th>Corpo & Parágrafos</th>
      <th>Veredito Swiss Style</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Geist</strong></td>
      <td><strong>100 a 900 (Variável)</strong></td>
      <td>⭐⭐⭐⭐⭐ <strong>Brutal (Black 900)</strong></td>
      <td>⭐⭐⭐⭐⭐ Impecável e neutra</td>
      <td><strong>100% (Purista Suíço)</strong></td>
    </tr>
    <tr>
      <td><strong>SUSE</strong></td>
      <td><strong>100 a 800 (Variável)</strong></td>
      <td>⭐⭐⭐⭐☆ Muito forte (ExtraBold 800)</td>
      <td>⭐⭐⭐⭐☆ Técnico e estável</td>
      <td><strong>95% (Suíço Industrial)</strong></td>
    </tr>
    <tr>
      <td><strong>Liter</strong></td>
      <td><strong>Apenas 400 (Regular)</strong></td>
      <td>⭐⭐☆☆☆ Suave (Faux bold apenas)</td>
      <td>⭐⭐⭐⭐☆ Excelente leitura</td>
      <td><strong>80% (Falta peso pesado)</strong></td>
    </tr>
    <tr>
      <td><strong>Questrial</strong></td>
      <td><strong>Apenas 400 (Regular)</strong></td>
      <td>⭐⭐☆☆☆ Suave (Faux bold apenas)</td>
      <td>⭐⭐⭐☆☆ Aberta e espaçada</td>
      <td><strong>70% (Mais Bauhaus que Suíço)</strong></td>
    </tr>
  </tbody>
</table>

<div class="callout-specs" style="margin-top: 18px;">
ANÁLISE DE IMPACTO:<br>
• SE VOCÊ QUER O IMPACTO PESADO E MONUMENTAL DO SWISS DESIGN: ESCOLHA <strong>GEIST</strong>.<br>
• SE VOCÊ QUER UMA ESTÉTICA MAIS TÉCNICA E INDUSTRIAL: ESCOLHA <strong>SUSE</strong>.<br>
• LITER E QUESTRIAL SÓ POSSUEM PESO 400 NO GOOGLE FONTS, PERDENDO O CONTRASTE BRUTAL DO ESTILO.
</div>
