---
nav_order: 11
dificuldade: 10
tags: [cond, loop, list]
mathjax: true
title: Só uma linha
---

Digamos que eu lhe forneça uma lista de números: `a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. Escreva uma única linha em Python que gere uma nova lista apenas com os elementos pares de `a`.

<!-- more -->

### Solução

```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x for x in a if x % 2 == 0])
```


