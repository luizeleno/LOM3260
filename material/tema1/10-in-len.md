---
title: Comandos in e len()
parent: temaone
nav_order: 9
status: green
tags: [in, range, palavras, chave]
timestamp: 07/06/20
---

Dois operadores importantes
{: .lead}

## `in`

O operador `in` serve basicamente para duas situações:

1. iterar por todos os valores de uma lista ou string. É usado geralmente em conjunto com o comando `for`. Por exemplo, o seguinte código:
```python
for n in range(8):
  print(n)
```
vai resultar na seguinte saída:
```
0
1
2
3
4
5
6
7
```

2. Determinar se uma string ou lista contém determinado elemento. É usualmente usado em conjunto com a construção `if elif else`. Por exemplo no codigo abaixo,
```python
s = 'bobo'
c = 'bo'
if c in s:
  print('encontrado!')
```
é retornado `encontrado!`. Nessa situação, o operador `in` itera por todos os elementos de `s`, mesmo sem termos explicitamente estabelecido um laço usando `while` ou `for`. Se a string `c` fizer parte de `s`, a condição `c in s` resultará em `True`.

## `len`

O comando `len()` retorna o tamanho de uma lista ou de um string. Um exemplo:
```python
s = 'EEL/USP'
Ns = len(s)
print(Ns)
```
Esse código retorna `7`, já que `'EEL/USP'` tem sete caracteres.
