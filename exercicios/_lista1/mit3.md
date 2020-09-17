---
nav_order: 9
dificuldade: 60
tags: [cond, loop, string]
mathjax: true
title: MIT III
label: mittres
---

(MIT) Escreva um código para imprimir a maior sequência em ordem estritamente alfabética de uma *string* `s` composta unicamente de letras minúsculas. Por exemplo, se `s = 'azcbobobegghakl'`, seu programa deve imprimir `Maior sequência em ordem alfabética: beggh`. Em caso de empate, imprima apenas a primeira subsequência. Por exemplo, se `s = 'abcbcd'`, seu programa deve imprimir `Maior sequência em ordem alfabética: abc`.

<!-- more -->

## Solução

```python
s='azcbobobegghakl'

N = len(s)
start = 0
maxstart = 0
size = 1
maxsize = 1

for i in range(1, N):
	if s[i] >= s[i-1]:
		size += 1
	else:
		start = i
		size = 1
	if size > maxsize:
		maxsize = size
		maxstart = start

a = s[maxstart:maxstart+maxsize]

print(f'Longest substring in alphabetical order is: {a}')
```
