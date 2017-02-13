---
title: Eboard 08  User stories
number: 8
section: eboards
held: 2017-02-08
link: true
---
CSC 321.01, Class 08:  User stories
===================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Agility, revisited
* What user stories
* User story criteria
* Sample user stories

### News / Etc.

* Yes, we are skipping Hartl chapter 4.

### Upcoming work

* Hartl, Chapter 4 due Friday.  (Do as much as you can within your time box.)
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.10) due
  Monday.

### Good things to do

*Nope, no extra credit.*

* Scholars Convocation, Thursday, 9 Feb 2017, 11:00 a.m., JRC 101.
  David Orr: *Climate Change and the Crisis of American Democracy*.
* Thursday extras, Thursday, 9 Feb 2017, 4:15 p.m., Science 3821: Something on
  computer graphics (visitor from UMN).

### Questions

Agility, revisited
------------------

### Why agile?

* Evidence suggests that it is more likely to bring projects in on time
  and under budget.  (And then there's www.grinnell.edu)
* More user focused than both kinds of plan-and-document - regular 
  check-ins with clients to make sure that you are on target, and to
  adapt to moving targets.
* Each iteration is small.  Small is good.  Feels more feasible.  Concrete
  achievements.
* Don't spend time on things that aren't going to get done anyway.

### Why not?

* Wastes time if you have a situation in which plan and document will work.
* Mostly designed for small and medium projects; little evidence that it
  works for big projects.
    * Hard to get everyone together.
* Good design encourages us to write general code.
* Some characteristics of projects are not amenable to agile design, such
  as security.  It's hard to engineer in security afterwards.
* Odd not to have deadlines.
* Geographic separation or unavailable client
* It's not engineering
* Paying by time, rather than product, is not optimal for the client.

### Good practices

* Allows you to focus on smaller parts, without worrying about the whole
  project.
* Give programmers ownership.

User stories
------------

* An attempt to clarify a client's goals.
* Typically, written by the developers, after listening to the client.
* Used to communicate.
* Used to prioritize.

Assessing user stories
----------------------

What are some criteria we should use as we consider user stories?

* Three primary components
    * Perspective "As an old person who knows about computers"
    * Goal "So that I can communicate with my grandchild"
    * Feature/process "I want to be able to type a message and click a button and have the message delivered directly to my grandchild's cortex."
    * Aka "Who we are, what we want to do, and why"
* Clear and straightforward; unambiguous
* SMART - Specific, Measurable, Achievable, Relevant, Time-boxed
* Nice to have examples for clarification!

Some user stories to assess
---------------------------

For each

* Is it a good (SMART) story?  Why or why not?
* Rewrite the story to make it better.
* Add an example.

### SpamR

#### Feature: (Untitled)

* As a student, 
* so make the mail box clear and be able to find the older email, 
* I want to archive all of the emails.

Critique

* Not very measurable.
* Unclear
* Not specific
* Ambiguous: What does archive mean?  What does find mean?

Rewrite

* As a student
* I want to view all of the past emails to csstudents in chronological order
  from newest to oldest
* So that I can find newer emails

Critique

* "Store" is odd.  (Replaced with "view" above.)

Example

* Suppose I have the following emails from csstudents
    * Summer research / From Sam / Dated 2017-01-01 12:01
    * CS Table / From CC / Dated 2016-09-11 0:30
    * Thursday Extras / From Reseda / 2017-02-01 0:00
* They should appear in the order
    * Thursday Extras / From Reseda / 2017-02-01 0:00
    * Summer research / From Sam / Dated 2017-01-01 12:01
    * CS Table / From CC / Dated 2016-09-11 0:30
 
### Feature: Add internship calendar

* As a student 
* So that I can look at what internship/research positions are available and when their applications are due. 

Critique

* Missing one of the three legs.
* Perhaps too big.
* A bit ambiguous.

### Feature: Filter emails 

* As a: student on the cs mailing list
* So that: I can read only emails that interest me
* I want to: be able to set filters when viewing emails 
* (e.g. filtering summer opportunities/grad school programs/Thursday extras etc.)

Critique

* How do we measure "emails that interest you"?  How do we know that
  we are successful.
* Assumes that emails are categorized.
* What is filtering?

Rewrite

* As a: student on the cs mailing list
* So that: I can read the email of interest
* I want to: Be able to read only the email in a certain category
* (Implication: Email is categorized.)

### Feature: Archive emails sent to CS students

* As a Grinnell CS professor
* So that CS students are able to see opportunities for themselves
* I want to make opportunities visible to all CS students

Critique

* Needs us to read in between the lines.  (Ambiguous)
* Redundant: action and goal seem similar.
* Maybe should talk more about details of the implementation.
* Too "big picture"

### Feature: (Untitled)

* As a student at Grinnell College, 
* I want a tagging system 
* so I can easily find archived emails pertaining to internships. 

Feature: Store all CS Emails
* As a student,
* So that I can have a collection of emails,
* I want to read emails later.

Feature: (Untitled)
* Students: 
* effectively filter all spam and have the option to sort all emails by date or sender or subject 
* so that they can better organize their emails

Feature: Add an email blacklist
* As a faculty member
* So that I do not see mail from particular individuals
* I want to blacklist individual users by email address

Feature: Users can filter emails by tag
* As a student,
* So that I can know what to read for the next CS table,
* I want to click a button to have easy access to a chronologically ordered list of the emails related to CS table.

Feature: Selecting and viewing emails
* As a student, 
* I want to be able to search the record of CSStudents mailing list by keyword(s) and displayed in chronological 
* so that I can find the most recent relevant emails to my keyword(s).

Feature: (Untitled)
* As a faculty member 
* I want easy access to find the emails that have been sent 
* to reuse them later or read them to see what I have sent so far.

Feature: (Untitled)
* As a student, 
* I want to be able to search for emails by subject, 
* so that I can look for messages related to internships and other topics.

Feature: (Untitled)
* As a student, 
* I want to have the csstudents emails filtered into different folders 
* so I can be more organized.

### Course Planning

Feature: Course Preference Indicator
* As a Computer Science department chair,
* So that I can effectively plan for course offerings, 
* I want to be able to assess the interest of computer science students in the tentative schedule for future years in number of students potentially interested.

Feature: see how many people plan to take a specific class next semester
* As a department chair
* So that I can plan the number of sections provided for that class.
* I want to avoid cutting people from the class.

Feature: Tally how many students are interested in a course
* As the department chair
* To better anticipate the need for different classes in any given semester
* I want to have a mechanism to track and tally students planned courses based off of student responses

Feature: Select potential class enrollment 
* As a: student
* So that: my professors can plan accordingly and avoid over-enrollment which puts me in a smaller class (almost always preferable)
* I want to: indicate my desire to enroll in a specific class offered in the current academic year 

Feature: Show tentative offerings
* As a student
* I want to be able to lists of planned offerings of courses by semester in course order, including brief description
* So that I can easily and quickly determine what cs courses will be offered each semester

Feature: Student can search the CS course planner that fits their current schedule and  4-year plan
* As a Grinnell CS student
* So that I can plan my classes to have a balanced schedule that allows me to graduate on time
* I want to plan my semester schedule and 4-year plan
* Scenario: Add a CS class to my next semester schedule
    * Given I am on the CS course planner home page
    * Then I should see a "4-year plan"
    * When I press "4-year plan"
    * Then I should see a 4-year plan in semester format
    * When I press the next semester
    * Then I should be in the next semester schedule in calendar format
    * Then I should see "Search CS courses"
    * When I press "Search CS courses"
    * Then I should see a list of CS courses offered that semester with details of each course
    * Then I should be able to click an "Add course to schedule" button on each course offered
    * When I press "Add course to schedule" for a specific course
    * Then I should be able to see the course in my next semester calendar
    * And the department chair and faculty should be able to see that I have planned that class too

Feature: Useful data presentation for future planning
* As a department chair
* So that I can plan classes and faculty hiring in the future
* I want the data on total number of students planning to take different CS classes

Feature: View planned courses for next three years
* As the department chair
* So that I can see how the demand for certain courses is changing over time
* I want to see all classes planned for each semester for the next three years on the same page and how many students have expressed interest in taking each class each semester

