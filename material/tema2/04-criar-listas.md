---
title: Criando novas listas
parent: tematwo
nav_order: 4
status: green
mathjax: true
tags: [overload, sobrecarga, operadores, listas, strings, inicializar]
timestamp: 23/08/20
---

Usando sobrecarga de operadores, vamos ver uma maneira de criar listas e strings de maneira fácil e rápida
{: .lead }

Imagine que você precise de uma lista de 200 elementos, todos iguais a 1. Você poderia fazer o seguinte:
```python
L = []  # uma lista vazia
for i in range(200):
  L.append(1)
print(L)
```
Esse código usa o comando `append`, que não descrevi anteriormente porque não vamos usá-lo neste curso, já que, em computação científica, como veremos, é preferível trabalhar com **arrays**, e não com listas (veremos mais sobre arrays no devido tempo). Mas, basicamente, `L.append(c)` é um *método* para acrescentar o elemento `c` ao final da lista `L`.

O código acima, apesar de funcionar, não é o mais indicado nessa situação. Podemos aproveitar a sobrecarga do operador `*` para "multiplicar" os elementos de uma lista. Veja:
```python
L = [1] * 200
print(L)
```
O comando `[1] * 200` faz exatamente o mesmo que todo o conteúdo do `for` do código-exemplo anterior!  Veja que o código funciona com listas contendo elementos de qualquer tipo:
```python
L = ['Oi'] * 200
print(L)
```
E funciona também para criar strings com caracteres repetidos:
```python
s = 'Oi' * 200
print(s)
```

Concluindo: a sobrecarga do operador `*` é uma ótima maneira de **inicializar** listas e strings.
