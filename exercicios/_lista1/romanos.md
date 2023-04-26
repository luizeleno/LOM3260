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
# DICIONÁRIOS
rom2arab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
arab2rom = {val: key for key, val in rom2arab.items()}  # invertendo r2a usando list comprehension

def det_simb(digit, pos=1):
  '''
    função auxiliar para determinar o símbolo
    correspondente ao dígito (digit: int)
    do número arábico na pos
    pos = 1   -> unidade
        = 10  -> dezena
        = 100 -> centena
  '''
  
  if digit <= 3:  # I, II, III ou X, XX, XXX ou C, CC, CCC
    return arab2rom[pos] * digit
  elif digit == 4:  # IV ou XL ou CD
    return arab2rom[pos] + arab2rom[pos * 5]
  elif digit == 5:  # V ou L ou D
    return arab2rom[pos*5]
  elif 6 <= digit <= 8:  # VI, VII, VIII ou LX, LXX, LXXX ou DC, DCC, DCCC
    return arab2rom[pos*5] + arab2rom[pos] * (digit - 5)
  else:  # IX ou XC ou CM
    return arab2rom[pos] + arab2rom[pos * 10]

def a2r(num):
  '''
    Conversão de número arábico num (int) para romano 
    válido para 1 <= num <= 3999
  '''
  
  arab = f'{num:04d}'
  rom = ''
  # dígito do milhar:
  d = int(arab[0])
  rom = arab2rom[1000] * d
  # dígito da centena:
  d = int(arab[1])
  rom += det_simb(d, pos=100)
  # dígito da dezena:
  d = int(arab[2])
  rom += det_simb(d, pos=10)
  # dígito da unidade:
  d = int(arab[3])
  rom += det_simb(d, pos=1)
  
  return rom

def r2a(rom):
  '''
    conversão de número em algarismos romanos rom (str) para arábicos (int)
  '''
  
  cm = rom[-1]
  num = rom2arab[cm]

  for c in rom[-2::-1]:  # lendo um caractere por vez, de traz para frente, começando do penúltimo
    if rom2arab[c] >= rom2arab[cm]:
      num += rom2arab[c]
    else:
      num -= rom2arab[c]
    cm = c
    
  return num


# TESTE: todos os inteiros de 1 a 3999
for A in range(1, 4000):
    R = a2r(A)  # de arábico para romano
    print(r2a(R), R)  # de romano para arábico
```
