---
title: Quarta Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 12-11-2020 09:27
#hidden: false
resolvidos: ['1', '2']
---

{% assign exs = site.lista4 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções

{%if page.resolvidos%}
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
{%-endif-%}
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice versa!
- use recursos dos módulos `scipy.linalg` à vontade

---

{% include exercicios.html exs=exs %}
