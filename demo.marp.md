---
marp: true
theme: nobeamer
class: lead
paginate: true
size: 16:9
title: "Demonstração do Tema: nobeamer"
---

# Demonstração do Tema

O objetivo desse demo é mostrar os principais estilos do tema `nobeamer`.

---

## Tipografia Padrão

Texto normal para leitura. O design foca em **contraste** e _legibilidade_.

- Item de lista um
- Item de lista dois
  - Subitem
- Item de lista três

1. Lista ordenada
2. Segundo item

---

## O Card Padrão ("Blockquote")

> Este é o estilo **padrão** para citações ou _destaque geral_.
> Ele serve para quebrar a monotonia e formalidade do slide e ser uma voz mais amigável (**voz do professor**).

```html
> Este é o estilo padrão...
```

---

## Card de Informação (.card-info)

<div class="card-info">
<h3>Dica Útil</h3>
Use este card para fornecer informações adicionais ou dicas de contexto que não são críticas, mas ajudam no entendimento.
</div>

```html
<div class="card-info">
<h3>Dica Útil</h3>
...
</div>
```

---

## Card de Alerta (.card-alert)

<div class="card-alert">
<h3>Cuidado</h3>
Use este estilo para avisos importantes, exceções ou erros comuns que os alunos devem evitar.
</div>

```html
<div class="card-alert">
<h3>Cuidado</h3>
...
</div>
```

---

## Card de Sucesso (.card-success)

<div class="card-success">
<h3>Resultado Correto</h3>
Perfeito para mostrar conclusões, respostas certas ou validações de hipóteses.
</div>

```html
<div class="card-success">
<h3>Resultado Correto</h3>
...
</div>
```

---

## Tabelas e Código

| Estatística | Valor (g) | Descrição |
| :--- | ---: | :--- |
| Média | 100.0 | Valor esperado |
| Desvio | 10.0 | Dispersão |
| Z-Score | 2.5 | Significativo |

```python
def hello():
    print("Hello Marp!")
```

---

## Bloco de Resolução Matemática

<div class="math-resolution">

$$
\begin{aligned}
    P(X \le x) &= \sum_{i=0}^x \binom{n}{i} p^i (1-p)^{n-i} \\
    &= \binom{10}{2} 0.5^2 (0.5)^8 + \dots
\end{aligned}
$$

</div>

```html
<div class="math-resolution">
$$ \begin{aligned} ... \end{aligned} $$
</div>
```
