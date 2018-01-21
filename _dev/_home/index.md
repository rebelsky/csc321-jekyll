---
title: Software Design Principles and Practices
---
# {{ site.title }}

  <dl class="dl-horizontal">
    <dt>Instructor</dt>
    <dd>
      <a href="{{ site.data.info.instructor_homepage }}">{{ site.data.info.instructor }}</a>
    </dd>
  
    <dt>Meeting Times</dt>
    <dd>{{ site.data.info.meeting_times }}</dd>
  
    <dt>Office Hours</dt>
    <dd>{{ site.data.info.office_hours }}</dd>
    <dd>Book meeetings at <a href="https://rebelsky.youcanbook.me">https://rebelsky.youcanbook.me</a>.</dd>
    <dd>I also tend to follow an open door policy: Feel free to
      stop by when my door is open to to make an appointment for
      another time.</dd>

    <dt>Class Mentors</dt>
    <dd>
      <ul class="list-unstyled">
        {% for mentor in site.data.info.mentors %}
          <li>{{ mentor }}</li>
        {% endfor %}
      </ul>
    </dd>
  </dl>

## About this course

Welcome to the Spring 2018 section of Grinnell College's CSC 321,
*Software Design: Principles and Practices*.  In CSC 321, we build
your skills in software development to prepare you for projects
in CSC 322 and elsewhere.  The current model of the course focuses on
Web applications with the Sofware as a Service (SaaS) model using Agile
Development principles.  We will ground many of the ideas in the Ruby
on Rails framework.

Note that this is likely to be the last time that CSC 321 and CSC 322
are offered separately.  We plan to combine them into a single course
in the fall and add a second two-credit course for students returning
to software design.  *Do not take CSC 321 this semester without taking
CSC 322.*

Read more about the course in [the syllabus](../home/syllabus) and [the schedule](../home/schedule).
