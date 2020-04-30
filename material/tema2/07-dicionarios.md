---
title: Dicionários
parent: tematwo
nav_order: 7
status: green
tags: [dict, dicionário, chaves, itens, elementos, ]
---

Uma poderosa ferramenta para turbinar seu código
{: .lead }

Dicionários são uma espécie de lista, em que os índices, ao invés de uma sequência de inteiros começando em zero, são **chaves** que você mesmo fornece. É muito parecido com um dicionário de verdade, com verbetes e suas definições.

Vejemos um exemplo. Vamos criar um dicionário:
```python
meu_dicio = {'o': 'the', 'livro': 'book', 'está': 'is', 'sobre': 'on', 'a': 'the', 'mesa': 'table'}
```
A variável `meu_dicio` contém o dicionário. Os valores antes dos dois-pontos (`:`) são  as **chaves** (*keys*) e os demais valores são os **itens** (*items*) indexados pelas chaves. Por exemplo,
```python
meu_dicio['o']
```
retorna `the`.

Os dois comandos a seguir usam um recurso chamado *list comprehension*, que vimos na lição anterior:
```python
print([x for x in meu_dicio])
print([meu_dicio[x] for x in meu_dicio])
```
Rode-os em python e tente entender a saída.

## Alguns exemplos de como usar o dicionário na prática:

O comando
```python
palavra='mesa'
print(f'{palavra} em inglês é {meu_dicio[palavra]}')
```
retorna `mesa em inglês é table`

Mais um exemplo:
```python
palavra_pt = 'caderno'
if palavra_pt in meu_dicio:
    # o operador in opera recursivamente por todas as chaves em meu_dicio
    print(f'Eu sei traduzir {palavra_pt} pro inglês: {meu_dicio[palavra_pt]}' )
else:
    print(f'Não faço ideia de como é \'{palavra_pt}\' em inglês')
```
Qual é a saída desse código?

## Tipos de dados para chaves e itens    

As chaves e os itens não precisam necessariamente ser strings. Veja o seguinte exemplo:
```python
dicio = {3: 5, 3.141593: 'pi', 'e': 2.718282}

print(dicio[3])
print(dicio[3.141593])
print(dicio['e'])
```
O que esses comandos `print` imprimem?

## Acrescentar e alterar valores

Uma vez criado um dicionário, é possível acrescentar, remover ou alterar valores. Veja os exemplos abaixo:
```python
dicio = {'animal': 'cachorro', 'fruta': 'laranja', 'cidade': 'Lorena', 'cor': 'vermelho'}

# Acrescentar um valor:
dicio['estado'] = 'SP' 

# Alterar um valor:
dicio['animal'] = 'gato' 

# Remover um valor
dicio.pop('cor')
``` 

## Observação

Também é possível pesquisar no sentido contrário, apesar de ser um pouco mais complicado (não será usado nesse curso). Para isso, não podem haver chaves repetidas, mas itens repetidos são permitidos (por exemplo, 'the' no dicionário `meu_dicio`). Um exemplo:
```python
palavra_en = 'the'
[chave for chave, item in meu_dicio.items() if item is palavra_en]
```
