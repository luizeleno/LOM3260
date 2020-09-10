---
nav_order: 2
dificuldade: 20
tags:
mathjax: true
title: Tempo em segundos
---

Escreva um programa que, dada uma duração de tempo em segundos, calcule o número equivalente de dias, horas, minutos e segundos.

Por exemplo, 123554 segundos equivalem a 1 dia, 10 horas, 19 minutos e 14 segundos.

### Dicas:

Nesse exercício, use os operadores // (divisão inteira) e % (resto de divisão). Alguns exemplos:
```python
x = 18
y = x // 3 # retorna o int 6
y = x % 3 # retorna o int 0
y = x // 4 # retorna o int 4
y = x % 4 # retorna o int 2
```

<!-- more -->

## Solução

Existem muitas maneiras de resolver este exercício. Uma proposta é encontrada abaixo:

```python
t = 1423554  # tempo em segundos

s = t % 60  # segundos: 60 s = 1 min
t //= 60  # tempo restante em minutos
m = t % 60  # minutos: 60 min = 1 h
t //= 60  # tempo restante em horas
h = t % 24  # horas: 24 h = 1 dia
d = t // 24  # tempo restante em dias

print(f'{d}d {h}h {m}m {s}s')

# Teste da solução:
t = 60 * ( 60 * (d * 24 + h) + m) + s
print(f'{t}s')

```
