---
nav_order: 9
dificuldade: 50
#tags: [loop, list, func]
mathjax: true
title: Escadas
label: escada
---

<div class="float-right col-md-3">
{% include figure.html image='/assets/images/tikz/escadas.png' id='escadas' %}
</div>

Duas escadas, de comprimento $L_1$ e $L_2$, estão apoiadas às paredes de um beco de largura $W$, como na figura.

As escadas se interceptam a uma altura $H$ do chão. Determine $W$ se $L_1=15\,$m, $L_2=10\,$m e $H=4\,$m.

<!-- more -->

<div class="float-right col-md-4">
{% include figure.html image='/assets/images/tikz/escadas-sol.png' id='escadassol' %}
</div>

Considere os comprimentos $a$, $b$, $x$ e $y$ como na figura. Pelo teorema de Pitágoras:

$$
a = \sqrt{L_1^2-W^2} \,, \qquad b = \sqrt{L_2^2-W^2}
$$

Além disso, por semelhança de triângulos,

$$\frac{H}{a} = \frac{x}{W} \quad \Rightarrow \quad x = \frac{HW}{a}$$

$$\frac{H}{b} = \frac{y}{W} \quad \Rightarrow \quad y = \frac{HW}{b}$$

Mas $ x + y = W $, o que leva a

$$ \frac{1}{a} + \frac{1}{b} = \frac{1}{H} $$

que deve ser resolvida numericamente usando, por exemplo, `scipy.optimize.newton`:

```python
import numpy as np
import scipy.optimize as op

L1, L2, H = 15, 10, 4

def f(w):
  a = np.sqrt(L1**2-w**2)
  b = np.sqrt(L2**2-w**2)
  return 1/a + 1/b - 1/H

W = op.newton(f, 6)
print(W)
```

O resultado é $W=8.106$m.
