---
nav_order: 6
dificuldade: 20
#tags: [loop, list, func]
mathjax: true
title: Erro na integração 1
label: exp
---

Delimite o erro que se comete ao calcular 

$$
\int_0^{0.4} e^x dx
$$

pela fórmula de Simpson com $h=0.1$.

<!-- more -->

A fórmula para a delimitação do erro no cálculo da integral

$$
\int_a^b f(x) \, dx
$$

pelo método de Simpson é 

$$
E \le \frac{|b-a|^5}{180 n^4} \, \max |f^{iv}(x)|
$$

Nesse caso, $a=0$, $b=0.4$ e $f(x)=e^x$, e como todas as derivadas de $f(x)=e^x$ são iguais à própria função, temos que $\max f^{iv}(x)= e^{0.4}=1.491825\,$ (em cálculos numéricos, trabalhe sempre em dupla precisão para evitar perda de algarismos significativos). Além disso, sabemos que

$$
h = \frac{b-a}{n} \quad \Rightarrow \quad n = \frac{b-a}{h}
$$

que nos fornece $n=4$. Com isso, delimitamos o erro em 

$$
E \le \frac{0.4^5}{180 \times 4^4} \times 1.491825 = 3.3152 \times 10^{-7}
$$

Mas, como nesse caso conhecemos o valor exato da integral, podemos calcular o erro cometido ao usar a regra de Simpson (ao invés de apenas delimitá-lo). A integral vale, com doze casas decimais:

$$
\int_0^{0.4} e^x dx = e^{0.4} - e^{0} = 1.491825 - 1 = 0.49182469764
$$

Já a regra de Simpson com $h=0.1$ fornece, com doze casas decimais:

$$
\int_0^{0.4} e^x dx \approx \frac{0.1}{3} \left( e^{0} + 4 e^{0.1} + 2 e^{0.2} + 4 e^{0.3} + e^{0.4} \right) = 0.491824970553
$$

O erro entáo é a diferença entre o valor exato e o aproximado, dentro da precisão de 12 casas decimais:

$$
E = 2.72913 \times 10^{-7}
$$

cujo valor realmente cai dentro do intervalo em que o havíamos delimitado.
