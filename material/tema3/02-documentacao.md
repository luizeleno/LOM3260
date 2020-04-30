---
title: Documentação
parent: temathree
nav_order: 2
status: green
tags: [funções, função, módulos, help, ajuda, documentação]
---

Aprenda a navegar e entender a documentação de um módulo 
{: .lead }

## Documentação das funções do python básico 

Quando você está em dúvida sobre o que um comando faz, ou quer saber mais detalhes sobre as opções de uma certa função, você pode usar o comando `help` antes de partir para buscas na internet. Por exemplo, para mais informações sobre o  comando `print`, simplesmente digite o seguinte comando em python:
```python
help(print)
```
Isso fará aparecer a seguinte mensagem na janela de saída do seu ambiente python:
```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

A primeira parte da mensagem (*"Help on built-in function print in module builtins:"*) nos diz que `print` é uma função do módulo `builtins` (*integradas*), à qual pertencem a maior parte das funções que vimos até aqui (`range()`, `str()` `input()`, e  por exemplo) e que é carregado por padrão.

A seguir vem a definição da função, ou seja, o que ela faz e todas os argumentos que você pode fornecer ao chamá-la, incluindo os opcionais. No caso do `print`, vemos que o comando tem vários argumentos: `value, ..., sep=' ', end='\n', file=sys.stdout, flush=False`, a maior parte dos quais é opcional. O único argumento obrigatório é `value, ...`, ou seja, uma lista de "valores" (`values`) separados por virgulas --- que é o que você quer imprimir, afinal de contas!

Veremos mais tarde como interpretar a sintaxe dos argumentos opcionais, quando falarmos em mais detalhes sobre funções. Por enquanto, você pode testar o comando `help` com outras funções.

## Documentação de funções de módulos externos

O comando `help` também pode ser usado com funções de módulos externos (inclusive os seus próprios módulos personalizados, como veremos), *desde que os criadores do módulo tenham se preocupado em fornecer essa informação!* Nem sempre, porém, a informação fornecida pelos desenvolvedores de módulos ao comando `help` é de grande ajuda para iniciantes. Por exemplo, importe o módulo `numpy` e procure ajuda sobre a função `sqrt`:
```python
import numpy as np
help(np.sqrt)
```
A longa mensagem fornecida provavelmente será de pouca ajuda para você que está apenas engatinhando em programação em python (e para muitos que se dizem programadores também, é bom que se diga!). Se o comando `help` não te auxiliar em nada, é preciso consultar a documentação específica no manual do módulo. Por sorte, vivemos na era da informação, e essa documentação pode ser facilmente encontrada na internet.

:warning: Consulte sempre primeiro a documentação oficial de um módulo antes de buscar tutoriais independentes! Isso garante que você terá a informação mais correta, escrita pelos próprios criadores do módulo, além de ser uma excelente oportunidade de treinar o inglês.
{: .alert .alert-warning} 

A documentação oficial do `numpy` (e do `scipy`) está no site deles: <https://docs.scipy.org/doc/>{: target="\_blank"}. Vá então para a documentação específica do numpy (<https://docs.scipy.org/doc/numpy/>) e digite `sqrt` no campo de busca (*search*). Um dos primeiros resultados é o que você precisa: `numpy.sqrt`. Clicando no link vocÊ será levado para a documentação oficial da função (este é o endereço: <https://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html>). 

Você descobrirá então que a função `numpy.sqrt` retorna a raiz quadrada não-negativa de um array, elemento por elemento (*Return the non-negative square-root of an array, element-wise*). Ainda não vimos o que é um array, mas você pode considerá-los por enquanto como uma espécie de lista turbinada. O único argumento obrigatório é `x`, o array do qual você quer a raiz quadrada. Não está dito ali, mas funciona também para ints e floats da maneira usual: `numpy.sqrt(5)` e `numpy.sqrt(5.)` vão retornar o valor esperado.
