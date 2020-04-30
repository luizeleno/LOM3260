---
nav_order: 28
dificuldade: 15
tags: [cond, func]
mathjax: true
title: Cômputo da Páscoa
---

A Páscoa cai no primeiro domingo do ano após a lua cheia (mas não a lua cheia real, e sim de acordo com um antigo cômputo (computus) eclesiástico que nada mais tem a ver com a lua que vemos no céu: é apenas um *algoritmo*...) que acontece no ou imediatamente após o equinócio de março (considera-se sempre 21 de março como a data do equinócio, o que nem sempre é verdade, pois pode ser um ou dois dias antes...). Na prática, é mais fácil calcular a data da Páscoa usando o algoritmo de Meeus--Jones--Butcher:
    
| Divida          | por | Quociente | &nbsp; Resto |
|:----------------|:----:|:----------:|:------:|
| o ano $x$       | 19  | --- | $a$ |
| o ano $x$       | 100 | $b$ | $c$ |
| $b$             | 4   | $d$ | $e$ |
| $b+8$           | 25  | $f$ | --- |
| $b-f+1$         | 3   | $g$ | --- |
| $19a+b-d-g+15$  | 30  | --- | $h$ |
| $c$             | 4   | $i$ | $k$ |
| $32+2e+2i-h-k$  | 7   | --- | $l$ |
| $a+11h+22l$     | 451 | $m$ | --- |
| $h+l-7m+114$    | 31  | $n$ | $p$ |

O domingo de Páscoa será então no dia $p+1$ do mês $n$ (3: março, 4: abril). O algoritmo é válido para qualquer ano no calendário gregoriano, ou seja, a partir de 1583. Implemente-o em python e verifique [aqui](https://www.assa.org.au/edm){: target="blank"}. **Dica**: não use o operador `/`, e sim `//` (divisão inteira) para as divisões.
