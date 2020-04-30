---
title: Tipos de objetos
parent: temaone
nav_order: 3
status: green
mathjax: true
tags: [tipos, objetos, int, float, string, complex, boolean, converter, notação, científica, expoente, exponenciação]
permalink: /docs/tipos/
---

Python tem uma grande variedade de **tipos de objetos** para as mais diversas finalidades
{: .lead }

## Alguns tipos de objetos em python

### Tipos numéricos

Em computação científica, os principais tipos de dados são naturalmente os dados numéricos. O python diferencia entre alguns tipos. Alguns exemplos:
```python
a = 5453  # tipo inteiro (int)
a1 = 5453.  # tipo ponto flutuante (float)

a2 = 5.453e+3  # float em notação científica
a3 = 5.453 * 10**3  # evite fazer explicitamente a exponenciação: você perderá eficiência!

b = 5  # tipo int
b = 5. # tipo float (o ponto no final faz diferença!!!)
b = 5.0  # tipo float - é o mesmo que a linha anterior

c1 = 5.+6.j  # tipo número complexo
```

Repare que `5` é um dado do tipo int, ao passo que `5.` é do tipo float. 

:information_source: Escrever `5.` é o mesmo que `5.0`, ou `5.00`, etc. Uma outra notação é escrever `.5234`, que equivale a `0.5234` (ou seja, podemos ignorar o zero antes da vírgula para definir um float de módulo menor que 1). Vale também para números negativos: `-.12` é o mesmo que `-0.12`.
{: .alert .alert-primary}


:heavy_check_mark: **Notação científica:** Um número em notação científica, por exemplo, $5.23 \times 10^{4}=52300.$, é preferencialmente indicado assim em python: `5.23e4`. Ou seja, o `e` significa `10**`. O expoente pode ser negativo: `5.23e-3` é o float `.00523`.
{: .alert .alert-success}

:x: Evite usar explicitamente a exponenciação quando desnecessário! Por exemplo, nunca defina uma variável como `k = 1.38 * 10**(-23)`. Ao invés disso, use a notação científica: `k = 1.38e-23`. Com isso, você evita fazer contas desnecessariamente, que podem até mesmo levar a uma perda de precisão.
{: .alert .alert-danger}

### Tipo *string*

Outro tipo de dado comum e importante é a **string**, ou sequência de caracteres. Elas são indicadas por qualquer sequência de símbolos (letras, números e caracteres não alfa-numéricos como `?:&(-=+@#)`), delimitados por aspas simples (`''`) ou duplas (`""`).
```python
s1 = 'string 1'  # delimitada por aspas simples
s2 = "String 2"  # delimitada por aspas duplas

w = 'Uma string mais longa com caracteres diferentes: :&%$@%#$'
```
Cuidado quando lidar com strings compostas por caracteres numéricos!
```python
a3 = 5.0  # a3 é do tipo float
s3 = '5.0' # s3 é do tipo string
```

### Tipo booleano (variáveis lógicas)

Dados lógicos ou booleanos (do nome do matemático inglês [George Boole](https://pt.wikipedia.org/wiki/George_Boole){: target="\_blank"}) são basicamente dois: verdadeiro (`True`) e falso (`False`):
```python
v1 = True
v2 = False
```
Eles são importantes para fazer testes de condições, como veremos mais adiante.

## Convertendo entre tipos de objetos

Às vezes é possível converter objetos para outros tipos usando alguns comandos básicos do python. Vejamos alguns exemplos:

### `int` ou `float` para `string`

Use o comando `str()`:
```python
n = 52  # n é do tipo int 
ns = str(n)  # ns é do tipo string 
```

### `String` para `int` ou `float`

Use os comandos `int()` e `float()`:
```python
s = '45.23'
sf = float(s)
si = int(s)  # dá erro! quando for rodar o código, comente essa linha
si = int(sf)  # assim funciona
```
Teste os últimos comandos para ver o que a função `int()` retorna quando `s='45.23'` (uma string) e quando `sf=45.23` (um float).

## Outros tipos de dados

Os tipos de dados não param com os vistos acima. Existem muitos outros, como `range`, `list`, `dict`, `array`, etc. Você pode até mesmo definir novos tipos de dados para atender necessidades específicas do seu código. É impossível descrever todos os tipos básicos de dados nessa altura do curso. Veremos vários deles com o desenrolar do semestre.
