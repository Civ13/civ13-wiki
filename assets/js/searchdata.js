---
layout: null
is_wiki_page: false
---
{% if site.search_engine == "js" %}
var jsondata=[
  {% for page in site.html_pages %}
   {
     {% assign title = page.title | default: page.name %}
     {% if title != nil %}
        "title"    : "{{ title | escape }}",
        "category" : "{{ page.category }}",
        "tags"     : "{{ page.tags | join: ', ' }}",
        "url"      : "{{ site.baseurl }}{{ page.url }}",
        "date"     : "{{ page.date }}",
        "content"  : {{ page.content | jsonify }}
     {% endif %}
   } {% unless forloop.last %},{% endunless %}
  {% endfor %}
];

var sjs = SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: jsondata,
    searchResultTemplate: '<a href="{url}" title="{desc}">{title}</a><br>',
    noResultsText: 'No results found',
    limit: 10,
    fuzzy: false,
    exclude: []
  })
{% endif %}

