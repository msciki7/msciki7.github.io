---
title: "Digital Image Processing"
permalink: categories/Digital Image Processing
layout: archive # category
author_profile: true
sidebar:
  nav: "docs"
# types: posts
# taxononmy: Javascript
---

{% assign posts = site.categories['Digital Image Processing']%}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
