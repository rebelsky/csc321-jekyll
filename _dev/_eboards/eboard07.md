---
title: Eboard 07  Key ideas - Software as a service and user stories
number: 07
section: eboards
held: 2017-09-14
---
CSC 321.01, Class 07:  Key ideas - Software as a service and user stories
=========================================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Good things to do
* Project work time
* SaaS
* User stories
* Using user stories
* Making user stories SMART
* Your user stories

### News / Etc.

* Attendance.
* I think I've been off by one on the reading journal numbers.  Apologies.
  That issue is now fixed.
* I've added a week to the due date to the introductory rails assignment.
* Please let me know when you notice problems on the Web site.  I think 
  I've fixed most of them.
* We will be discussing user stories that involve projects on the elderly,
  sexual assault, animals, hunger, health, volunteering, and four-year
  planning.  Please feel free to leave the room at any point if you find
  these conversations difficult.

### Upcoming Work

* Programming assignment: [Intro rails](../assignments/getting-started-with-rails) (due Tuesday the 19 at 10:30 p.m.)
* Readings: [SaasBook, Chapters 7 and 8](../readings/tdd-bdd) (due Monday at 8 p.m.)
* Programming assignment: [Cucumber](../assignments/cucumber) (due Tuesday the 26 at 10:30 p.m.)
    * Those working on Python/Django projects may choose to design their own equivalent assignment.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* CS Extras today
* CS Table Tuesday (tbd)

#### Peer

* CS Extras today
* Elephantitis this weekend (Saturday morning at HS and afternoon at MS)
  (Sunday at HS)

Project work time
-----------------

I couldn't get it to deploy to Heroku.  I skipped that step.
  : Knowing how to deploy is important.  Ask for help.

Wow, minor things cause big problems!
  : Yup, we've talked about that before.
  : Context is important.  Execute commands in the correct directory.
  : Executing (or failing to execute) prior commands, a current command
    may/may not work.

I have no idea why I'm getting an error?
  : If you see a "nil, no such method" error, it means that you haven't
    assigned a value to a variable that you are using.
  : Think more carefully about program logic.

What are the big-picture issues you saw?
  : It's hard to program when you don't have immediate help available.
    But that's something you have to learn.
  : You need to ask questions of others.
  : The steps are important.

SaaS
----

_Note: Your most common response is that Stallman is an idealist and
most people have to deal with compromises._

* What is it?
* Why do some folks like it?
* Why do some folks dislike it?

User stories
------------

_What are they?_

* A way of describing the goals of our project, primarily from the user's
  perspective.

How do we represent them?  

* Feature: A general name for what we are trying to achieve
* Actor (As _this-kind-of-user_)
* Goal (So that I can _something I want to achieve_)
* Action (I want to be able to _do this_)
* Examples - Help make sure that we all understand the Actor/Goal/Action
  triplet.

Sample example

* Suppose our database includes the following entries

        Rebelsky        Fall 2017       CSC 321 01      2
        Rebelsky        Fall 2017       CSC 322 01      2
        Rebelsky        Fall 2017       CSC 301 01      4
        ...

* When I go to the "total teaching load" page, select "Rebelsky", and
  click "Compute", I should see ...

Why do we have them?

* Communicate with the user
* Stories provide an opening point for discussions.  "If this is your
  goal, couldn't we also achieve it this way?"  "Why are you doing this?"
* Lets us prioritize

Making user stories SMART
-------------------------

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

Your stories
------------

### Stories to discuss

#### Unknown project: 

* Display a page to the user with a title

Problems

* Not specific
* Not necessarly applicable
* Not a known user base.

#### Project PALS: Add a posting system for car pool services for those without personal transportation to get to PALS

* As a volunteer,
* So that I can volunteer at PALS without worrying about how to get to the animal shelter,
* I want to add a posting system so that any volunteer with a car can volunteer to pick people up or drop them off. 

Fixes

* Needs to better express what actions you'd like to do.
* "I want to be able to indicate that I need a ride and be notified at
  least one day in advance if that ride is available."
* Might also add: "I want my shift cancelled and me to be notified at
  least one day in advance if that ride is not available"

#### Callisto: Untitled

* As a survivor, 
* I want to have different methods of reporting my case. It should be either a voice recording, call for Grinnell Advocates or other national hotlines, text typed on a computer, or a picture of documents written on paper 
* So that I can report with the least trouble

