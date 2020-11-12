---
nav_order: 3
dificuldade: 25
mathjax: true
title: Perímetro da elipse
label: elipse
---

O perímetro de uma elipse com semi-eixo maior $a$ e semi-eixo menor $b$ é dado por

$$
 C = 4a \int_0^{\pi/2} \sqrt{ 1 - e^2 \cos^2 \theta} \, d\theta
$$

sendo

$$
e = \sqrt{ 1 - \left(\frac{b}{a} \right)^2 }
$$

 a *excentricidade* da elipse (se $b>a$, troque as posições de $a$ e $b$ na fração). 
 
 1. Calcule $C$ quando $a=20\,$cm e $b=10\,$cm.
 2. Faça um gráfico de $C$ em função de $e$ para $a=10\,$cm no intervalo $0.1 \le e \le 10$. No mesmo gráfico, mostre o perímetro de um círculo de raio $a$.

<!-- more -->

A solução abaixo usa a função `quad` do módulo `scipy.integrate` para o cálculo da integral. Usa também um recurso dessa função: o argumento opcional `args`, que passa outros argumentos que o integrando possa ter além da variável de integração.

Além disso, no item b usei abrangência de listas (_list comprehension_) para gerar numa única linha uma lista de valores em função da excentricidade $e$, que é então convertida em `array`. A primeira coluna contém os valores da integral, a segunda os erros de integração estimados.

Repare também o uso dos métodos `.min()` e `.max()` aplicados ao array `excs` para delimitar os valores do eixo horizontal do gráfico.

Segue o código:

```python
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def integrando(th, e):
    return np.sqrt(1 - (e * np.cos(th))**2)
  
# item a
a, b = 20, 10
e = np.sqrt(1 - (b / a) ** 2)
integral, erro = spi.quad(integrando, 0, np.pi/2, args=(e))
perimetro = 4 * a * integral
print(perimetro)

# item b
a = 10
excs = np.linspace(0.1, 1, 101)
integral = np.array([spi.quad(integrando, 0, np.pi/2, args=(e)) for e in excs])
perimetro = 4 * a * integral[:, 0]

perimetro_circulo = 2 * np.pi * a

plt.figure()
plt.xlim(excs.min(), excs.max())
plt.plot(excs, perimetro, label='elipse')
plt.axhline(perimetro_circulo, color='red', label='circulo')
plt.legend()
plt.show()
```

{% include figure.html image='/assets/images/elipses-sol.png' id='elipsol' caption='Perímetro em função da excentricidade para $a=10$' %}
