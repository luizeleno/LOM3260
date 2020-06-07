---
title: O comando range
parent: temaone
nav_order: 6
status: green
tags: [range]
timestamp: 07/06/20
---

Gerando sequências de inteiros 
{: .lead }

O comando `range()` gera uma sequência de valores de acordo com a seguinte sintaxe:
```python
range([start,] stop [, step])
```
onde
- `start`: primeiro valor da sequência
- `stop`: último valor, QUE NÃO É INCLUÍDO na sequência gerada
- `step`: passo (diferença) entre os valores da sequência

Os argumentos em colchetes (`[start,]` e `[, step]`) são opcionais. Quando não são fornecidos, valem por padrão 0 (`start`) e 1 (`step`)

## Exemplos:

1. `range(8)` gera os valores 0, 1, 2, 3, 4, 5, 6, 7
  - se o primeiro valor (`start`) não é especificado, ele é 0 por padrão
  - se o passo (`step`) não é especificado, ele é 1 por padrão
  - o último valor (`stop`) **não** é incluído na sequência gerada
1. `range(1, 9)` gera 1, 2, 3, 4, 5, 6, 7, 8
  - aqui fornecemos `start` e `stop`, mas não `step` (que por padrão é 1)
  - novamente, o último valor (`stop`) não é incluído
1. `range(0, 32, 4)` gera 0, 4, 8, 12, 16, 20, 24, 28
  - se você quiser fornecer o `step`, precisa necessariamente fornecer também o `start`
1. os valores também podem ser negativos: `range(-4, 6)` gera -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
1. o passo também pode ser negativo: `range(6, 0, -1)` gera 6, 5, 4, 3, 2, 1

## Observações

 O comando `range()` gera um **objeto do tipo range**. Para conferir se o comando `range` realmente gera a sequência esperada, use o comando `list()` para convertê-lo para um **objeto do tipo lista**. Por exemplo, o comando
```python
x = range(15, 3, -2)
```
gera a sequência 15, 13, 11, 9, 7, 5. Para conferir que isso realmente é verdade, converta-o para um objeto do tipo `list`
```python
y = list(range(15, 3, -2))
```
e o imprima:
```python
print(y)
```

Veremos em breve como trabalhar com objetos do tipo `list`.

