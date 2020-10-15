---
title: O módulo matplotlib
parent: temafive
status: yellow
tags: [numpy, matplotlib, pyplot, plt, arrays, gráficos, plots, scatter, desvios, erro, barra, legenda, eixos]
timestamp: 10/15/2020, 11:15:31 AM
---

O melhor módulo para criar gráficos em python
{: .lead }

É dificílimo superestimar a qualidade do módulo `matplotlib`. Ele é extremamente versátil para a criação de uma imensa variedade de gráficos 2D e 3D, com uma qualidade impressionante. Apesar de não ser o único módulo para essa finalidade, ele é sem dúvida o mais difundido mundo afora.

Além disso, é impossível (para mim, que tenho um tempo limitado e usado para muitas tarefas dentro da universidade!) deixar aqui mais do que algumas recomendações para o seu uso, na forma de alguns *templates* (modelos) de uso de alguns tipos simples de gráfico. Você encontra muitas outras informações na documentação do matplotlib (<https://matplotlib.org/users/index.html>{: target="\_blank"}) e em tutoriais espalhados pela internet (recomendo este: <https://github.com/rougier/matplotlib-tutorial>{: target="\_blank"}).

Nesse curso veremos apenas como fazer gráficos 2D com o módulo `matplotlib.pyplot`. Teste os exemplos abaixo na caixa do trinket.io para ver o que acontece.

## Gráficos simples

Um gráfico de dados fornecidos em listas:
```python
import matplotlib.pyplot as plt

x = [0, 1, 3, 2, 3, 4]
y = [1, 3, 5, 1, 8, 3]

plt.figure()

plt.plot(x, y)

plt.show()
```

<img src="{{site.baseurl}}/material/tema5/fig1.png" class="mw-100">

Veja que, por padrão, o python apenas liga os dados com linhas, mas não identifica os pontos por símbolos. Troque o comportamento acima mudando a linha com a função `plt.plot` por
```python
plt.plot(x, y, 'o')
```
ou por
```python
plt.plot(x, y, '-o')
```

<div class="row">
<div class="col-md-6">
<img src="{{site.baseurl}}/material/tema5/fig2.png" class="mw-100">
</div>
<div class="col-md-6">
<img src="{{site.baseurl}}/material/tema5/fig3.png" class="mw-100">
</div>
</div>

Existem muitas outras opções de símbolos, tipos de linhas e cores, que você encontra na documentação ou em tutoriais.

:bulb: Você pode usar quantos comandos `plt.plot()` você quiser dentro de um mesmo gráfico!
{: .alert .alert-primary}

## Formatando o gráfico

Vejamos agora como alterar propriedades como rótulos dos eixos, limites do gráfico e legenda. O exemplo abaixo sumariza algumas mudanças.
```python
import matplotlib.pyplot as plt

x = [0, 1, 3, 2, 3, 4]
y = [1, 3, 5, 1, 8, 3]

plt.figure()

plt.plot(x, y, '--o', label='medidas experimentais')

plt.xlim(0,5)
plt.ylim(0,10)

plt.xlabel('valores de $x$')  # veja que dá pra usar LaTeX!
plt.ylabel('valores de $f(x)$')

plt.legend()
plt.show()
```

<img src="{{site.baseurl}}/material/tema5/fig4.png" class="mw-100">

## Gráfico de uma função

Você pode combinar o `matplotlib` com recursos do `numpy` para fazer gráficos de funções matemáticas:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, 2*np.pi, 101)
y = np.cos(x)

plt.figure()

plt.plot(x, y, label='$\cos(x)$')

plt.xlim(-np.pi,2*np.pi)
plt.ylim(-1.2, 1.2)

plt.xlabel('$x$')  # veja que dá pra usar LaTeX!
plt.ylabel('$\cos(x)$')

plt.axhline(y=0, color='k')  # eixo x
plt.axvline(x=0, color='k')  # eixo y

plt.legend()
plt.show()
```

<img src="{{site.baseurl}}/material/tema5/fig5.png" class="mw-100">

## Gráfico com barras de erros

Um tipo de gráfico muito útil para apresentar medidas experimentais, e seus respectivos desvios-padrão, é o gráfico com barras de erros. Os exemplos abaixo mostram o que você deve fazer.

### Desvio constante

Quando o desvio é o mesmo para todos os pontos, faça simplesmente isso:
```python
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 3, 2, 3, 4]
y = [1, 3, 5, 1, 8, 3]

desvio = .5

plt.figure()

plt.errorbar(x, y, yerr=desvio, fmt='ro', ecolor='black', linestyle=None, capsize=2, label='experimental')

plt.legend()
plt.show()
```

<img src="{{site.baseurl}}/material/tema5/fig6.png" class="mw-100">

### Desvio como porcentagem

Digamos agora que o desvio corresponde a 10% dos valores de `y`. Faça o seguinte: troque a definição de `desvio` por `desvio = .1 * np.array(y)`. Veja que, para facilitar a nossa vida, criamos uma versão de `y` como um array antes de multiplicar por 0.1. Caso contrário, teríamos que usar um laço ou list comprehension: `desvio = [.1 * v for v in y]`

<img src="{{site.baseurl}}/material/tema5/fig7.png" class="mw-100">

### Desvio variável.

Digamos agora que os desvios são diferentes para cada ponto, mas não são necessariamente uma porcentagem do valor medido. Nesse caso também não é difícil de criar um gráfico com barras de erros: basta criar uma nova lista (ou array) com os desvios de cada ponto.
```python
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 3, 2, 3, 4]
y = [1, 3, 5, 1, 8, 3]

desvio = [.4, .2, .3, .4, 1, .5]

plt.figure()

plt.errorbar(x, y, yerr=desvio, fmt='ro', ecolor='black', linestyle=None, capsize=2, label='experimental')

plt.legend()
plt.show()
```

<img src="{{site.baseurl}}/material/tema5/fig8.png" class="mw-100">
