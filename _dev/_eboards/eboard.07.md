---
title: Eboard 07  An introduction to software engineering
number: 7
section: eboards
held: 2017-02-06
---
CSC 321.01, Class 07:  An introduction to software engineering
==============================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Model/View/Controller frameworks
* RESTful programming
* Models of software engineering
* Important agile practices
* Why agile?
* Why not agile?

### News / Etc.

* Why are students missing?  Bad students!  No coffee.

### Upcoming work

* [SaaSbook, sections 7.1-7.5]({{ site.baseurl }}/readings/user-stories).
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.08).

### Good things to do

*Nope, no extra credit.*

* CS Table, Tuesday, 7 Feb 2017.  Something on privacy.
* Scholars Convocation, Thursday, 9 Feb 2017, 11:00 a.m., JRC 101.
  David Orr: *Climate Change and the Crisis of American Democracy*.
* Thursday extras, Thursday, 9 Feb 2017, 4:15 p.m., Science 3821: Something on
  computer graphics (visitor from UMN).

### Questions

Model/View/Controller frameworks
--------------------------------

* Software designers have tried to develop/document standard "designs"
  that work well for many situations.
* Model/view/controller is one of the most successful designs; 
  modularizes many traditional interactive programs into three
  separate modules with a somewaht standand interface between them.
    * Modularization helps us isolate errors.
    * Can help with DRYness
    * May help with reusability.
    * Makes it easier to segment the work.
    * We can use different views with the same model
* Model: Describes the data
* Controller: Describes changes to the data
* View: Shows the data
* In Rails, when you say "I'm working with this kind of data", you'll get
  a model, a view (.erb), and a controller.

RESTful programming
-------------------

* Modern Web: Applications get data from everywhere.
* Old Internet: Everyone had their own protocol for how to request
  and format data.
* People started developing common ways to request data.
* REST leverages existing Web formats, protocols, and ports to simplify
  the request and transmission of data.
* REST uses http as the primary protocol.  So we can send
   * `GET` + URL + data
   * `POST`+ URL + data
   * `DELETE`+ URL + data
* REST tends to use four formats for returning values
   * JSON - A Javascript format for representing objects.
   * XML - Generalized markup language
   * CSV - comma-separated values
   * TXT - anything goes
* REST is supposed to be stateless.
   * Makes it easier to shift requests around; can be somewhat harder
     for the server to implement.
* REST is a series of practices/expectations layered on top of HTTP.
* A lot of the work for REST is available through libraries or toolkits.
* Keeping track of state is perhaps the hardest thing that sometimes ha
  to be customized.
* HTTP transactions are not encrypted.  Anyone looking at the packets can
  figure out what is being sent.
    * Hypertext transfer protocol
* HTTPS is a moderately well encrypted format.  The NSA can tell what is
  being sent, because they undermined the protocol, but most people cannot.
    * Hypertext transfer protocol, supposedly secure
* Protocol is a series of rules that govern a transaction.

Models of software engineering
------------------------------

Three models of software engineering

* Plan and document
   * Waterfall - everything flows downhill
   * Spiral
* Agile

*Talk to your neighbor: Similarities, differences.*

* All of these methodologies have a similar sequence of steps
   * Gather requirements from clients
   * Verify requirements
   * Design architecture
   * Implement
   * Test
   * Release
   * Maintain
* However, they have very different numbers of iterations and iteration
  lengths
   * Waterfall - One iteration, often multiple years
   * Spiral - Multiple iterations (usually about four), a few months
   * Agile - As many iterations as necessary, one or two weeks
* Different models of specifying requirements
   * More formal for waterfall
   * Less formal for agile
* Agile is used a lot these days 

Important agile practices
-------------------------

Agile is a group of practices that work together to help ensure that we
build good software while using the "short iterations" model.

*What do you see as the most important agile practices?*

* Use customer stories as documentation / tasks / issues.
    * Helps us ensure that we are building the product our users want,
      rather than the product we think our users want (or that our
      pointy-haired bosses think our users want)
* Focus on the task at hand, rather than a long-term picture.
    * History suggests that what users think they want at the beginning
      of the project is not what they realize they want at the end.
    * History suggests that program designs that sound good at the 
      beginning may not be so good at the end.
    * User stories *are* the tasks at hand.
* Frequent iterations, with prototypes.
    * "Sprint" == "Iteration" == "..."
    * Not all features available.
    * Lets user see what's done, think about what's important
    * Helps build user stories
* Test-driven design
    * Makes it easier to add or change code and tell whether you've 
      broken something
    * Documents requirements
* Smaller teams
    * Easier to collaborate
    * Perhaps less need for documentation
    * Supports communication
    * Enable frequent meetings
* Frequent meetings
    * With team - keeps you on track
    * With client - keeps you on track
* Pair programming
    * Make friends
    * Catches errors more quickly
    * Evidence suggests that pairs are more productive: More code,
      fewer bugs.
    * Share knowledge, practices, etc.
    * Provides continuous code review
* Track velocity
    * Know how much you are producing
    * Know how much you can produce
    * Helps plan each cycle
    * Helps with communications with client
* Start simple
    * Don't waste too much time on something that may be thrown away
    * Lets you get prototypes out more quickly
* Ruthlessly refactor
    * Rewrite bad code when it crops up.

Why agile?
----------

Why do our authors (and others) promote agile approaches?

Why not agile?
--------------

Why might critics not like agile approaches?

