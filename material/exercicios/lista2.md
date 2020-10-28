---
title: Segunda Lista
parent: exs
nav_order: 2
mathjax: true
remove_trinket: true
timestamp: 10/23/2020, 9:12:33 AM
resolvidos: ['3','8']
entrega2: ['1', '2', '9']
---

{% assign exs = site.lista2 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções

{%if page.resolvidos%}
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
{%-endif-%}
- os exercícios marcados em <span class="badge badge-danger">vermelho</span> devem ser entregues no dia 05/11/2020.
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice versa!
- pode-se usar recursos do módulo `scipy.optimize` à vontade.
- para fazer gráficos rápidos e ajudar a encontrar graficamente raízes, use recursos _online_ como os do [www.desmos.com](https://www.desmos.com/calculator){: target='_blank'}.

---

{% include exercicios.html exs=exs %}
