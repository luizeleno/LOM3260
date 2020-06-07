---
title: Objetos e variáveis
parent: temaone
nav_order: 2
status: green
tags: [objeto, variável, tipo, int, float, string, lógico, boolean, atribuição, atualização]
timestamp: 07/06/20
---

Dois conceitos fundamentais em programação: objetos e variáveis
{: .lead }

<!-- ## Conteúdo
{: .no_toc .text-delta }

1. TOC
{:toc} -->

## O que são *objetos* e *tipos*?

O conceito de **objeto** em programação é um daqueles difíceis de explicar em palavras, mas fácil de entender na prática. Objetos são dados que o seu programa python manipula para realizar as tarefas necessárias para atingir o seu objetivo. Os objetos podem ser de diversos **tipos** (*types*): números inteiros (`int`), números em ponto flutuante (`float`), sequências de caracteres (`string`), listas (**list**), dicionários (**dict**), e muitos outros tipos.

## E o que são variáveis?

Ao criar um objeto de qualquer tipo, é preciso guardá-lo em algum lugar na memória (RAM) do computador, para que o código consiga acessá-lo sempre que necessário. A esse processo dá-se o nome de **atribuição** de um dado a uma **variável**. Por exemplo, 
```python
a = 2
```
significa que atribuímos um dado do tipo `int` (e igual a 2) a uma variável que batizamos de `a`. Leia `a=2` como "`a` recebe `2`" (e não "a igual a 2"). O símbolo `=`, nesse contexto, é chamado de **operador de atribuição**, e não *igual*. Após a atribuição, o `int` 2 está guardado em algum lugar da memória, que chamamos de `a`. Seu código pode acessá-lo sempre que precisar apenas usando o nome da variável. Por exemplo, no código
```python
a = 2
b = 3 * a
```
atribuimos o valor `3 * a` à variável `b`. Como, no ponto do código em que ocorre a linha `a = 3 * a`, na variável `a` está guardado o valor `2`, segue que `b` recebe `6`.

Tome cuidado, no entanto, com o símbolo `=` usado para atribuição. Por exemplo, no seguinte código:
```python
a = 2
b = 3 * a
a = 5
print(b)
```
O que você acha que será impresso pelo comando `print`? Ora, a última vez que o python atribuiu algum objeto à variável `b`, esse objeto era o `int` 6. Ao alterar o valor guardado em `a`, o que estava em `b` não é alterado. Portanto, o comando `print(b)` imprime na tela o valor `6`.

Outra maneira de usar o operador de atribuição (`=`) que causa confusão entre iniciantes em programação é algo como o seguinte código:
```python
a = 2
a = a + 1
print(a)
```
Qual o valor impresso? Bom, na primeira linha, atribuímos o `int` 2 à variável `a`. Na segunda linha, somamos 1 ao valor guardado em `a` (2), cujo resultado é obviamente 3. Esse valor é então atribuído novamente à variável `a`, ou seja, guardamos esse novo resultado no mesmo lugar da memória, atualizando seu valor. Com efeito, o que fizemos foi basicamente alterar o objeto guardado na variável `a`. 

