---
title: Software Design Principles and Practices
---
# {{ site.title }}

**Warning!  The class site is currently under development.  Expect things
to change significantly.**

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

