---
title: Primeira Lista
parent: exs
nav_order: 1
mathjax: true
remove_trinket: true
# resolvidos: ['1', '2', '3', '4', '5', '6', '16', '20', '28', '10', '18', '17']
#resolvidos: ['1', '3', '4', '5', '6', '15', '16', '20', '28', '18', '27', '12', '13', '14']
#resolvidos: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '27', '28', '29']
#, '5', '6', '7', '8', '11', '12', '13', '15', '16', '20', '21', '22', '23', '26'] # retireo o 17 para a aula, depois voltar com ele!!!!!
#entrega1: ['9', '13', '14', '18', '19', '20']
#entrega2: ['30']
#entrega3: ['26']
timestamp: 10-04-2023 10:29
labels: true
---

{% assign exs = site.lista1 | sort: 'nav_order' %}

### Acesso rápido

{% include quick-access.html exs=exs %}

### Instruções

{%if page.resolvidos%}
- para os exercícios marcados em <span class="badge badge-success">verde</span>, uma possível solução é fornecida aqui, junto ao exercício.
{%endif-%}
<!-- - os exercícios marcados em <span class="badge badge-warning">amarelo</span> devem ser entregues no dia 08/10/2020. -->
<!-- - os exercícios marcados em <span class="badge badge-danger">vermelho</span> devem ser entregues no dia 05/11/2020. -->
<!-- - os exercícios marcados em <span class="badge badge-dark">preto</span> devem ser entregues em dupla no dia 03/12/2020. -->
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice versa!

{% include labels-ex.html %}

---

{% include exercicios.html exs=exs %}
