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

Welcome to the Fall 2017 section of Grinnell College's CSC 321,
*Software Design: Principles and Practices*.  In CSC 321, we build
your skills in software development to prepare you for projects
in CSC 322 and elsewhere.  The current model of the course focuses on
Web applications with the Sofware as a Service (SaaS) model using Agile
Development principles.  We will ground many of the ideas in the Ruby
on Rails framework.

Catalog Description
-------------------

> Provides a foundation for "programming in the large" and developing
high-quality software that meets human needs. Introduces the software
lifecycle, agile development methods, professional tools, and software
design principles. Includes hands-on laboratory work.

Class Format
------------

This course is being offered in a non-traditional format.  We will be
relying on a MOOC and SPOC as part of the core "textbooks" for the course.
We can then spend class time more on discussion and problem-solving based
on the readings and videos from the MOOC/SPOC.  (Some people would call
this a "flipped classroom.")

This is also a course in which you should be developing professional
skills and habits.  Hence, some of the work in the class will require
you to do exploration on your own.  The College would probably call
this an opportunity to "learn how to learn".  When you are stuck, I
recommend that you follow the strategy of [you must try, and then you must
ask](https://blogs.akamai.com/2013/10/you-must-try-and-then-you-must-ask.html).

The course meets three days per week for the first seven weeks of the semester.
You are expected to do about twelve hours of work outside of class each 
week (and you may timebox that work).

Learning Goals
--------------

By the end of this course,  you should be able to

* apply agile software development methodology, tools, and practices 
  in real-world team projects;
* contrast agile software development methodology with plan-and-document 
  methodologies;
* build SaaS applications with the Ruby on Rails framework; and
* apply techniques for understanding and modifying legacy code.

Important Warnings
------------------

*Warning!* The Berkeley CS 169 course that forms the underpinnings of
this course keeps changing.

*Warning!* I continue to use Web tools that with which I am not completely
familiar (e.g., edX, Jekyll).  When things look wrong on this site or
the edX site, please notify me ASAP.

*Warning!* Some students prefer readings.  Some prefer videos.  
You should try both.

Grading
-------

*These policies are likely to change.
may change.*

* __Class participation__: 20%.  Much of class time is in discussion.  
  I will evaluate you on the quality of your contributions.
* __Journal__: 40%.  Following the lead of Dr. Davis and Prof. Weinman, I
  ask you to do a journal assignment after each reading, video, and/or
  tutorial.  Journals are generally due at 8:00 p.m. on the night before
  class to give me time to reflect on them before class.
* __Homework__: 30%.  These are timeboxed.  If you spend the required
  time and document your efforts, you will get a minimum of 90% on
  a homework assignment.  Homeworks will be due every few days.
* __Project__: 10%.  Toward the end of the period, I will ask you
  to develop a small project.

Workload
--------

Here's what I expect you'll be spending your time on each week

* Class time (3 hours)
* Readings/videos (4 hours)
* Journaling (2 hours)
* Programming and writing assignments (4 hours)

The first week may be a bit busier as you get set up.

Communication
-------------

Dr. Davis created a Slack team for general discussion of CSC
321/2.  Join it here: <https://grinnell-sw.slack.com/>.  There is a
`#homework` channel for discussion of homework assignments!

Development
-----------

The course designers recommend that we do
development on Cloud 9.  Instructions are at
<https://github.com/saasbook/courseware/wiki/Setting-up-Cloud9>.

Books and Other Readings
------------------------

[The CSC 321 Course Web](index.html)

> The hypertext that you are currently reading.  Right now, it looks like
it will primarily contain my notes for each class (outlines) and my record
of each class (eboards), but we'll see.

Fox, Armando and Patterson, David (2016). _Engineering Software as a
Service: An Agile Approach Using Cloud Computing_, latest edition.

> Our core textbook.  Fox and Patterson synthesized a lot of ideas
to produce a textbook that grounds software engineering principles in
a new model of computing.  This textbook is rapidly evolving.
I would recommend that you purchase the Kindle edition through Amazon,
particularly since they are updating the textbook again this semester.
(With the Kindle Cloud Reader, available at <https://read.amazon.com/>
or an appropriate app, you should be able to read the book on any
electronic device.)

Hartl, Michael (2016).  _Ruby on Rails Tutorial_ (4th Edition).  Addison-Wesley.

> The book we'll be using to learn Rails.  Available online at
  <https://www.railstutorial.org/book>

Fox, Armando and Patterson, David (2016).  BerkeleyX: CS169.1x Agile Development Using Ruby on Rails - The Basics.  Available online at 
<https://courses.edx.org/courses/course-v1%3ABerkeleyX%2BCS169.1x%2B3T2015SP/info>

> The underlying MOOC.  You can use this MOOC for videos that correspond
to the various readings.  There are also many other resources available
on the MOOC.  I've reorganized the material for our SPOC, which is available online at <https://edge.edx.org/courses/course-v1:Grinnell_College+CS321-1-S17+2017_Spring/>.

Citations
---------

Many parts of this overview, as well as the overall design of the course, are
due to Janet Davis.  I have reused materials with her permission.

The various tools and files used to build this site are adapted from
Charlie Curtsinger's courses.
