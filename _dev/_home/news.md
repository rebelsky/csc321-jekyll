---
title: Class news
section: top-level
---
Class news
==========

*This information is copied from the daily outlines.*

{% assign dates = "" | split: "|" %}
{% for week_data in site.data.dates %}
  {% if week_data.days %}
    {% assign newdates = week_data.days | join: '|' %}
    {% assign dates = dates | join: '|' | append: '|' | append: newdates | split: '|' %}
  {% endif %}
{% endfor %}
{% assign prelim = site.prelim %}

{% assign numbers = (1..prelim.size) | reverse %}
{% for counter in numbers %}
  {% if counter < 10 %}
    {% capture num %}0{{ counter }}{% endcapture %}
  {% else %}
    {% capture num %}{{ counter }}{% endcapture %}
  {% endif %}
  {% capture filepath %}_prelim/prelim.{{ num }}.md{% endcapture %}
  {% assign info = site.prelim | where: "path", filepath | first %}
  {% if info %}
     {% if info.link %}
       {% assign held = dates[counter] %}
## Class {{ counter }} ({{ held | date: '%A, %-d %B %Y' }})

{{ info.content }}
<hr/>
     {% endif %}
  {% else %}
**Can't find daily preliminaries!**

counter: {{ counter }}

num: {{ num }}

info: {{ info }}

filepath: {{ filepath }}

<hr/>
  {% endif %}
{% endfor %}
