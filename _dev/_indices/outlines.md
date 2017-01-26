---
title: Outlines
permalink: /outlines/
---
# Outlines
These are the notes I've prepared in advance of each class session. 
They may or may not reflect what actually happens in the session.
(See the [EBoards](../eboards/) for a record of what happened in class.)

{% assign outlines = site.outlines | sort: 'number' | reverse %}
{% for outline in outlines %}
  {% if outline.link %}
  {% assign num = outline.number %}
  {% assign index = num | plus: '-1' %}
  {% assign twodig = num | plus: '0' %}
  {% if twodig < 10 %}{% assign twodig = num | prepend: '0' %}{% endif %}
  * <a href="{{ site.baseurl }}/outlines/outline.{{ twodig }}.html">Outline {{ num }}: {{ site.data.classes[index].topic }}</a> {% if outline.held %}(held {{ outline.held | date: '%A, %-d %B %Y' }}){% endif %}
  {% endif %}
{% endfor %}
