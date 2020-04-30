---
title: Variáveis locais e globais
parent: temathree
status: green
mathjax: true
tags: [funções, função, def, return, argumentos, padrão, variável, variáveis, local, global]
timestamp: '11/04/2020'
---

Variáveis criadas dentro de funções são apenas locais: elas não são acessíveis fora do **escopo** da função
{: .lead }

## Variáveis locais

Rode o código abaixo:
```python
def teste_local(x):
    y = x + 2
    return y


x = 5
result = teste_local(x)
print(result)
print(y)
```
O python retornará a seguinte mensagem de erro: `NameError: name 'y' is not defined`. Isso porque a variável `y` é uma **variável local**. Ela existe apenas dentro da função, ou seja, é criada durante a execução da função e, assim que a execução termina, ela é "esquecida".

Para ver se você entendeu o que acontece com variáveis locais, e não se deixar confundir, tente prever o que acontece com o seguinte código:
```python
def SeraQueMuda(x):
  x = x * 2
  return x


x = 5
z= SeraQueMuda(x)
print(x)
```
Que valor o comando `print(x)` imprime?

## Variáveis globais

Você pode dizer explicitamente ao python se você deseja tratar uma variável como **global**. Veja o seguinte código:
```python
def YLocal(x):
    y = x * 2
    return y


x = 5
y = 3
z= YLocal(x)
print(y)
```
Veja que a função `YLocal` não afeta o valor da variável `y` (criada fora da função), pois o que você chamou de `y` dentro da função só existe durante o seu escopo (ou seja, a sua execução). No entanto, diga ao python para tratá-la como uma variável global da seguinte maneira:

```python
def YGlobal(x):
    global y
    y = x * 2
    return y


x = 5
y = 3
z= YGlobal(x)
print(y)
```
Veja que agora a função `YGlobal` altera o valor de `y`, pois essa é agora uma variável tornada  **global**, ou seja, a função deve tratá-la como uma variável externa a si própria.
