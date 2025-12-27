---
title: "SISC-Web"
permalink: categories/SISC-Web
layout: archive # category
author_profile: true
sidebar:
  nav: "docs"
# types: posts
# taxononmy: Javascript
---

{% assign posts = site.categories['SISC-Web']%}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
