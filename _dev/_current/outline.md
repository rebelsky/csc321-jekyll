---
title: Current Outline
permalink: /outlines/current.html
---
{% assign current = site.outlines | where: "current", true | first %}
{% if current %}
Current outline 
================
<script language="javascript">
  document.location = "{{ site.baseurl }}{{ current.url }}";
</script>
<p>
  Our current outline is 
  <a href="{{ site.baseurl }}{{ current.url }}">{{ current.title }}</a>.
</p>
{% else %}
No current outline
=================

For unknown reasons, there is not a current outline.  Contact SamR to
get this issue fixed.
{% endif %}
