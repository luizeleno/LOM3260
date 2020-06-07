---
title: Terceira Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 07/06/20
---

### Acesso rápido
{% for i in (1..3) %}
{%- assign v = i | downcase %}
[Ex. {{i}}](#ex{{i}}){: .badge .badge-{% if page.entrega1 contains v %}warning{% elsif page.entrega2 contains v %}danger{% elsif page.resolvidos contains v %}success{% else %}primary{% endif %} }
{%- endfor %}

### Instruções
- use recursos dos módulos `scipy.linalg` à vontade

---

{% assign n = 0 %}

{% assign exs = site.lista3 | sort: 'nav_order' %}

{% for ex in exs %}

{% assign n = n | plus: 1 %}

<div class="card mb-2">
    <a name="ex{{n}}"></a><h2 class="card-title alert alert-primary">Exercício {{n}}: {{ex.title}}</h2>
    <div class="card-body">
        <ul>
            <li><i><b>dificuldade:</b></i> {{ex.dificuldade}}%</li>
            <!-- <li><i><b>utiliza:</b></i> {% include grade-exs.html tags=ex.tags %}</li> -->
        </ul>

        {{ex.content}}

    </div>
</div>

{% endfor %}

