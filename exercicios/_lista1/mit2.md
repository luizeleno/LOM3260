---
nav_order: 8
dificuldade: 30
tags: [cond, loop, string]
mathjax: true
title: MIT II
label: mitdois
---

(MIT) Escreva um código para contar o número de vezes que a sequência `'bob'` aparece numa *string* `s` composta unicamente de letras minúsculas. Por exemplo, se `s = 'azcbobobegghakl'`, seu programa deve imprimir `Número de ocorrências de bob: 2`.

<!-- more -->

### Solução:
```python
s='bobazcbobobobobegbobghakl'
ns = len(s)

v = 'bob'
nv = len(v)

n = 0
for i in range(ns-nv+1):
  if s[i:i+nv] == v:
    n += 1

print(f'Número de ocorrências de {v}: {n}')
```
