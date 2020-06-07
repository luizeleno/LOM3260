---
title: Laços (loops)
parent: temaone
nav_order: 6
status: green
tags: [loop, laço, for, while, iteração]
timestamp: 07/06/20
---

Uma construção para repetir comandos, ou um grupo de comandos, é chamada de *loop*, ou **laço** em português.
{: .lead }

<!-- ## Nesta página:
{: .no_toc .text-delta }

1. TOC
{:toc} -->

## A construção `while`

Um dos comandos para criar laços é o `while`. A sintaxe do comando é a seguinte:
```python
while bool:
    [comandos]
```
onde `bool` é uma variável lógica, ou um teste que resulte numa variável lógica. Repare que é o mesmo tipo de construção qua a usada para testar condições (`if-elif-else`).

Por exemplo, o seguinte fragmento de código imprime a soma dos números inteiros de 1 a 10:
```python
n = 1
soma = 0
while n <= 10:
    soma += n
    n += 1
print(soma)
```

Repare que o `while` não sabe de antemão quantas iterações serão realizadas: ele precisa testar a condição (`n <= 10`) a cada nova iteração (do latim *iter*: rota). Portanto, se você não tomar cuidado, o `while` pode entrar num *"loop infinito"*.

## A construção `for`

Uma outra maneira de criar laços, quando sabemos exatamente quantas iterações queremos fazer, é usando a construção `for`. A sintaxe do comando pode ser entendida usando o mesmo exemplo acima:
```python
soma = 0
for n in range(1, 11):
    soma += n
print(soma)
```

Ou seja, o for gera valores de 1 a 10 usando o comando `range`, atribuídos sequencialmente a uma variável `n`.

## Observações

- Mais detalhes sobre o comando `range` no próximo material.
- A palavra `in` no comando `for` é uma palavra chave. Mais detalhes em breve.

