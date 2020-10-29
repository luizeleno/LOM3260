---
nav_order: 7
dificuldade: 30
#tags: [loop, list, func]
mathjax: true
title: Erro na integração 2
label: log
---

Deseja-se calcular

$$
\ln 2 = \int_1^{2} \frac{dx}{x}
$$

com erro inferior a $1/2400$ usando a fórmula dos trapézios. Qual deve ser o passo escolhido? Repita o exercício para a fórmula de Simpson.

:bulb: Se for usar o python para calcular logaritmos naturais (ou seja, em base $e$), use a função `numpy.log`. Se quiser log na base 10, use `numpy.log10` e, em base 2, `numpy.log2`. Para qualquer outra base, use a fórmula de mudança de base, $\log_a b = \log_c a \, / \log_c b$ (e use $c=e$, $10$ ou $2$ em python, apesar de a fórmula valer para qualquer base $c$).
{: .alert .alert-success}
