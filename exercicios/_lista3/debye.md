---
nav_order: 5
dificuldade: 50
#tags: [loop, list, func]
mathjax: true
title: Capacidade térmica de sólidos
label: debye
---

A  **função de Debye** é definida como

$$
 D(x) = \frac{9}{x^3} \int_0^x \frac{u^4 e^u}{(e^u-1)^2} du
$$

(cuidado! O integrando não é definido em $u=0$ e você tem que tomar cuidado ao calcular a integral).

No _modelo de Debye_, o **calor específico molar** de um sólido a volume constante é dado por 

$$
 c_v(T) = R D\left(\frac{\theta_D}{T}\right)
$$

sendo $T$ a temperatura em Kelvin, $\theta_D$ a **temperatura de Debye** do material e $R=8.31451\,$J$\,$mol$\,^{-1}$K$\,^{-1}$ a constante universal dos gases. O calor específico molar mede a quantidade de calor que um mol do material absorve/libera numa variação de temperatura.

1. Implemente a função de Debye em python.
1. Faça um gráfico de $c_v$ em função de $T$ para o diamante, para o qual $\theta_D=1849\,$K. No mesmo gráfico, mostre os pontos experimentais encontrados nos seguintes artigos: 
    - K. S. Pitzer, _J. Chem. Phys._ **6** (1938) 68; 
    - A. C. Victor, _J. Chem. Phys._ **36** (1962) 1903. 

    Os dados estão [neste arquivo]({{site.baseurl}}/assets/data/diamante.dat).
