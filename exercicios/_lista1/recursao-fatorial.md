---
nav_order: 23
dificuldade: 20
tags: [cond, func, recurs]
mathjax: true
title: Fatorial por recursão
label: fat
---

Interprete a saída da seguinte função, que usa uma propriedade conhecida como **recursão**:
```python
def fatorial_recursivo(n):
    if n < 2:
        return 1
    else:
        return n * fatorial_recursivo(n-1)
```

<!-- more -->

A função retorna o fatorial de um inteiro, como você deve ter imaginado. Repare que a função chama ela mesma dentro dela. A isso chamamos de recursão.
