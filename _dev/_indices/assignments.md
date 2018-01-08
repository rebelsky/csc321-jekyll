---
title: Assignments
permalink: /assignments/
---
# Assignments
We will have assignments almost every day of the semester. You can feel
free to work on assignments alone or to collaborate on any part of an
assignment.  However, reading journals should be submitted individually.

<dl>
  {% assign assignments = site.assignments | sort: 'due' %}
  {% for assignment in assignments %}
    {% if assignment.link %}
      {% if assignment.due %}
        <dt>{% include schedule_item.html item=assignment show-due-time=false show-subtitle=true %}</dt>
        <dd>
          <ul class="list-inline">
            {% if assignment.assigned %}
              <li>Assigned {{ assignment.assigned | date: '%-d %B %Y' }}</li>
            {% endif %}
            {% if assignment.due %}
              <li>Due {{ assignment.due | date: '%-d %B %Y' }}{% if assignment.due-time %} <i>(before {{ assignment.due-time | split: ' ' | first }})</i>{% endif %}</li>
            {% endif %}
          </ul>
        </dd>
      {% endif %}
    {% endif %}
  {% endfor %}
</dl>
