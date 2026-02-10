---
title: "data structure"
permalink: categories/data structure
layout: archive # category
author_profile: true
sidebar:
  nav: "docs"
# types: posts
# taxononmy: Javascript
---

{% assign posts = site.categories['data structure']%}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
