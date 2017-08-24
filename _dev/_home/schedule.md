---
title: Schedule
permalink: /schedule/
---
<h1>Schedule</h1>
<table class="table table-condensed table-responsive text-center">
  <tbody style="vertical-align: middle">
    {% assign daynum = 0 %}
    {% for week_data in site.data.dates %}
      {% if week_data.days %}
        <tr class="week-header">
          <td colspan="6">{{ week_data.week }}</td>
        </tr>
        <tr class="column-header">
          <td class="hidden-xs">Day</td>
          <td>Date</td>
          <td>Topic</td>
          <td>Reading</td>
          <td>Lab</td>
          <td>Work Due</td>
        </tr>
        {% for day in week_data.days %}
          {% assign class = site.data.classes[daynum] %}
          <tr>
            <td class="hidden-xs">{{ day | date: "%A" | remove: "onday" | remove: "uesday" | remove: "ednesday" | remove: "ursday" | remove: "riday" }}</td>
            <td>{{ day | date: "%-m/%-d" }}</td>
            <td>
              <ul class="list-unstyled">
                {% assign twodig = daynum | plus: '1' %}
                {% if twodig < 10 %}{% assign twodig = twodig | prepend: 0 %}{% endif %}
                <a href="{{ site.baseurl }}/outlines/outline.{{ twodig }}.html">
                {% for topic in class.topic %}
                  <li>
                    {{ topic | markdownify | remove: '<p>' | remove: '</p>' }}
                  </li>
                {% endfor %}
                </a>
                {% if class.notes %}<li><a href="{{ class.notes }}">(notes)</a></li>{% endif %}
              </ul>
            </td>
            <td>
              <ul class="list-unstyled">
                {% if class.reading %}
                  {% for item in class.reading %}
                    {% assign reading = site.documents | where: "url", item | first %}
                    {% if reading %}
                      <li>{% include schedule_item.html item=reading show-due-time=false %}</li>
                    {% else %}
                      <li>{{ item | markdownify | remove: '<p>' | remove: '</p>' }}</li>
                    {% endif %}
                  {% endfor %}
                {% elsif class.read %}
                  {% for item in class.read %}
                    <li>{{ item | markdownify | remove: '<p>' | remove: '</p>' }}</li>
                  {% endfor %}
                {% else %}
                  <li><i>No reading</i></li>
                {% endif %}
              </ul>
            </td>
            <td>
              <ul class="list-unstyled">
                {% if class.lab %}
                  {% for item in class.lab %}
                    {% assign lab = site.documents | where: "url", item | first %}
                    {% if lab %}
                      <li>{% include schedule_item.html item=lab show-due-time=false %}</li>
                    {% else %}
                      <li>{{ item | markdownify | remove: '<p>' | remove: '</p>' }}</li>
                    {% endif %}
                  {% endfor %}
                {% else %}
                  <li><i>No lab</i></li>
                {% endif %}
              </ul>
            </td>
            <td class="text-nowrap">
              {% assign work_due = site.documents | where: "due", day %}
              {% include schedule_items.html items=work_due show-due-time=true %}
            </td>
          </tr>
          {% assign daynum = daynum | plus: 1 %}
        {% endfor %}
      {% else %}
        <tr class="active">
          <td colspan="6">{{ week_data.week }}</td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
