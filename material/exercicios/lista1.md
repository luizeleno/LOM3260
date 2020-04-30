---
title: Primeira Lista
parent: exs
nav_order: 1
mathjax: true
remove_trinket: true
resolvidos: ['1', '5', '6', '7', '8', '11', '12', '13', '15', '16', '20', '21', '22', '23', '26']
entrega1: ['2', '3', '4', '9', '14', '17', '19', '28']
entrega2: ['18', '29', '30']
---

### Acesso rápido
{% for i in (1..30) %}
{%- assign v = i | downcase %}
[Ex. {{i}}](#ex{{i}}){: .badge .badge-{% if page.entrega1 contains v %}warning{% elsif page.entrega2 contains v %}danger{% elsif page.resolvidos contains v %}success{% else %}primary{% endif %} }
{%- endfor %}

### Instruções
- **Os exercícios marcados em <span class="badge badge-warning">amarelo</span> na lista acima (Acesso rápido) devem ser entregues em dupla no [Google Classroom](https://classroom.google.com){: target="\_blank"} até as 14h00 do dia 12/09/2019. São os exercícios {% for i in page.entrega1 %}{{i}}{% unless forloop.last %}, {%endunless%}{% endfor %}.**
- **Os exercícios marcados em <span class="badge badge-danger">vermelho</span> na lista acima (Acesso rápido) devem ser entregues em dupla no [Google Classroom](https://classroom.google.com){: target="\_blank"} até as 14h00 do dia 24/10/2019. São os exercícios {% for i in page.entrega2 %}{{i}}{% unless forloop.last %}, {%endunless%}{% endfor %}.**
- os exercícios marcados em <span class="badge badge-success">verde</span> foram resolvidos em sala de aula. Uma possível solução é fornecida aqui, junto ao exercício.
- as porcentagens no começo de cada exercício são uma maneira de indicar o seu grau de dificuldade. Mas não se apegue muito a esses valores: talvez você ache fáceis alguns que eu julgo como difíceis --- e vice-versa!
- Seja paciente. Se começar a encontrar muitas dificuldades, mude para outro problema e volte para o anterior depois de uma boa pausa, com a cabeça fresca.
- Nos exercícios envolvendo *strings*, suponha que ela só contenha caracteres da [Tabela ASCII](https://pt.wikipedia.org/wiki/ASCII){: target="\_blank"} de 32 em diante. Caracteres com acentos não fazem parte do código ASCII. Hoje em dia usa-se quase sempre a codificação *unicode*, mais completa que a ASCII, com a vantagem de manter os mesmos códigos para os caracteres comuns a ambos. Portanto, para simplificar a sua vida, nos exercícios com strings suponha que o usuário sempre fornece caracteres sem nenhum acento.

{% include labels-ex.html %}

---

{% assign n = 0 %}

{% assign exs = site.lista1 | sort: 'nav_order' %}

{% for ex in exs %}

{% assign n = n | plus: 1 %}

<div class="card mb-2">
    <a name="ex{{n}}"></a><h2 class="card-title alert alert-primary">Exercício {{n}}: {{ex.title}}</h2>
    <div class="card-body">
        <ul>
            <li><i><b>dificuldade:</b></i> {{ex.dificuldade}}%</li>
            <li><i><b>utiliza:</b></i> {% include grade-exs.html tags=ex.tags %}</li>
        </ul>

        {{ex.content}}

    </div>
</div>

{% endfor %}
