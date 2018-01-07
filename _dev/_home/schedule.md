---
title: Schedule
section: home
---
# {{ page.title }}

**Warning!  This schedule, like much of the course, is under development
and may change significantly.**

<a href="#schedule" class="sr-only sr-only-focusable">Skip to schedule</a>
[Week 1](#week01) |
[Week 2](#week02) |
[Week 3](#week03) |
[Week 4](#week04) |
[Week 5](#week05) |
[Week 6](#week06) |
[Week 7](#week07) |
[Week 8](#week08) |
[Week 9](#week09) |
[Week 10](#week10) |
[Week 11](#week11) |
[Week 12](#week12) |
[Week 13](#week13) |
[Week 14](#week14)
<a name="schedule"></a>
>>>>>>> b0731697e0c8061b8e2ceec411fea6f8e31ab19d

<table class="table table-condensed table-responsive text-center">
  <tbody style="vertical-align: middle">
    {% assign daynum = 0 %}
    {% for week_data in site.data.dates %}
      {% if week_data.days %}
        <tr class="week-header">
          <td colspan="8"><a name="{{ week_data.anchor }}"></a>{{ week_data.week }}</td>
        </tr>
        <tr class="column-header">
          <td class="hidden-xs">#</td>
          <td class="hidden-xs">Day</td>
          <td>Date</td>
          <td colspan="2">Topic</td>
          <td>Reading(s)</td>
          <td>Lab</td>
          <td>Work Due</td>
        </tr>
        {% for day in week_data.days %}
          {% assign class = site.data.classes[daynum] %}
          {% assign classnum = daynum | plus: '1' %}
          {% assign twodig = classnum %}
          {% if twodig < 10 %}{% assign twodig = twodig | prepend: 0 %}{% endif %}
          <tr>
            <td class="hidden-xs">{{ classnum }}</td>
            <td class="hidden-xs">{{ day | date: "%A" | remove: "onday" | remove: "uesday" | remove: "ednesday" | remove: "ursday" | remove: "riday" }}</td>
            <td>{{ day | date: "%-m/%-d" }}</td>
            <td halign="left" colspan="2">
                    <a href="{{ site.baseurl }}/outlines/outline.{{ twodig }}.html">
                    <strong>{{ class.topic | markdownify | remove: '<p>' | remove: '</p>' }}</strong>
                    </a>
                {% if class.notes %}<li><a href="{{ class.notes }}">(notes)</a></li>{% endif %}
                <br>
                  <em>{{ class.summary | markdownify | remove: '<p>' | remove: '</p>' }}</em>
            </td>
            <td>
              {% if class.reading %}
                <ul>
                  {% for item in class.reading %}
                    {% assign itemlong = item | append: ".html" | replace: ".html.html", ".html" %}
                    {% assign reading = site.documents | where: "url", itemlong | first %}
                    {% if reading %}
                      <li>{% include schedule_item.html item=reading show-due-time=false %}</li>
                    {% else %}
                      <li>{{ item | markdownify | remove: '<p>' | remove: '</p>' }}</li>
                    {% endif %}
                  {% endfor %}
                </ul>
              {% else %}
                <i>No reading</i>
              {% endif %}
            </td>
            <td>
              {% if class.lab %}
                <ul>
                  {% for item in class.lab %}
                    {% assign itemlong = item | append: ".html" | replace: ".html.html", ".html" %}
                    {% assign lab = site.documents | where: "url", itemlong | first %}
                    {% if lab %}
                      <li>{% include schedule_item.html item=lab show-due-time=false %}</li>
                    {% else %}
                      <li>{{ item | markdownify | remove: '<p>' | remove: '</p>' }}</li>
                    {% endif %}
                  {% endfor %}
                </ul>
              {% else %}
               <i>No lab</i>
              {% endif %}
            </td>
            <td class="text-nowrap">
              {% assign work_due = site.documents | where: "due", day %}
              {% include schedule_items.html items=work_due show-due-time=true %}
            </td>
          </tr>
          {% assign daynum = daynum | plus: 1 %}
        {% endfor %}
      {% else %}
        <tr class="week-header">
          <td colspan="8">{{ week_data.week }}</td>
        </tr>
        <tr>
          <td colspan="8"></td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
