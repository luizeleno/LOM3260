---
nav_order: 17
dificuldade: 20
tags: [cond, loop]
mathjax: true
title: Joguinho
---

Implemente o seguinte joguinho de computador: o usuário deve adivinhar um número de 1 a 100 "pensado" pelo computador (use a função `randint()` do módulo `numpy.random`). A cada palpite do usuário, o programa vai "cercando" o número, informando o intervalo $[a,\,b]$ em que ele se encontra. Acompanhe o seguinte exemplo, em que o número secreto é 42:
```
Adivinhe o número:
Está entre 1 e 100: 25
Está entre 25 e 100: 60
Está entre 25 e 60: 40
Está entre 40 e 60:
```
E assim por diante, até o usuário acertar. Não precisa de interface gráfica! Use a função `input()` para pedir ao usuário seu palpite (ou seja, crie uma **TUI** --- *text-based user interface*). Qual é a melhor estratégia para ganhar o jogo no menor número de tentativas?
