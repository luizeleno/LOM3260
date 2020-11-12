---
nav_order: 25
dificuldade: 25
tags: [loop, list, func]
mathjax: true
title: Ajuste linear
label: ajuste
---

Uma linha de melhor ajuste é uma linha reta que melhor se aproxima de uma coleção de $n$ pontos de dados. Neste exercício, vamos supor que cada ponto na coleção tem uma coordenada $(x_i,\,y_i)$, com $1\le i \le n$. A linha de melhor ajuste é representada pela equação $y = m x + b$, onde $m$ e $b$ são calculados usando as seguintes fórmulas:

$$
m = \frac{ n \sum x_i y_i - \left( \sum x_i \right) \left( \sum y_i \right) }{n \sum x_i^2 - \left( \sum x_i \right)^2}
$$

$$
b = \overline{y} - m \overline{x}
$$

onde os símbolos $\overline{x}$ e $\overline{y}$ são os valores médios de $x$ e $y$, respectivamente. Escreva um programa para ler os pontos contidos num arquivo-texto fornecido pelo usuário (use a função `genfromtxt()` do módulo `numpy`). Então calcule e exiba a linha de melhor ajuste.
Por exemplo, se o usuário fornece as coordenadas $(1,\,1)$, $(2,\,2.1)$ e $(3,\,2.9)$, o seu
o programa deve exibir `y = 0.95 x + 0.1`. Faça também um gráfico com os pontos e a linha de melhor ajuste usando as funções `scatter()` e `plot()` do módulo `matplotlib.pyplot`.

Para testar seu código, use os dados deste arquivo: [dados-linear.csv]({{site.baseurl}}/assets/data/dados-linear.csv)

:bulb: Um arquivo csv é um arquivo-texto em que os dados de cada linha estão separados por vírgulas (csv: _comma separated values_). Qualquer editor de texto é capaz de abri-los, e também programas de planilhas eletrônicas, como o M$Excel
{: .alert .alert-success}

<!-- more -->

## Solução

A solução abaixo faz uso de muitas propriedades de arrays.

```python
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

# Leitura dos dados
import numpy as np
import matplotlib.pyplot as plt

x, y = np.genfromtxt('dados-linear.csv', 
                     delimiter=',', skip_header=1, unpack=True)

# Cálculo da reta de melhor ajuste
n = x.size
sx = x.sum()
sy = y.sum()

sxx = sx**2
sx2 = (x**2).sum()
sxy = (x*y).sum()

m = (n * sxy - sx * sy) / (n * sx2 - sxx)

xm = x.mean()
ym = y.mean()

b = ym - m * xm

# criando a reta de ajuste
xajuste = np.linspace(x.min(), x.max(), 2)  # uma reta só precisa de 2 pontos!
yajuste = m * xajuste + b

# criação do gráfico
plt.figure()

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.plot(x, y, 'o', label='experimental')
plt.plot(xajuste, yajuste, '-', label='ajuste linear')

eq = f'$y(x) = {m:.5f} x {b:+.5f}$'  # formatando números com 5 casas decimais
plt.text(2.5, 3.5, eq)  # colocando a equação no gráfico!

plt.legend()

# salvando a figura como arquivo
plt.savefig('ajuste.png', bbox_inches='tight')

plt.show()
```
