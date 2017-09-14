---
title: Eboard 04  Getting started with Rails
number: 04
section: eboards
held: 2017-09-05
---
CSC 321.01, Class 04:  Getting started with Rails
=================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Model/View/Controller
* An introduction to Rails
* Guest lecture: Design

### News / Etc.

* Today we start on Rails.
* We will be exploring Rails all of this week and some of next week.
  (I think we need more time than I had originally planned.)
* We will have a visitor for the second half of class today.
  Shu-Yang Lin, <http://shuyanglin.com/>.  She will discuss design
  issues and more.
* I'm still working on the course Web site.

### Upcoming Work

* Read [SaasBook, Chapter 2](../readings/saasbook2) (Thursday)
* Do [The introduction to Rails from SaasBook](https://github.com/saasbook/hw-rails-intro) (starts in class Thursday; continues through next week)

### Good things to do

#### Academic

* Rosenfield symposium, this week.  (Lots of different events)

#### Peer

* ???

### Questions

Model-View-Controller and other acronyms
----------------------------------------

A decent amount of the kind of software we are developing follows
the ``Model-View-Controller'', or just ``MVC'' pattern.  As the name
suggests, the model encourages you to segment your program into three
big pieces.

* Model: What your data look like.  (Plus the code that lets you 
  access and update the data.)
    * Good thing: Use an appropriate kind of database management system.
    * Traditionally, DBMS's are relational; they store tables and
      relationships between tables
    * Example: 
        * Table of students ("relation"): ID, surname, forename,
          preferred name, ...
        * Table of courses: ID, department, section, semester, title,
          instructor
        * Some mechanism for describing how it can be that a student
          has many courses and a course has many students
    * Increasingly, programmers are finding it useful to think of
      less structured databases and just think about a database as a
      store of objects
    * Rails provides a natural way to describe models as objects
      and to tie those automatically to an underlying database.
* View: What we present to the user
    * Different situations may require different views
    * Distinguish based on role of viewer
    * Distinguish based on user prefs
    * Distinguish based on platform capabilities
    * Some default views
    * HAML, HTML, etc. for doing markup
* Controller: Where the real work happens
    * The program logic.
    * Write it in Ruby

What do users normally do with data on an MVC application: CRUD
   * Create
   * Reading data
   * Update
   * Delete

Challenge for Web applications: How do we convey CRUD to the user?
   * The Web was designed as stateless: Clients request URLs, servers
     return data associated with that URL
   * But interactive programs often require state/context/etc.  E.g.,
     who is this user?
   * One form of state: Cookies.  An agreement between browser and server
     that (a) the server can send information to the browser; (b) the
     browser stores that information; (c) the next time the browser
     visits the server, it sends that information along with the page
     request.
   * Another form of state: Encoded in URLs
     `http://www.anaconda.com/books/walker2017`
     `http://www.anaconda.com/books/walker2017?customer=samr`
   * A number of mechanisms for encoding additional information, such as
     type of request, in the URL have been developed.  Rails uses
     REST - a custom for what URLs look like (and little more)
     "REST" = REpresentational State Transfer

One more important acronym you've probably seen: DRY
    * Don't Repeat Yourself: The idea that you shouldn't have the same
      data in two places or the same code in two places.
    * Look for strategies and approaches to ensure that you don't 
      repeat code and data.

An introduction to Rails
------------------------

Tool to support the quick building and deployment of MVC Web sites.
Application of the DRY principle to Web site design: Once we know
what goes into a Web site, just generate the common code and structure
and ....

When you build a Rails Web site, at least in the abstract, you provide
it with a list of data types you're using and it magically sets up
the model and view and a template for the controller.

Questions and Answers
---------------------

### Big picture and such

Agh!  The chapter is a big mess.
  : I agree that it's not necessarily straightforward.  I should have
    had you read chapter 2 first.
  : You will best understand code by trying it.
  : And then trying variants.
  : Problem: Rails and Ruby are quickly moving targets
  : Problem: Lots of assumptions about what else is in the application
    and where

What is MVC?
  : See above

How do you set up a Rails app?
  : Thursday

Are there "cheat sheets" for Rails conventions?
  : There may be, but I haven't found them.  We should check with the
    alums.
  : The official Rails documentation helps; it's more that it walks
    you through everything.  And there's always Ctrl-F, which stands
    for "Find"
  : Sam will check in with alums

### Medium picture

Please explain route mapping
  : Given a URL, do the following code
    `http://www.csc321.org/course/csc321/homework/submit`
  : Ideally, the routes are patterns
    `http://www.csc321.org/course/ID/homework/submit` =>
    submit(ID,...)
  : Provide information for code through URLs.
  : An embodiement of RESTful URLs

Please explain RESTful URLs
  : See above

What is CRUD?
  : See above

What is DRY?
  : See above
  : That answer was DRY

What is database migration and why do we have it?
  : We are agile developers, at least in this course.
  : Agile development suggests that you don't try to design the whole
    application in advance.  You essentially build a feature or two at
    a time.
  : Agile development means that things change.  They sometimes change
    a lot.
  : One of the things that will change is your model.  You might add 
    fields to an existing object.  You might add new objects.
  : Other people may also have copies of your application, possibly
    with different data.
  : We need a way to describe the change to the model.
  : Database migration!
  : YOu can describe what changes you are making to your data model.
  : Others can then run those changes
  : You can back out of those changes

### Small picture

Does Rails really isolate you from SQL?
  : Yes
  : That's both good and bad.

Starting Rails
--------------

https://github.com/saasbook/hw-rails-intro

Guest lecture: Design and beyond
--------------------------------

Welcome to Shu-Yang Lin, <http://shuyanglin.com/>

* Working for the Taiwanese goverment as a startup incubator.
* Empower government employees to think about ways to better serve
  their communities.
* A bit of a "nomad designer"
* Her experience was a bit of chaos.  As a fresh graduate, explored various
  aspects of her career path.
* Decided that working for government was a way to make a bigger difference
  in the world.
* Important to understand the context of your country.
* How do we open government.
* Democracy is people working together to make decisions.
* Working with a civic hacker - Digital minister of Taiwan
* Hacking the government in positively.  
* Shadow Web sites, .g0v

Questions

How did you get to this state?
  : Started by people having ideas and pitching those ideas.  
  : A bit of a "hack-a-thon" atmosphere.  
  : Need to make prototypes to show people what you are doing.

Collaboration vs. Cooperation
  : Cooperation is to work with someone once you know them.
  : Collaboration you work with people before you really know them - E.g.,
    working on a git project without knowing who else is working on it.
  : Trying to get that culture into the department.

Sample project
  : "We are trying to reinvent democracy."
  : Democracy is all about people coming together and sharing ideas.
  : Currently: Elected officials represent us.
  : Future: More direct representation.  For example, you can assign
    your right to vote on an environmental issue to someone else who
    knows more about it.
  : One project is to help people form consensus.
  : PCA - Principle component analysis
  : Each comment is a datum, divide it into parts
  : Example: How do we regulate Uber in Taiwan?  View of drivers.
    View of government officials.
  : The VTaiwan platform ended up being useful
  : Example: <https://vtaiwan.tw/topic/uberx>
  : Importance of consensus vs. vote/rule of the majority
  : But consensus takes time and effort
  : We know democracy doesn't work now; what are the ways in which technology
    can help restore democracy?
  : But what happens if you empower a machine too much?  It's not likely
    to happen yet, as long as we realize that we still need human
    input.  
  : Example of voice recognition: You probably want someone to post-process
    what the voice recognition software generates.
  : We do better if we can combine capabilities of computing and capabilities
    of humans.
  : Should we worry about the singularity?  We are here in it now.  Let's
    make the best of it.  (And then type really fast.)

Q: What platform do folks use for vTaiwan?
  : Built with third-party <https://pol.is>

What authentication do you rely upon?
  : People do try to hack it.
  : But, in the end, it doesn't make that much difference because you see the main players anyway.  In the Uber situation, you could see Taxi Drivers, Uber Drivers, Government officials, and ...

What informed the process of creating the platform?
  : Try it for Thursday's talk: <https://pol.is/2ouf>.

How do you keep track of who is different if it's anonymous?
  : We are looking at voting patterns.
  : So we look at group formation.

How does the clustering work?
  : We have a bunch of people and they vote for each comment.
  : There are four options: Agree, Disagree, Haven't voted.  Encode as
    numbers like 1, -1, 0.
  : Treat these as vectors in N space.
  : We can compute the distance between any two people.  A group is a
    bunch of people who are nearby in N space.
  : We then project onto a two-dimensional space using the two axes that
    divide most between the groups.

How do these technical people make a positive difference in democracy?
  : Hack it.
  : **Teach other people about how to use technology.**
  : Think about an issue that you are passionate about (e.g., animal
    rights, global warming, etc.)
  : Dedicate your skills to one of those things.
  : Use that powerful skill that is in your hands.
  : Or just work for a big company like Google or Amazon or Microsoft
    and use your spare time to make a difference.
  : Be involved.
  : Do things with open data, promote open data.
  : Build programs that help others better understand the situation.
  : Code for America
  : 18F - Government Digital Services
