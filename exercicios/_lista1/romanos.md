---
nav_order: 10
dificuldade: 50
tags: [cond, loop, string, dict]
mathjax: true
title: Números romanos
label: romanos
---

Implemente um algoritmo para converter números em algarismos arábicos (por exemplo, 4, 18, 29, 98, 1746) em algarismos romanos (IV, XVIII, XXIX, XCVIII, MDCCXLVI). Limite-se aos valores de 1 a 3999. Se estiver inspirado, implemente a conversão de algarismos romanos para arábicos.

<!-- more -->

## Solução

```python
dict_unidade = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V',
                '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '0': ''}
dict_dezena = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L',
               '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC', '0': ''}
dict_centena = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D',
                '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM', '0': ''}
dict_milhar = {'1': 'M', '2': 'MM', '3': 'MMM', '0': ''}
# inseri 0 nos milhares para facilitar a conversão de romanos para arábicos

dic = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def arabico_para_romano(n):
    arab = f'{n:04d}'  # converte o inteiro n para string, padding com zeros
    rom = dict_milhar[arab[0]]
    rom += dict_centena[arab[1]]
    rom += dict_dezena[arab[2]]
    rom += dict_unidade[arab[3]]
    return rom


def romano_para_arabico(n):
    a = dic[n[-1]]
    N = len(n)
    for i in range(N-1):
        if dic[n[i]] < dic[n[i+1]]:
            a -= dic[n[i]]
        else:
            a += dic[n[i]]
    return a
```
