---
title: Buscar no site
id: search
nav_order: 100
permalink: /search/
icon: mag
timestamp: 21/08/20
---

Use o campo abaixo para encontrar mais rapidamente o que você procura
{: .lead }

<div class="input-group">
  <div class="input-group-prepend">
    <span class="input-group-text" id="Busca">{% octicon search %}</span>
  </div>
  <input type="text" class="form-control" placeholder="Busque no site..." aria-label="Search" aria-describedby="Busca" id="search-input">
</div>
<ul id="results-container" class="list-group"></ul>

<!-- Script pointing to search-script.js -->
<script src="{{site.baseurl}}/js/search-script.js" type="text/javascript"></script>

<!-- Configuration -->
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: '{{site.baseurl}}/search/search.json',
  searchResultTemplate: '<li class="list-group-item"><a href="{url}">{title}</a></li>'
})
</script>

---

O mecanismo de busca acima foi inspirado por [este post]{: target="\_blank"}.

[este post]: https://cri.dev/posts/2017-02-05-Use-Simple-Jekyll-Search-on-your-blog-in-these-easy-steps/
