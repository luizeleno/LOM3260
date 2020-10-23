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

<!-- more -->

Segue uma função usando um _array_  em `numpy`:

```python
import numpy as np

def pascal(N):
    '''
    gera as N primeiras linhas do triângulo de Pascal
    (supoe N inteiro não-negativo)
    '''
    v = np.zeros((N, N))  # uma matriz NxN de 0'
    for i in range(N):  # laço para gerar as linhas
        v[i, 0] = 1
        for j in range(1, i+1):  # laço pelas colunas
            v[i, j] = v[i-1, j] + v[i-1, j-1]

    return v
```

Para a segunda parte do exercício, podemos usar a função acima, aliada ao poder de arrays em numpy, e calcular diretamente o resto da divisão por 2. Isso automaticamente substituirá números pares por 0 e ímpares por 1:

```python
N = 500
tri = pascal(N) % 2

import matplotlib.pyplot as plt

plt.figure()
plt.imshow(tri, interpolation='none')
plt.show()
```

:exclamation: É um bom hábito de programação carregar todos os módulos no começo do arquivo, e não fazer como no exemplo acima, em que carreguei o módulo `matplotlib.pyplot` no meio do código (um exemplo do ditado _faça o que eu digo, não faça o que eu faço..._).
{: .alert .alert-warning }

O resultado é a imagem abaixo:

{% include figure.html id='pascaltri' image='/assets/images/sierpinski-pascal.png' caption='Pascal modificado - Sierpinski' %}
