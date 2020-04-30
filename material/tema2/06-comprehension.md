---
title: List comprehension
parent: tematwo
nav_order: 6
status: green
tags: [list, comprehension, dicionário, tupla, string, lista]
---

Uma maneira rápida e elegante de iterar por elementos de uma lista ou string
{: .lead }

Considere o seguinte código usado para multiplicar todos os elementos de uma lista por uma constante:
```python
L = [4, 6, 23, -5, 8, 16]
c = 2
for n in range(len(L)):
  L[n] *= c

print(L)
```
O código acima atinge o objetivo esperado: multiplicar todos os elementos da lista `L` por dois. Mas existe uma outra maneira de fazer isso usando um conceito chamado **list comprehension**, ou *abrangência de lista*. A ideia é usar colchetes (`[]`), que é o indicador de indexação, como sabemos, para criar uma nova lista seguindo a regra encontrada dentro dos colchetes. No caso do exemplo acima, teríamos 
```python
L = [4, 6, 23, -5, 8, 16]
c = 2
Lnovo = [n * c for n in L]
print(Lnovo)
```

A sintaxe completa da construção para **list comprehension** é a seguinte:
```python
[expressao for item in lista if condicao]
```
que tem a seguinte interpretação em plavras: executar o comando `expressao` para (`for`) todo `item` encontrado em (`in`) `lista` se (`if`) a `condicao` é satisfeita (ou seja, retorna `True`). Essa última parte (o `if`) é opcional.

A notação de list comprehension é equivalente ao seguinte aninhamento de um `if` num `for`:
```python
for item in lista:
    if condicao:
        expressao
```

Um outro exemplo: digamos que temos a seguinte lista: 
```python
dados = ['Cristina', 'Jefferson', 13.5, 8, '#af3429', 2-1.j, range(12) ]
```
e queremos extrair apenas as variáveis do tipo `int`, multiplicando-as por 3, deixando de lado os outros dados. Podemos usar list comprehension e fazer:
```python
dados = ['Cristina', 'Jefferson', 13.5, 5, '#af3429', 2-1.j, range(12) ]
dados_int3 = [dado * 3 for dado in dados if type(dado) == int]
print(dados_int3)
```
Veja que, nesse caso, `dados_int3` será uma lista com um único elemento, dado por `15`. 

List comprehension funciona também com strings, tuplas e dicionários! Teste o seguinte exemplo:
```python
dic = {1:'a', 2:'b', 3:'c'}
print('valores no dicionário:')
[print(c, dic[c]) for c in dic]
```
