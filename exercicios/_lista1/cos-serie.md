---
nav_order: 15
dificuldade: 30
tags: [cond, loop]
mathjax: true
title: Cosseno como uma série
label: cos
---

Calcule uma aproximação para $\cos x$ através da série

$$ \small
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots
$$

até que o módulo do último termo seja menor que $10^{-6}$. O usuário deve fornecer o valor de $x$. Não use a função fatorial, pois isso é desperdício de tempo de processamento, já que boa parte das operações para o cálculo de um termo da série já foi feita para o termo anterior!

<!-- more -->

### Solução

Vou criar uma função que pede como argumentos o valor de $x$ e, opcionalmente, a precisão do último termo (padrão: $10^{-6}$). Além disso, confere as unidades de $x$ --graus ou radianos--, considerando radianos por padrão.

```python
import numpy as np


def cos_serie(x, tol=1.e-6, unid='rad'):

  '''
    cos_serie calcula cos(x) por série de Taylor com uma tolerância no número de termos

    entrada:
      - x (obrigatório): float de que se deseja calcular o cosseno
      - tol (opcional): módulo do útimo termo é menor do que isso
      - unid (opcional): unidade de x.
          Opções:
            - 'rad' (padrão): x em radianos
            - 'graus': x em graus
  '''

  x0 = x * np.pi / 180 if unid == 'graus' else x

  termo, soma = 1., 1.
  a, b = 2, 1
  while abs(termo) > tol:
    termo *= -x0*x0 / a / b
    soma += termo
    a, b = a+2, b+2

  return soma


# usando a função
x = float(input('x='))
print(f'cos({x}) = {cos_serie(x)}')

```
