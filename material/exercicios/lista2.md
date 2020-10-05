---
title: Segunda Lista
parent: exs
nav_order: 2
mathjax: true
remove_trinket: true
timestamp: 10/5/2020, 11:15:02 AM
resolvidos: #['8']
---

{% assign exs = site.lista2 | sort: 'nav_order' %}

### Acesso rápido
{% for i in (1..exs.size) %}
  {%- assign v = i | downcase %}
  [Ex. {{i}}](#ex{{i}}){: .badge .badge-{% if page.entrega1 contains v %}warning{% elsif page.entrega2 contains v %}danger{% elsif page.resolvidos contains v %}success{% else %}primary{% endif %} }
{%- endfor %}

### Instruções
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
<!-- - os exercícios marcados em <span class="badge badge-warning">amarelo</span> devem ser entregues no dia 08/10/2020. -->
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice versa!

{% assign n = 0 %}

{% for ex in exs %}

{% assign n = n | plus: 1 %}

<div class="card mb-2">
    <a name="ex{{n}}"></a><h2 class="card-title alert alert-primary">Exercício {{n}}: {{ex.title}}</h2>
    <div class="card-body">
        <ul>
            <li><i><b>dificuldade:</b></i> {{ex.dificuldade}}%</li>
        </ul>

        {% if ex.content contains "<!-- more -->" %}
        {% assign conteudo = ex.content | split:"<!-- more -->"  %}
          {{conteudo[0]}}
        {% else %}
          {{ ex.content }}
        {% endif %}

        {%- assign ns = n | downcase %}
        {% if page.resolvidos contains ns %}

        <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="collapse" data-target="#{{ex.label}}" aria-expanded="false" aria-controls="{{ex.label}}">
          Solução
        </button>
        <div class="collapse" id="{{ex.label}}">
          <div class="card card-body">
            {{conteudo[1]}}
          </div>
        </div>

        {% endif %}

    </div>
</div>

{% endfor %}
