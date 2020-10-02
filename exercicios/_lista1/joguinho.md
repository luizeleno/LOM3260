---
nav_order: 17
dificuldade: 20
tags: [cond, loop]
mathjax: true
title: Joguinho
label: joguinho
---

Implemente o seguinte joguinho de computador: o usuário deve adivinhar um número de 1 a 100 "pensado" pelo computador (use a função `randint()` do módulo `numpy.random`). A cada palpite do usuário, o programa vai "cercando" o número, informando o intervalo $[a,\,b]$ em que ele se encontra. Acompanhe o seguinte exemplo, em que o número secreto é 42:
```
Adivinhe o número:
Está entre 0 e 100: 25
Está entre 25 e 100: 60
Está entre 25 e 60: 40
Está entre 40 e 60:
```
E assim por diante, até o usuário acertar. Não precisa de interface gráfica! Use a função `input()` para pedir ao usuário seu palpite (ou seja, crie uma **TUI** --- *text-based user interface*). Qual é a melhor estratégia para ganhar o jogo no menor número de tentativas?

<!-- more -->

Aqui está um possível algoritmo para o jogo:

```python
import numpy.random as rd

a, b = 1, 100  # o segredo estará em [a,b]

# número secreto a ser adivinhado pelo jogador:
segredo = np.randint(a, b+1)

# Início do jogo:
print('Adivinhe o número:')

n = 1  # n será o contador de tentativas e o indicador (flag) de acerto
while n > 0:
  chute = int(input(f'Está entre {a} e {b}:'))

  if chute > segredo:
    b = chute
    n += 1
  elif chute < segredo:
    a = chute
    n += 1
  else:
    print(f'Acertou em {n} tentativas!')
    n = 0  # zerando n para se tornar um flag de acerto

```
