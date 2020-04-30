---
title: Docstrings
parent: temathree
nav_order: 4
status: green
tags: [funções, função, def, return, docstring]
---

Criando documentação para suas funções!
{: .lead }

Voltemos ao último exemplo da aula anterior (*Funções*), que era uma função para calcular o quadrado de um número:
```python
def quadrado(x):
  return x * x
```
Você pode tentar usar o comando `help()` para ver o que acontece:
```python
help(quadrado)
```
O resultado será algo assim: 
```
Help on function quadrado in module __main__:

quadrado(x)
```

Não é muito útil, concorda? Mas o que você esperava? O python só sabe executar a sua função, ele não sabe para que ela serve! 

Se você quiser fornecer mensagens para o comando `help()`, coloque uma **docstring** na sua função. Uma *docstring* é quanquer mensagem de texto delimitada por pares de três aspas simples (`'''`) ou duplas (`"""`) logo após o comando `def`, como no exemplo abaixo:  
```python
def quadrado(x):
  '''
    uma função para calcular 
    o quadrado de um número
    
    Entrada (input): x, um float ou int
    Saída (output): o quadrado de x 
  '''
  return x * x
```

Se você agora usar o comando `help(quadrado)`, verá a mensagem acima! Claro que a função acima é muito fácil, mas funções podem ter vários argumentos, alguns opcionais, é também vários valores retornados. É sempre bom, portanto, acrescentar uma docstring para auxiliar os usuários a usar corretamente as funções que você cria. 

:+1: Obviamente eu espero que o seu projeto de software faça amplo uso de docstrings, além de comentários usuais ao longo do código!
{: .alert .alert-primary }
