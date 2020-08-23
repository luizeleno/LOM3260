---
nav_order: 30
dificuldade: 40
tags: [cond, loop, list]
mathjax: true
title: Quadrado mágico
---

Um **quadrado mágico** é uma tabela de números em que a soma nas linhas, colunas e diagonais dá sempre o mesmo valor. Por exemplo, na gravura *Melencholia I* de Albrecht Dürer (1471--1528),

| ![]({{site.baseurl}}/assets/images/melencol.jpg){: width="100%"} | ![]({{site.baseurl}}/assets/images/Durer.jpg){: width="100%"} |

a soma dos números é sempre igual a 34 (o quadrádo mágico de Dürer serviu de inspiração para o nome e o logotipo da [Editora 34](http://www.editora34.com.br/quemsomos.htm){: target="blank"}). Outro exemplo simples é o seguinte, em que estão presentes todos os inteiros de 1 a 9 num quadrado $3\times3$:
```
  |---|---|---|
  | 8 | 1 | 6 |
  |---|---|---|
  | 3 | 5 | 7 |
  |---|---|---|
  | 4 | 9 | 2 |
  |---|---|---|
```
e a soma é sempre igual a 15.

Existe um algoritmo para criar quadrados mágicos de ordem ímpar $n$ (a ordem é o número de linhas = número de colunas), preenchidos por todos os inteiros de 1 a $n^2$:

---
### Algoritmo:

| (i) Comece com o número 1 na célula central superior do quadrado (como no exemplo acima); |
| (ii) preencha sequencialmente na diagonal, seguindo para a direita e subindo; |
| (iii) quando atingir as bordas do quadrado, o próximo número é preenchido como se o quadrado estivesse "enrolado" feito uma rosquinha --- ou seja, a borda esquerda "colada" à direita e a superior à inferior. Isso é o que se chama de **condições de contorno periódicas**; |
| (iv) uma exceção é o canto superior direito: quando atingi-lo, o próximo valor vai na célula de baixo; |
| (v) se a próxima célula já está ocupada, o próximo valor vai abaixo do último número preenchido; |
| (vi) continue até chegar em $n^2$ na célula central inferior. |

---

Para ilustrar o uso do algoritmo, vejamos sua aplicação para gerar um quadrado mágico de ordem $n=5$:

- Comece com o passo i, colocando o número 1 na célula central superior
do quadrado:

```
|---|---|---|---|---|
|   |   | 1 |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|---|---|---|---|---|
```

- Ao tentar usar o passo ii para inserir o próximo número (2), não temos
célula acima e à direita da célula anterior (1). Temos então que usar o
passo iii:

```
  |---|---|---|---|---|
  |   |   | 1 |   |   |
  |---|---|---|---|---|
  |   |   |   |   |   |
  |---|---|---|---|---|
  |   |   |   |   |   |
  |---|---|---|---|---|
  |   |   |   |   |   |
  |---|---|---|---|---|
  |   |   |   | 2 |   |
  |---|---|---|---|---|
```

- Alguns passos depois, usando os passos ii e iii, o quadrado estará assim:

```
|---|---|---|---|---|
|   |   | 1 |   |   |
|---|---|---|---|---|
|   | 5 |   |   |   |
|---|---|---|---|---|
| 4 |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   | 3 |
|---|---|---|---|---|
|   |   |   | 2 |   |
|---|---|---|---|---|
```

- Como a próxima célula (1) já está ocupada, usamos o passo v para o
próximo valor (6):

```
|---|---|---|---|---|
|   |   | 1 |   |   |
|---|---|---|---|---|
|   | 5 |   |   |   |
|---|---|---|---|---|
| 4 | 6 |   |   |   |
|---|---|---|---|---|
|   |   |   |   | 3 |
|---|---|---|---|---|
|   |   |   | 2 |   |
|---|---|---|---|---|
```

- Continuando por mais alguns valores, usando os passos ii, iii e v:

```
|----|----|----|----|----|
|    |    | 1  | 8  | 15 |
|----|----|----|----|----|
|    | 5  | 7  | 14 |    |
|----|----|----|----|----|
| 4  | 6  | 13 |    |    |
|----|----|----|----|----|
| 10 | 12 |    |    | 3  |
|----|----|----|----|----|
| 11 |    |    | 2  | 9  |
|--- |----|----|----|----|
```

- Atingido o canto superior direito, o próximo valor (16) vai abaixo dele,
de acordo com o passo iv:

```
|----|----|----|----|----|
|    |    | 1  | 8  | 15 |
|----|----|----|----|----|
|    | 5  | 7  | 14 | 16 |
|----|----|----|----|----|
| 4  | 6  | 13 |    |    |
|----|----|----|----|----|
| 10 | 12 |    |    | 3  |
|----|----|----|----|----|
| 11 |    |    | 2  | 9  |
|--- |----|----|----|----|
```

- E agora continue com os passos ii, iii e v até terminar de preencher o
quadrado:

```
|----|----|----|----|----|
| 17 | 24 | 1  | 8  | 15 |
|----|----|----|----|----|
| 23 | 5  | 7  | 14 | 16 |
|----|----|----|----|----|
| 4  | 6  | 13 | 20 | 22 |
|----|----|----|----|----|
| 10 | 12 | 19 | 21 | 3  |
|----|----|----|----|----|
| 11 | 18 | 25 | 2  | 9  |
|--- |----|----|----|----|
```

Lembre que o algoritmo só vale para valores ímpares de $n$. Existem muitos outros quadrados mágicos de mesma ordem, o algoritmo só fornece uma possibilidade.

1. Qual é a soma em cada linha, coluna e nas duas diagonais, em função de $n$? Responda a essa pergunta usando a cabeça, não o computador!
1. Implemente o algoritmo em python para montar e exibir um quadrado mágico de ordem $n$ ($n$ ímpar) com os números inteiros de 1 a $n^2$. A ordem do quadrado ($n$) deve ser fornecida pelo usuário.
