---
nav_order: 28
dificuldade: 15
tags: [cond, func]
mathjax: true
title: Cômputo da Páscoa
label: pascoa
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

<!-- more -->

```python
def pascoa(ano):
    a = ano % 19
    b, c = ano // 100, ano % 100
    d, e = b // 4, b % 4
    f = ( b + 8 ) // 25
    g = ( b - f + 1 ) // 3
    h = ( 19 * a + b - d - g + 15 ) % 30
    i, k = c // 4, c % 4
    l = ( 32 + 2 * e + 2 * i - h - k ) % 7
    m = ( a + 11 * h + 22 * l ) // 451
    o = h + l - 7 * m + 114
    n, p = o // 31, o % 31
    return p + 1, n

# dicionário para converter mes de int para string
mes = {3:'Março', 4:'Abril'}

x = int(input('Ano: '))
d, m = pascoa(x)

# o formato 02d imprime um inteiro com 2 algarismos, com zeros à esquerda se necessário
print( f'Data da Páscoa em {x}: {d:02d} de {mes[m]}' )
```
