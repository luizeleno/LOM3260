---
nav_order: 29
dificuldade: 30
tags: [cond, loop, list]
mathjax: true
title: Triângulo de Pascal
label: pascal
---

O triângulo de Pascal é uma tabela de números construída assim: o elemento da linha $i$ e coluna $j$ (com $0 \le j \le i$ e começando de cima, onde $i=j=0$) é dado por

$$
 a_{i,j} =
 \begin{cases}
1 \quad \text{ se } j=0 \text{ ou }  j=i\\
a_{i-1,j} + a_{i-1,j-1} \,, \text{ se } 1 \lt j \lt  i
\end{cases}
$$

As primeiras oito linhas (ou seja, até $i=7$) são mostradas abaixo:
```
  1
  1  1
  1  2  1
  1  3  3  1
  1  4  6  4  1
  1  5  10 10 5  1
  1  6  15 20 15 6  1
  1  7  21 35 35 21 7  1
```

1. Implemente um algoritmo para calcular as primeiras $n$ linhas do triângulo de Pascal.
1. Modifique o código para substituir os números ímpares do triângulo por 1 e os pares por 0. Use um valor alto de $n$ (algo em torno de 500) e salve o resultado numa matriz. Por fim, use o comando `imshow()` do módulo `matplotlib.pyplot` para exibir graficamente o resultado, que é muito parecido com o fractal chamado de *Triângulo de Sierpinski* (clique [aqui](https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Sierpinski){: target="blank"} e veja na Wikipedia).
