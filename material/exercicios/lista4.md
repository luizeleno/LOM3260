---
title: Quarta Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 10/5/2020, 4:00:06 PM
hidden: true
---

{% assign exs = site.lista4 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
- use recursos dos módulos `scipy.linalg` à vontade

---

{% include exercicios.html exs=exs %}
