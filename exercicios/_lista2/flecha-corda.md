---
nav_order: 8
dificuldade: 40
mathjax: true
title: Arco e flecha
label: flecha
---

<div class='float-right col-md-4'>
{% include figure.html image='/assets/images/arco-flecha.png' id='flcd' caption='Corda AB e arco ADB'%}
</div>

A figura representa um círculo de centro em $O$ em que a corda $AB$ mede 10cm e o arco $ADB$ (ao longo da circunferência) mede 12cm. Determine o comprimento da flecha $CD$, sendo $C$ o ponto médio de $AB$. **Dica:** tente descobrir primeiro o ângulo $A\hat{O}C$ e o raio do círculo.

<!-- more -->

<div class='float-right col-md-8'>
{% include figure.html image='/assets/images/tikz/arco-flecha.png' id='flcdsol'%}
</div>

A figura mostra os segmentos e ângulos que vamos utilizar para resolver o problema. Conseguimos duas equações em $R$ (o raio do círculo) e $\theta$ (o ângulo $A\hat{O}C$):

$$
  R \theta = 6
$$

$$
  R \sin \theta = 5
$$

Dividindo uma pela outra e reescrevendo, obtemos

$$
  5 \theta -6 \sin \theta = 0
$$

que resolvemos numericamente:

```python
import numpy as np
import scipy.optimize as spo

def f(th):  # função da qual se quer a raiz
  return 5 * th - 6 * np.sin(th)

c = 1  # chute inicial
th = spo.newton(f, c)

R = 6 / th
CD = R * (1 - np.cos(th))

print(th, R)

print(f'CD={CD}')
```

Obtendo $\theta=1.0267\,$rad (58.827°). Voltando às equações, calculamos $R = 5.8437\,\text{cm}$ e finalmente a flecha $CD$:

$$  CD = R (1-\cos \theta) = 2.8189\text{ cm}$$
