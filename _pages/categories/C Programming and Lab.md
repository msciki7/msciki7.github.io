---
title: "C Programming and Lab"
permalink: categories/C Programming and Lab
layout: archive # category
author_profile: true
sidebar:
  nav: "docs"
# types: posts
# taxononmy: Javascript
---

{% assign posts = site.categories['C Programming and Lab']%}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
