---
nav_order: 3
dificuldade: 25
#tags: [loop, list, func]
mathjax: true
title: Catenária
label: catenaria
---

<div class="float-right col-md-6">
{% include figure.html image='/assets/images/tikz/catenaria.png' id='catenaria'%}
</div>

Cabos usados em pontes e linhas de transmissão suportam o próprio peso uniformemente distribuído e assumem um formato conhecido por **catenária**, expresso por

$$
 y(x) = a \cosh\left(\frac{x}{a}\right)
$$

sendo $a$ um comprimento definido na figura e

$$
 \cosh \theta = \frac{e^\theta+e^{-\theta}}{2}
$$

a função **cosseno hiperbólico**.

Considere que o cabo está suspenso entre dois pontos distantes 100m um do outro, com uma máxima deflexão de 20m. Além disso, o cabo tem um peso específico de $w=50\,$N/m.

Determine as tensões mínima e máxima suportadas pelo cabo, que  acontecem, respectivamente, no meio ($x=0$) e nas extremidades ($x = \pm 50\,$m) e são dadas por $ T_\mathrm{min}= w a $ e $ T_\mathrm{max}= w (a+20)$.

<!-- more -->

A catenária passa pelo ponto $x=50,\,y=a+20$, o que fornece a equação

$$
a+20 = a \cosh \left( \frac{50}{a} \right)
$$

que resolvemos numericamente:

```python
import numpy as np
import scipy.optimize as spo

def f(a):  # função da qual se quer a raiz
  return a + 20 - a * np.cosh(50 / a)

c = 65  # chute inicial
a = spo.newton(f, c)
print(a)

w = 50
print(f'Tmin={w*a}, Tmax={w*(a+20)}')
```

Obtemos $a=65.5862\,$m. Com isso, as tensões mínima e máxima são

$$
  T_\text{min} = \omega a = 3279.3\,\text{N}
$$

$$
  T_\text{max} = \omega (a+20) = 4279.3\,\text{N}
$$
