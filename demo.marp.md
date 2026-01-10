---
marp: true
theme: nobeamer
class: lead
paginate: true
size: 16:9
title: "Theme Demo: nobeamer"
---

# NOBEAMER GUIDELINES

This document serves as both a demo and a guideline for the `nobeamer` theme.
Follow these rules to create beautiful, handwritten-style presentations.

![bg left:56%](nb_img/paper2.jpg)

---

## 1. Typography & Readability

Normal text for reading. The design focuses on **contrast** and _readability_.

- List item one
- List item two
  - Subitem
- List item three

1. Ordered list
2. Second item

![bg left:10%](nb_img/paper2.jpg)

---

## 2. Using Standard Cards

> Use standard blockquotes for **informal remarks** or "teacher's voice".
> This style mimics a handwritten note and should be used to break the flow of formal content.

```markdown
> This is the standard style...
```

---

## 3. Specialized Cards

> [](#i) **Information**
> Use the **Info Card** for tips, side notes, or context that isn't critical but helpful.

```markdown
> [](#i) **Useful Tip**
> Content...
```

---

> [](#a) **Warning**
> Use the **Alert Card** sparingly for critical warnings or common pitfalls.

```markdown
> [](#a) **Caution**
> Content...
```

---

> [](#s) **Success / Solution**
> Use the **Success Card** for correct answers, conclusions, or good practices.

```markdown
> [](#s) **Correct Result**
> Content...
```

---

## 4. Data Presentation

| Statistic | Value (g) | Description |
| :--- | ---: | :--- |
| Mean | 100.0 | Expected value |
| Deviation | 10.0 | Dispersion |
| Z-Score | 2.5 | Significant |

---

## 5. Code Presentation

```python
def hello():
    print("Hello Marp!")

if __name__ == "__main__":
    hello()
```

---

## 6. Math & Formulas

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

---

## 7. Imagery Guidelines
### Full Background

- Use full backgrounds for **section breaks** or impactful openers.
- Ensure the image has low contrast if you plan to place text over it (or let the theme handle it). 

![bg](nb_img/paper2.jpg)

```markdown
![bg](nb_img/paper2.jpg)
```



---

### Side background

Choose a beautiful image to fill the side of the slide. 

> [](#i) **Empty Space**
> Use side background to avoid empty white spaces.

```markdown
![bg left:56%](nb_img/paper2.jpg)
```

![bg left:56%](nb_img/paper2.jpg)


---

### Side background

... but right
Content comes first 


> [](#i) **Monotony**
> Alter the position of the image to avoid monotony.


```markdown
![bg right:44%](nb_img/paper2.jpg)
```

![bg right:44%](nb_img/paper2.jpg)

---

### Framed figure

Easy way to layout a figure that doesn't fit as as borderless figure. 

```markdown
![bg drop-shadow left:44% 80%](nb_img/paper2.jpg)
```

![bg drop-shadow left:44% 80%](nb_img/paper2.jpg)

---

## Inline figure

Text flows naturally around inline figures. 

![h:200 w:800 drop-shadow](nb_img/paper2.jpg)

> [](#i) **Inline figure**
> Use for panoramic images only.

```markdown
![h:200 w:800 drop-shadow](nb_img/paper2.jpg)
```

