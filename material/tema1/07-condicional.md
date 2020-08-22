---
title: Testando condições
parent: temaone
nav_order: 6
status: green
tags: [if, elif, else, condições, condicional, decisão]
timestamp: 22/08/20
---

Dicas sobre a construção `if elif else`, usada para testar condições e tomar decisões dentro do código
{: .lead }

A sintaxe é:

```python
if condicao1:
    [comandos1]
elif condicao2:
    [comandos2]
elif condicao3:
    [comandos3]
else:
    [comandos4]
```

onde `condicao` representa variáveis do tipo `bool` (`True` ou `False`), ou testes que resultem em variáveis `bool`. Se `condicao` resulta em `True`, executa os comandos sob o `if`; caso contrário, passa pelos comandos `elif` em sequência, até um deles ser `True`. Se isso não acontece, chega finalmente ao `else`. Todos os `elif` e o `else` são opcionais. Voce pode colocar quantos `elif` você quiser, mas apenas um `else` ao final.

Assim, o seguinte fragmento de código:
```python
x = False
if x:
    a = 1
else:
    a = 2
```
resultará em `a = 2`, e é equivalente a
```python
x = False
if x == True:
    a = 1
else:
    a = 2
```

Na verdade, qualquer valor positivo passado ao comando if será interpretado como True. Por exemplo,
```python
x = 9
if x % 4:
    a = 1
else:
    a = 2
```
resulta em `a = 1`, pois `9 % 4 == 1`, que é positivo e equivale a `True`. Esse fragmento de código é exatamente equivalente ao seguinte:
```python
x = 9
if x % 4 == True:
    a = 1
else:
    a = 2
```

Por outro lado, qualquer valor negativo ou zero será considerado `False`:
```python
x = 8
if x % 4:
    a = 1
else:
    a = 2
```
resulta em `a = 2`. Isso acontece porque `8 % 4` resulta em `0`, que é interpretado como `False` pelo `if`.

O próximo exemplo ilustra estruturas condicionais aninhadas. Analise o seguinte código para encontrar o maior dentre três inteiros:
```python
a, b, c = 2, -3, 5
if a > b:
  if a > c:
    max = a
  else:
    max = c
else:
  if b > c:
    max = b
  else:
    max = c
print(f'O máximo de {a, b, c} é {max}')
```
