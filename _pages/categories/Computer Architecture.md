---
title: "Computer Architecture"
permalink: categories/Computer Architecture
layout: archive # category
author_profile: true
sidebar:
  nav: "docs"
# types: posts
# taxononmy: Javascript
---

{% assign posts = site.categories['Computer Architecture']%}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
