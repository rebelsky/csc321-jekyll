---
title: Eboard 09  User stories
number: 9
section: eboards
held: 2018-02-09
link: true
current: true
---
CSC 321.01, Class 09:  User stories
===================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Good things to do
    * Questions
* User stories
* Format of user stories
* Assessing user stories
* Some examples
* User stories in testing (aka behavior-driven design)
* User stories in planning

Preliminaries
-------------

### News and notes

* Alumni mentors visit next Wednesday.  Please try to clear lunch time,
  4pm for their talk, (and 1pm, if possible).
* I have not yet had time to rearrange the schedule.  I'm currently trying
  to figure out when my first free moment will be.
* From your mentor: Please remind the 321 students that I will have a
  mentor session from 7-8 on Sunday and another one from 6-8 on Thursday
  but no session for 321 on Tuesday.

### Upcoming work

* [Hartl 5](../assignments/hartl-5) due **Tuesday** at 10:30pm.
    * Extend by two days.  Please break up your work.
    * I need to find a three-hour block to write that assignment.
    * Python people should find an alternative.
    * You will have time to work on it on Monday.

### Good things to do (Academic/Artistic)

* MET opera on Saturday.
* Contra dance Friday at 8pm in Younker Lounge.  Live music!
* Two cool shows in the Faulconer.
* Islam week events next week (details forthcoming)
* Megan Goering design talk on Tuesday
* Wednesday visitors.
* I've been told that there's something on campus that doesn't fit my
  worldview: A concert on Rathje 3rd.  Saturday 3rd.

### Good things to do (Other)

### Friday PSA

* I brought BAC cards

### Questions

User stories
------------

* A way of understanding the requirements of your application from
  the perpsective of those who will be using the application.
* A user has something that they want to do, which is enabled by
  techology.
* How will the user employ the technology to achieve their goal.
* Ideally, gathered from talking to your users.
    * What are their goals?
    * How will they use it?
* They are a tool for communication.
* And they can serve as tools in the software construction process.
    * The core of your task list
    * A mechanism for testing

Format of user stories
----------------------

* Feature: A general name for what we are trying to achieve
* Actor (As _this-kind-of-user_)
* Goal (So that I can _something I want to achieve_)
* Action (I want to be able to _do this_)
* Examples - Help make sure that we all understand the Actor/Goal/Action
  triplet.

Assessing user stories
----------------------

Here's one way to think about user stories

* Specific
* Measurable
* Achievable
* Relevant
* Time-Boxed

Here's another, taken from <http://agileforall.com/new-to-agile-invest-in-good-user-stories/>

* Independent
* Negotiable
* Valuable
* Estimable
* Small
* Testable

Examples: SpamR
---------------

### Feature: SpamR

* As a member of the faculty of Grinnell College
* So that I can gather emails that people send to the csstudents mailing list
* I want to use SpamR service

Comments

* Does not meet SMART
* Doesn't have a clear motivational goal
* Doesn't have a clear process
* Why did I receive two *identical* answers to this question?

### Feature: gather emails that people send to the csstudents mailing list

* As a faculty member
* So that I can keep track of emails that are sent to the csstudents mailing list
* I want to create a service that gathers emails sent to the csstudents mailing list

### Feature: SpamR

* As a student at Grinnell College,
* So that I can filter and access emails that are sent to CS students emailing list
* I want to use SpamR service.

### Feature: Research Opportunity Detection

* As a student,
* So that I can be informed about all potential research opportunities,
* I want to automatically be forwarded any potential research opportunities by looking at certain words in the email title and body.

### Feature: List of events on Tuesday 13th February 2018

* As a student 
* So that I can update the college calendar with Computer
Science events, 
* I want a list of all Computer Science events mentioned in the emails scheduled to happen on 2/13/2018.

### Feature: List events

* As a student
* so that I can 
    * enhance my computer science education with extracurricular
      activities
    * so that I can determine if there are any events I want to attend
      (or at least that I want to do more than ___)
    * so that I can figure out where *not* to be on campus
    * find public food
* I want to 
    * find events by title
    * find all the events sent to the CS mailing list that mention
      a certain day
    * tag emails with a phrase
    * ...
* For example,
    * Given all the things that were posted in the past week
    * If I search for "2018-02-14", I should see
        * Cool alumni mentors on campus!
        * Inclusion in computing talk at 4:15 pm.
        * Tentative WinC meeting at 7:00 p.m.

Other partial stories ...

* As a student employee of communications
* so that I can update the calendar and keep my job
* ...

And another

* As an SEPC member
* so that I can update the calendar and promote my department

### Feature: ???

SpamR should save every email that gets sent to the csstudents, and be able to organize by sender, time-sent, or content & would need to have a username and password to be able to access all the emails. This is specific, measurable, achievable, relevant, and we could timebox it. 

* "Organize by sender" is specific
* "Organize by time-sent" is specific
* "Organize by content" is not specific; different people will implement
  it differently given that dettail.
* "Prevent those who lack an account from reading" is specific.
* [Not in the standard format.]
* No person.
* No name.
* No mtivational goal

Examples: Course planner
------------------------

### Feature: Create a good schedule

* As a student, 
* so that I can plan my courses such that I do not take too many hard courses in one semester,
* I want to see the ratings of each course in terms of hardness.

### Feature: (untitled)

* As a student, 
* so that I can spend less time worrying about signing up for classes, 
* I want to be able to enter in my four-year plan and automatically sign up for the necessary CS courses without doing it every semester.

### Feature: CS Course Planner

* As a CS student at Grinnell College
* So that I can track planned offerings of courses in the CS department
* I want to use the CS course planner

### Feature: Students can search for courses by courseID

* As the department chair,
* So that students can look for the exact section of a course they want,
* I want to search for courses in the course planner by courseID

User stories in testing (aka behavior-driven design)
----------------------------------------------------

* Good stories include examples.
* With some practice, you can turn those examples into test.
* Thing that people miss:
    * Tests live in a separate realm.  They generally do not
      access your current database.

User stories in planning
------------------------

* See above.
