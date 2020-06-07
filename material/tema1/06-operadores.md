---
title: Operadores
parent: temaone
nav_order: 5
status: green
tags: [operador, operadores, comparação, lógicos, incremento, operando, aritmético, lógico, comparação, atribuição]
timestamp: 07/06/20
---

Numa expressão como `c = a op b`, `a` e `b` são chamados *operandos* e `op` é um **operador**. Os operadores abaixo (com exceção do `not`) agem sobre dois *operandos* e produzem (*retornam*) um resultado, que depende dos tipos de dados dos operandos.
{: .lead}

## Operadores aritméticos

- adição: `+` 
- subtração: `-`
- multiplicação: `*`
- divisão: `/`
- exponenciação: `**`
- resto de divisão: `%`
- divisão inteira: `//`

**Regra:** se `op` é qualquer dos operadores acima, temos que:
- `int op int` retorna `int`
- `int op float` retorna `float` 
- `c op int` retorna `float`
- `float op float` retorna `float`

**Obs.:** Consulte a aula de [*Sobrecarga de operadores*]({{site.baseurl}}/docs/sobrecarga/) para outro uso do operador adição quando os operandos são `string`.

## Operadores de comparação

Se a comparação é satisfeita, os operadores de comparação retornam `True` (tipo booleanno, ver aula sobre [tipos de dados]({{site.baseurl}}/docs/tipos/)). Caso contrário, retornam `False`.
- igualdade: `==`
- não igualdade: `!=` ou `<>` contrário
- maior que: `>`
- maior ou igual a: `>=`
- menor ou igual a: `<=`

## Operadores de atribuição

- atribuir à variável: `=`
- somar e atribuir à variável: `+=` (`a += b` equivale a `a = a + b`)
- subtrair e atribuir à variável: `-=` (`a -= b` equivale a `a = a - b`)
- multiplicar e atribuir à variável: `*=` (`a *= b` equivale a `a = a * b`)
- dividir e atribuir à variável: `/=` (`a /= b` equivale a `a = a / b`)
- exponenciar e atribuir à variável: `**=` (`a **= b` equivale a `a = a ** b`)
- achar o resto e atribuir à variável: `%=` (`a %= b` equivale a `a = a % b`)
- achar a divisão inteira e atribuir à variável: `//=` (`a //= b` equivale a `a = a // b`)

## Operadores lógicos

- `and`: retorna `True` se (e somente se) ambos os operandos são `True`, senão retorna `False`
- `or`: retorna `True` se qualquer um dos operandos é `True`, senão retorna `False`
- `not`: usado para reverter o estado lógico de um operando (exemplo: `not(4 > 3 and 5 > 2)` retorna `False`)

Alguns exemplos:
```python
a, b = 3, 4
x = a > b and a > 0  
y = a > b or a > 0
print(x, y)
```
Esse código imprime `False True`

