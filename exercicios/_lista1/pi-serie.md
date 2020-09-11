---
nav_order: 16
dificuldade: 20
tags: [loop]
mathjax: true
title: Pi como uma série
label: pi
---

Calcule as quinze primeiras aproximações para $\pi$ de acordo com a série

$$ \small
\frac{\pi-3}{4} = \frac{1}{2\cdot3\cdot4} - \frac{1}{4\cdot5\cdot6} + \frac{1}{6\cdot7\cdot8} - \ldots
$$

Novamente, não use uma função fatorial, é uma perda de tempo e de recursos computacionais!

<!-- more -->

### Solução

```python
'''
Solução usando for, e eliminando fatores de 4 da fórmula do enunciado:
(pi-3)/4 = 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ...
é simplificada para
pi-3 = 1/(1*3*2) - 1/(2*5*3) + 1/(3*7*4) - ...
'''

soma = 3 # variável que vai receber as aproximações de pi
sinal = 1 # variável com o sinal dos termos da soma
for n in range(1, 16): # sequencia de 15 valores de 1 a 15
    soma += sinal / (n * (2 * n + 1) * (n + 1))
    print(n, soma)
    sinal = -sinal # alternando o sinal do termo
```
