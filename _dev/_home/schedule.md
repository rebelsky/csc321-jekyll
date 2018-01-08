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
[Week 7](#week07) 
<a name="schedule"></a>

<table class="table table-condensed table-responsive text-center">
  <tbody style="vertical-align: middle">
    {% assign daynum = 0 %}
    {% for week_data in site.data.dates %}
      {% if week_data.days %}
        <tr class="week-header">
          <td colspan="9"><a name="{{ week_data.anchor }}"></a>{{ week_data.week }}</td>
        </tr>
        <tr class="column-header">
          <td class="hidden-xs">#</td>
          <td class="hidden-xs">Day</td>
          <td>Date</td>
          <td colspan="4">Topic</td>
          <td colspan="2">Work Due</td>
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
            <td halign="left" colspan="4">
                    <a href="{{ site.baseurl }}/outlines/outline.{{ twodig }}.html">
                    <strong>{{ class.topic | markdownify | remove: '<p>' | remove: '</p>' }}</strong>
                    </a>
                {% if class.notes %}<li><a href="{{ class.notes }}">(notes)</a></li>{% endif %}
                <br>
                  <em>{{ class.summary | markdownify | remove: '<p>' | remove: '</p>' }}</em>
            </td>
            <td class="text-nowrap">
              {% assign work_due = site.documents | where: "schedule", day %}
              {% include schedule_items.html items=work_due show-due-time=true show-subtitle=true %}
            </td>
          </tr>
          {% assign daynum = daynum | plus: 1 %}
        {% endfor %}
      {% else %}
        <tr class="week-header">
          <td colspan="9">{{ week_data.week }}</td>
        </tr>
        <tr>
          <td colspan="9"></td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
