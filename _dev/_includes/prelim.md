{% assign counter = include.counter %}
{% if counter < 10 %}
{% capture num %}0{{ counter }}{% endcapture %}
{% else %}
{% capture num %}{{ counter }}{% endcapture %}
{% endif %}
{% capture filepath %}_prelim/prelim.{{ num }}.md{% endcapture %}
{% assign info = site.prelim | where: "path", filepath | first %}
{% if info %}

{{ info.content }}

{% else %}

**Can't find daily preliminaries!**

counter: {{ counter }}

num: {{ num }}

info: {{ info }}

filepath: {{ filepath }}

{% endif %}
