---
nav_order: 7
dificuldade: 10
tags: [cond, loop, string]
mathjax: true
title: MIT I
label: mitum
---

(MIT) Escreva um programa que conte o número de vogais numa *string* `s` composta unicamente de letras minúsculas. Por exemplo, se `s = 'azcbobobegghakl'`, seu programa deve imprimir `Número de vogais: 5`.

<!-- more -->

### Solução:
```python
s = input('Digite uma string de letras minúsculas: ')

n = 0
v = 'aeiou'

for letter in s:
  if letter in v:
    n += 1

print(f'Número de vogais: {n}')
```
