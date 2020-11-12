---
nav_order: 2
dificuldade: 5
title: Circuito elétrico
label: circuitos
---

No circuito elétrico da imagem, a combinação das leis de Ohm e de Kirchhoff fornece, para as correntes $i_1$, $i_2$, ..., $i_5$ (em amperes), o seguinte sistema:

<div class="col-md-6 float-right">
{% include figure.html image='/assets/images/tikz/circuito.png' id='circuito' %}
</div>

$$
 5 i_1 + 5 i_2 = 5.5 
$$

$$
 i_3 - i_4 - i_5 = 0
$$

$$
 2 i_4 - 3 i_5 = 0
$$
 
$$
 i_1 - i_2 - i_3 = 0
$$
 
$$
 5 i_2 - 7 i_3 -2 i_4 = 0
$$

Encontre todas as correntes do circuito.

<!-- more -->

Segue a solução usando `scipy.linalg`:

```python
import scipy.linalg as la

A = [[5, 5, 0, 0, 0], [0, 0, 1, -1, -1], [0, 0, 0, 2, -3], [1, -1, -1, 0, 0], [0, 5, -7, -2, 0]]
b = [5.5, 0, 0, 0, 0]

sol = la.solve(A, b)
print(sol)
```
