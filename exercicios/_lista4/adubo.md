---
nav_order: 1
dificuldade: 10
#tags: [loop, list, func]
mathjax: true
title: Adubação
label: adubo
---

Necessita-se adubar um terreno acrescentando, a cada 10m², 140g de nitrato, 190g de fosfato e 205g de potássio. Dispõe-se de quatro qualidades de adubo com as seguintes características:

- Cada quilograma do adubo I custa 5 reais e contém 10g de nitrato, 10g de fosfato e 100g de potássio;
- Cada quilograma do adubo II custa 6 reais e contém 10g de nitrato, 100g de fosfato e 30g de potássio;
- Cada quilograma do adubo III custa 5 reais e contém 50g de nitrato, 20g de fosfato e 20g de potássio;
- Cada quilograma do adubo IV custa 15 reais e contém 20g de nitrato, 40g de fosfato e 35g de potássio;

Quanto de cada adubo devemos misturar para conseguir o efeito desejado se estamos dispostos a gastar 54 reais para cada 10m² de terreno?

<!-- more -->

Segue uma solução usando `scipy.linalg`

```python
import scipy.linalg as la

A = [[5, 6, 5, 15], [10, 10, 50, 20], [10, 100, 20, 40], [100, 30, 20, 35]]
b = [54, 140, 190, 205]

sol = la.solve(A, b)
print(sol)
```
