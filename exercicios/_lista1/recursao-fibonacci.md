---
nav_order: 24
dificuldade: 30
tags: [cond, func, recurs]
mathjax: true
title: Fibonacci por recursão
label: fibo
---

Usando recursão, implemente uma função para calcular o $n$-ésimo termo da série de Fibonacci,

$$ 0,\ 1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ \ldots $$

que começa com $a_0=0$, $a_1=1$ e em que cada termo $a_n$ ($n \ge 2$) é calculado usando a equação recursiva

$$ a_n = a_{n-1} + a_{n-2}\,. $$

<!-- more -->

Segue uma proposta de função recursiva:

```python
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

Vamos usar a função acima para imprimir os dez primeiros valores da sequência:

```python
for n in range(10):
  print(f'n={n}, a_n = {fibonacci(n)}')
```
