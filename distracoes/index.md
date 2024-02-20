---
layout: page
title: Distrações
---
Essa é uma página das atividades ou distrações para quando não estou escrevendo. Pensei em colocar as leituras aqui também, mas achei melhor dedicar um espaço especial para elas.

## Fotografias

{% for fotografia in site.fotografias %}
* [{{fotografia.title}}]({{fotografia.url}})
{% endfor %}

## Pinturas

{% for pintura in site.pinturas %}
* [{{pintura.title}}]({{pintura.url}})
{% endfor %}
