---
nav_order: 1
dificuldade: 25
#tags: [loop, list, func]
mathjax: true
title: Carro de corrida
label: corrida
---

Um carro de corrida termina uma volta de certo circuito em 84 segundos. Durante a volta, medidas de velocidade (**v**) foram tomadas a cada 6 segundos e resultaram nos valores listados abaixo:

|---
t (s) |  v (km/h) | t (s) |  v (km/h) | t (s) |  v (km/h)
|---
 0  |         124 | 30 |         133 | 60 |         78  |
 6  |         134 | 36 |         121 | 66 |         89  |
 12 |         148 | 42 |         109 | 72 |         104 |
 18 |         156 | 48 |         99  | 78 |         116 |
 24 |         147 | 54 |         85  | 84 |         123 |
|---

Qual é a extensão da pista? Estime o resultado usando tanto o método dos trapézios quanto o de Simpson.

<!-- more -->

A solução abaixo usa as funções vistas em aula:

```python
import numpy as np

v = np.array([124, 134, 148, 156, 147, 133, 121, 109, 99, 85, 78, 89, 104, 116, 123])
v = v / 3.6  # converter km/h para m/s

h = 6.  # intervalo de tempo entre as medidas

# Regra dos Trapézios

s = v[0] + 2 * np.sum(v[1:-1]) + v[-1]
A = .5 * h * s
print(f'A pista tem {A:.2f} m de extensão (trapézios)')

# Regra de Simpson

si = np.sum(v[1::2])
sp = np.sum(v[2:-1:2])
s = v[0] + 4 * si + 2 * sp + v[-1]
A =  h * s / 3.
print(f'A pista tem {A:.2f} m de extensão (Simpson)')
```
