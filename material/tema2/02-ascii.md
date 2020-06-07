---
title: A Tabela ASCII
parent: tematwo
nav_order: 2
status: green
tags:  [string, caracteres, elementos, imutável, ASCII, ord, chr]
timestamp: 07/06/20
---

Historicamente, é a mais importante codificação eletrônica de caracteres
{: .lead }

**ASCII** significa *American Standard Code for Information Interchange.* (Código Padrão Americano para Intercâmbio de Informações). 

Hoje em dia, com a internacionalização da informática, a maioria dos computadores e *softwares* usa codificações diferentes, em geral a *Unicode*, capaz de representar praticamente todas as línguas e alfabetos do mundo, mais caracteres e símbolos para uma variedade incrível de finalidades.

Para simplificar e focar no tema de interesse, nos exercícios vamos nos limitar a tratar *strings* compostas exclusivamente de caracteres ASCII de códigos 32 a 126. A tabela completa você encontra, por exemplo, na [Wikipedia](https://pt.wikipedia.org/wiki/ASCII){: target="\_blank"}. Abaixo segue um resumo:
- Letras maiúsculas (A-Z): 65-90
- Letras minúsculas (a-z): 97-122
- Algarismos (0-9): 48-57

## Como obter o caractere a partir do código numérico (e vice-versa)

Os seguintes comandos em python são úteis para trabalhar com caracteres:
- `ord(c)`: retorna um `int` com a posição do caractere `c` na Tabela ASCII. Por exemplo, `ord('A')` retorna `65`.
- `chr(n)`: retorna o caractere correspondente ao inteiro `n`. Por exemplo, `chr(122)` retorna `'z'`.

