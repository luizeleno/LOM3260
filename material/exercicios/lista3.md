---
title: Terceira Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 07/06/20
hidden: true
---

{% assign exs = site.lista3 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
- use recursos dos módulos `scipy.integrate` à vontade

---

{% include exercicios.html exs=exs %}
