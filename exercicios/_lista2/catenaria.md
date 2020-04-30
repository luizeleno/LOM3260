---
nav_order: 1
dificuldade: 25
#tags: [loop, list, func]
mathjax: true
title: Catenária
---

<div class="float-right col-md-6">
{% include figure.html image='/assets/images/tikz/catenaria.png' id='catenaria'%}
</div>

Cabos usados em pontes e linhas de transmissão suportam o próprio peso uniformemente distribuído e assumem um formato conhecido por **catenária**, expresso por

$$
 y(x) = a \cosh\left(\frac{x}{a}\right)
$$

sendo $a$ um comprimento definido na figura e 

$$
 \cosh \theta = \frac{e^\theta+e^{-\theta}}{2}
$$ 

a função **cosseno hiperbólico**.

Considere que o cabo está suspenso entre dois pontos distantes 100m um do outro, com uma máxima deflexão de 20m. Além disso, o cabo tem um peso específico de $w=50\,$N/m. 

Determine as tensões mínima e máxima suportadas pelo cabo, que  acontecem, respectivamente, no meio ($x=0$) e nas extremidades ($x = \pm 50\,$m) e são dadas por $ T_\mathrm{min}= w a $ e $ T_\mathrm{max}= w (a+20)$.