Problem

* Too complex.  Needs simplification (multiple cases).
* Also needs story of "I can retrieve it later."

#### Callisto: Proving confidentiality of sexual assault report

* As a sexual assault survivor
* So that I can feel comfortable reporting the assault
* I want to be able to know that my report will be confidential until I choose to release it

Problem

* Needs measuring.

#### Callisto: Untitled

* As a school official, 
* I want to see the analytics of sexual assaults reported on campus (where, when, how) without seeing the victims or perpetrator's name, 
* so that I can adjust campus policy accordingly to minimize these incidents

NO NO NO NO NO

#### Mayflower Project: Untitled

I am a member of the Mayflower community who has been staying with my son
for 4 months as I prepared for his wedding. I am getting ready to head
back to the community and I would like to see if there are new faces
when I get back. I would also like to look up if they had similar past
experiences with me so that I can have something to talk about in our
initial interactions.

Problems

* Not in the proper form.
* Multiple goals and actions

#### Heartland Project: News Column

* As a person who is concerned about global health problems,
* So that I can obtain news from the website,
* I want to know about the status quo of global health.

#### Four year planner: Change a class’s location

* As an administrator
* So I can change a room if a class is too big
* I want to be able to change the location of a class

#### Heartland Project: Untitled

* As a concerned citizen of this country, 
* I want to be able to get access to to all documents to water quality 
  in one place 
* So that I know how my environment affects my health.

#### Mayflower Project: Password/information protection

* As a Mayflower resident, 
* so that I can keep my information private and viewable only to people I 
  permit, 
* I want to be able to hide/share my information as I please.

### Other stories

Callisto: Untitled

* As the Title IX coordinator
* So that I can bring justice to survivors and protect the community from future offenses
* I want to be notified within 10 minutes when the same assailant is reported more than once

Mayflower project: Search for resident

* As a Mayflower resident,
* So I can access my co-resident's phone numbers without having to have them written down,
* I want to be able to search for other resident's names and have their contact information be displayed. 


Mayflower project: Edit resident information

* As a Mayflower employee,
* So I can change a resident's residence information when they move rooms without deleting and recreating a new user profile,
* I want to be able to edit the information for a resident's profile, without other residents being able to edit others' information. 

Four year planner: Add a class

* As a student
* So I can have my advisor know I want to take a class
* I want to be able to add classes to a schedule
 
Heartland Project: External Resources

* As a student who wants to know more about global health,
* So that I can find the relevant links to different websites,
* I want to learn from those extra resources.

Mayflower project: Untitled

* As a staff member from Mayflower Community, 
* I want to easily search on a webpage a resident by their name or last name or nickname, 
* so I can know more about their personal information like phone number, family members, etc.

Heartland Project: Untitled:

* As a scientist who knows about the water quality in Powersheik county, 
* I would like to be able to upload any of my research findings on the internet
* So that anyone can have access to it and use it for educational purposes

Mayflower Project: Sorting by last name/first name/etc- 

* As a Mayflower staff member, 
* So that I can find the correct information quickly, 
* I want to be able to browse a sorted list of the directory's information.

Mayflower Project: I am a manager of the mayflower community database in charge of organizing social activities. I have had to leave Grinnell for a business trip and I have just received information about a new member joining the community. The folks back in Grinnell have entered his details in the database.  I would like to add him to a bowling group for Wednesday night bowling and will have to go through his details to see who I think he would have a great time with since he is new in town.

Mayflower Project: Untitled

* As a staff member from Mayflower Community, 
* I want to enter or edit a resident's data in a non-complicated way, 
* so I can have our database updated.

PALS Project: Implement a scheduler system with a work description so that volunteers can sign up for work they want on available dates

* As a volunteer,
* So that I can sign up to help the animals without worrying about reaching out to the PALS director and finding the suitable time,
* I want to add a scheduler system in the calendar that provides information on the work and dates available.

Project Callisto: Notifications

* As an administrator, 
* so that I can keep up with reports made by multiple people, 
* I want to be notified within one day by some sort of secure method when the same assailant is reported multiple times.

Project Callisto: Timed Updates. 

* As an administrator, 
* so that I can keep an eye on trends in reporting, 
* I want to be notified on some sort of regular basis set by me about trends in reporting.

Unknown Project:

* When user enters their name into name box, their name will be saved
