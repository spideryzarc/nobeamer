---
marp: true
theme: nobeamer
class: lead
paginate: true
size: 16:9
title: "Theme Demo: nobeamer"
---

# THEME DEMO

The goal of this demo is to showcase the main styles of the `nobeamer` theme.

---

## Default Typography

Normal text for reading. The design focuses on **contrast** and _readability_.

- List item one
- List item two
  - Subitem
- List item three

1. Ordered list
2. Second item

---

## Standard Card ("Blockquote")

> This is the **standard** style for quotes or _general highlights_.
> It serves to break the monotony and formality of the slide and be a friendlier voice (**teacher's voice**).

```html
> This is the standard style...
```

---

## Info Card (.card-info)

> [](#i) **Useful Tip**
> Use this card to provide additional information...

```markdown
> [](#i) **Useful Tip**
> Content...
```

---

## Alert Card (.card-alert)

> [](#a) **Caution**
> Use this style for important warnings...

```markdown
> [](#a) **Caution**
> Content...
```

---

## Success Card (.card-success)

> [](#s) **Correct Result**
> Perfect for showing conclusions...

```markdown
> [](#s) **Correct Result**
> Content...
```

---

## Tables and Code

| Statistic | Value (g) | Description |
| :--- | ---: | :--- |
| Mean | 100.0 | Expected value |
| Deviation | 10.0 | Dispersion |
| Z-Score | 2.5 | Significant |

```python
def hello():
    print("Hello Marp!")
```

---

## Math Resolution Block

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
