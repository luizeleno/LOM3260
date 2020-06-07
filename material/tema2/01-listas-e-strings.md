---
title: Strings, listas e tuplas
parent: tematwo
nav_order: 1
status: green
tags: [list, lista, string, caracteres, elementos, tupla, tuple, editável, imutável]
timestamp: 07/06/20
---

Três *tipos de objetos* parecidos e importantíssimos em python
{: .lead }

## Definições de strings, listas e tuplas

Strings, listas e tuplas (*tuples* em inglês) são tipos de dados muito parecidos em python. Todos são, basicamente, conjuntos de dados armazenados numa única variável. Vejamos alguns exemplos:
```python
# strings:
s1 = 'eu sou uma string'
s2 = "eu também! eu sou uma outra string"

# listas
L1 = ['e', 'u', 'a', 'dados', 'EEL']
L2 = [1, 2, 6, 7, 12 , -1, 0]
L3 = [1.45, 0.45, 1.45]
n = 5
L4 = [n, n*n, 2*n, 8, 5]

# uma tupla
T1 = ('e', 'u', 'a', 'dados', 'EEL')
T2a = (5, 7, 2, 8, 12, 't')
T2b = 5, 7, 2, 8, 12, 't'
```  
Repare que uma string é identificada por aspas simples (`''`) ou duplas (`""`). Elas formam palavras ou frases e são simplesmente, na verdade, sequências de caracteres.

Já listas e tuplas são conjuntos de dados agrupados formando... listas (!). Repare que listas são delimitadas por colchetes (`[]`) e tuplas por parênteses (`()`) ou por nada, apenas separando os elementos por vírgulas.

## Qual a diferença entre strings, listas e tuplas?

A diferença entre esses tipos de objetos é que listas são **editáveis**: após criadas, é possível alterar qualquer um de seus elementos. Já strings e tuplas são **imutáveis**: após criadas, elas não podem ser editadas, apenas sobrescritas.

*Como* editar listas será visto na próxima lição ("Indexing e Slicing").

