---
nav_order: 31
dificuldade: 80
tags: [cond, loop, list, func, recurs, desafio]
mathjax: true
title: 'Saindo do labirinto'
label: labirinto
---

Ajude um rato a encontrar um pedaço de queijo num labirinto como o do desenho abaixo:

<div class='w-100 col-md-12'>
{% include figure.html image='/assets/images/labirinto/labirinto.png' id='labirinto' caption='Exemplo de um labirinto'%}
</div>

Um labirinto desses pode ser representado por uma matriz retangular $L$, cujo elemento $\ell_{ij}$ vale $0$ ou $-1$, conforme a casa correspondente do labirinto seja uma passagem livre ou uma parede, respectivamente.

Um método geral para resolver esse problema consiste em marcar com o número $k$ ($k = 1, 2,\ldots$) todas as casas livres que estejam exatamente a $k-1$ passos de distância do queijo, pelo caminho mais curto possível. Suponha que, a cada passo, o rato possa se deslocar de apenas uma casa na vertical ou na horizontal. Então, rotula-se inicialmente a posição do queijo com $1$ e para cada $k\ge2$ examinam-se *todas* as casas livre do labirinto, marcando-se com $k$ aquelas ainda não marcadas e que sejam adjacentes a alguma casa marcada com $k-1$.

A marcação continua até ser atingido um valor $k$ (28 no exemplo abaixo) tal que nenhuma casa esteja em condições de ser marcada. Ao final da marcação teremos a seguinte matriz, supondo o queijo em (5,10), ou seja, no canto inferior direito:

{% include figure.html image='/assets/images/labirinto/labirinto-marcado-1.png' id='lab-marc' caption='Marcação do labirinto' %}

O caminho mais curto até o queijo pode então ser determinado, partindo-se da posição do rato e passando a cada etapa para uma casa adjacente cuja numeração seja menor do que a atual.

Por exemplo, partindo de (0, 0), i.e., o canto superior esquerdo, o rato precisará percorrer pelo menos 26 casas para chegar ao queijo: (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4,2), ..., (4, 10), (4, 15).

Dados o labirinto (matriz $L$) com elementos $0$ e $-1$ e as posições do rato e do queijo, determine o caminho mais curto que o rato deve percorrer até encontrar o queijo, se tal caminho existir.

**Sugestão:** escreva uma função que efetua a marcação (recebendo como argumentos a matriz $L$ e a posição do queijo) e uma outra que imprime o caminho (recebendo como argumentos a matriz $L$ já preenchida e a posição inicial do rato).

Com o código em mãos, teste a sua solução no seguinte labirinto:

<div class='w-100 col-md-12'>
{% include figure.html image='/assets/images/labirinto/labirinto-grande.png' id='labirintogrande' caption='Um labirinto mais complicado'%}
</div>

Baixe o arquivo com a matriz $L$ clicando no botão abaixo com o botão direito e escolhendo *"Salvar link como..."*

<a class='btn btn-primary btn-lg' href='{{site.baseurl}}/assets/images/labirinto/labirinto-grande.txt'>Baixe o arquivo labirinto-grande.txt</a>

O arquivo `labirinto-grande.txt` é composto por 0's e -1's, formando um labirinto de 41 linhas e 101 colunas, com o rato inicialmente na posição (1,0) e o queijo em (39, 100).
