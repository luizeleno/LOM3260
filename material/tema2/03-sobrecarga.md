---
title: Sobrecarga de operadores
parent: tematwo
nav_order: 3
status: green
mathjax: true
tags: [overload, sobrecarga, operadores]
permalink: /docs/sobrecarga/
timestamp: 23/08/20
---

Um mesmo símbolo pode significar diferentes operadores em python, dependendo dos tipos de dados sobre os quais ele opera
{: .lead }

Imagine que você tenha duas variáveis inteiras e queira calcular a sua soma. Nada mais fácil:
```python
a = 3
b = 8
c = a + b
```
O operador soma, indicado pelo símbolo `+`, é o encarregado de encontrar a soma de suas variáveis do tipo `int`. Repare que o resultado também é do tipo `int` (você pode se assegurar disso com o comando `type(c)` no código acima).

Mas observe agora o código abaixo:
```python
a = 3
b = 8.
c = a + b
```
Veja que não é a mesma coisa que no primeiro código, pois `b` é agora uma variável do tipo `float`, assim como a variável `c` que recebeu a soma `a+b`. Ou seja, o operador `+`, nesse caso, não fez exatamente a mesma coisa que no caso anterior. No entanto, usamos o mesmo símbolo para indicar essas duas operações diferentes (soma de dois `int` retornando um `int` $\neq$ soma de um `int` e um `float` retornando um `float`).

Chamamos esse "abuso" de um mesmo símbolo para indicar coisas diferentes de **sobrecarga** (*overloading*) de operadores e métodos.

Veja outro exemplo de uso do operador `+` que você pode usar para resolver muitos problemas práticos:
```python
a = '3'
b = '8'
c = a + b
print(c)
```
O que você acha que esse comando `print` imprime? Veja que `a` e `b` são do tipo `string` e, não `int`! Nesse caso, o operador `+` é o operador de **concatenação** de strings (como diz uma velha piadinha infantil: *quanto é 1+1? 2? Nao! É 11*).

Na próxima lição veremos como usar operadores "sobrecarregados" para criar facilmente novas listas.
