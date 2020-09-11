---
nav_order: 6
dificuldade: 10
tags: [cond, loop]
mathjax: true
title: Máximo divisor comum
label: mdc
---

O máximo divisor comum (MDC) de dois inteiros positivos, $n$ e $m$, é o maior número, $d$, capaz de dividir $n$ e $m$ sem deixar resto. Existem vários algoritmos para determinar $d$, incluindo o seguinte:

| 1. inicialize $d$ como o menor entre $m$ e $n$;|
| 2. enquanto $d$ não dividir exatamente $m$ e $n$, diminua o valor de $d$ de uma unidade.|

Ao final do algoritmo, $d$ sera o MDC de $n$ e $m$. Escreva um programa que leia dois inteiros positivos do usuário e use esse algoritmo para determinar e relatar seu máximo divisor comum.

<!-- more -->

### Solução:

```python
# Entrada
m = int(input('m = '))
n = int(input('n = '))

# Algoritmo

# encontrando o menor valor
if m < n:
  d = m
else:
  d = n

# encontrando o MDC(m, n)
while m % d or n % d :
  d -= 1

'''
comentário:
veja que
while m % d or n % d:
é o mesmo que
while m % d != 0 or n % d != 0:
pois qualquer valor positivo significa True,
e qualquer valor zero ou negativo resulta em False
'''

# Saída

print(f'MDC({m}, {n}) = {d}')
```
