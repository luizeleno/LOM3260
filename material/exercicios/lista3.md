---
title: Terceira Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 12-11-2020 13:19
resolvidos: ['1', '3', '4', '6']
#entrega3: ['2', '7']
# hidden: true
---

{% assign exs = site.lista3 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções

{%if page.resolvidos%}
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
{%endif-%}
<!-- - os exercícios marcados em <span class="badge badge-dark">preto</span> devem ser entregues em dupla no dia 03/12/2020. -->
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice versa!
- use recursos dos módulos `scipy.integrate` à vontade

---

{% include exercicios.html exs=exs %}
