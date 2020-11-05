---
nav_order: 4
dificuldade: 40
#tags: [loop, list, func]
mathjax: true
title: A função erro
label: erf
---

A **função erro** $(\mathrm{erf})$ é importante em Estatística, Transferência de Calor e Mecânica Quântica, entre outras áreas do conhecimento. Ela é definida pela seguinte integral:

$$
 \mathrm{erf}\,(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt\,,
$$

1. Monte uma tabela da função erro com seis casas decimais para valores de $x$ no intervalo $[0,\ 3]$ com um passo $\Delta x=0.1$.
2. Faça um gráfico da função no mesmo intervalo.
3. Estime graficamente o valor do limite

$$
\lim_{x\to\infty} \mathrm{erf}\,(x) \,.
$$

<!-- more -->

Segue uma solução possível usando arrays e _list compreehension_:

```python
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
  return np.exp(-x*x)

xi, xf, dx =  0, 3, 0.1
x = np.arange(xi, xf+dx, dx)
y = np.array([spi.quad(f, 0, xn) for xn in x])
erf = 2 / np.sqrt(np.pi) * y[:,0]

plt.figure()
plt.plot(x, erf)
plt.show()
```
