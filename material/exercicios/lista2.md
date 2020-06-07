---
title: Segunda Lista
parent: exs
mathjax: true
remove_trinket: true
timestamp: 07/06/20
---

### Acesso rápido
{% for i in (1..5) %}
{%- assign v = i | downcase %}
[Ex. {{i}}](#ex{{i}}){: .badge .badge-{% if page.entrega1 contains v %}warning{% elsif page.entrega2 contains v %}danger{% elsif page.resolvidos contains v %}success{% else %}primary{% endif %} }
{%- endfor %}

### Instruções
- Os exercícios 1 a 5 devem ser entregues em dupla no [Google Classroom](https://classroom.google.com){: target="\_blank"} até as 14h00 do dia 21/11/2019. 
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis &mdash; e vice-versa!
- Seja paciente. Se começar a encontrar muitas dificuldades, mude para outro problema e volte para o anterior depois de uma boa pausa, com a cabeça fresca.
- use recursos dos módulos `scipy.optimize` e `scipy.integrate` à vontade, exceto quanto explicitamente indicado o contrário.

---

{% assign n = 0 %}

{% assign exs = site.lista2 | sort: 'nav_order' %}

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

