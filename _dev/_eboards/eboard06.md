---
title: Eboard 06  An introduction to software engineering
number: 06
section: eboards
held: 2017-09-12
---
CSC 321.01, Class 06:  An introduction to software engineering
==============================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Good stuff to do
    * Questions
* Part one: Concepts
    * Models of software engineering
    * Important agile practices
    * Why agile?
    * Why not agile?
    * Your questions
* Part two: Rails work
    * Quick discusison
    * Lab time

### News / Etc.

* Remember to use Slack for questions!
    * <https://grinnell-sw.slack.com>
    * Use +# homework to add the homework channel.
* I'm glad to see that many of you are most excited by "I get to build
  software in a very different perspective."
    * To build software, we should have some understanding of concepts
      and practices.

### Upcoming Work

* Readings: [SaasBook, Sections 7.1-7.5; re-skim Ch. 2 and 4, Stallman](../readings/user-stories) (due Wednesday at 8 p.m.)
* Programming assignment forthcoming.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* CS Table Today.
* CS Extras Thursday.

#### Peer

* CS Extras Thursday.

### Questions

How do I find stuff on your Web site?
  : Go to the right one.  (That's a hint to Sam.)
  : The current eboard usually has the upcoming homework.
  : The schedule sometimes has the upcoming work.
  : Email/Slack me when things don't work, or when you have to remove 
    the dot.
  : Generally assume: Reading journal every class and homework every
    Tuesday night.

Models of software engineering/design/construction
------------------------------

We saw three models of software design

* Plan and document
    * Waterfall
    * Spiral
* Agile

_With the person next to you: Three things in common, three things different._

* Note: Sam has you discuss because evidence is that you learn better when
  you think actively than when you just listen.

Things in common

* All have something like a maintenance (sp?) phase
    * Waterfall asssumes that if you do other things well, you won't
      have many bugs that you have to squash.
    * Okay, all of them assume that you have caught most bugs during
      the development process.
* All three require that you allocate workload among team
    * Break up the software into components
    * Also different roles: Testers, developers, etc.
* All three begin by gathering requirements from the client
* Prepare to develop - document (user stories vs. detailed specs)
* Write tests
* Develop
* Release
* Maintain

Things different

* All three begin by gathering requirements from the client
    * Waterfall: Assumption is that you gather *all* requirements
      from the client up front and those requirements won't change.
    * Agile: Requirements change, so revisit with client regularly
* Prepare to develop
    * Waterfall: Documentation then tests
    * Agile: Tests and stories.
* Waterfall goes through the "cycle" once. Spiral and agile go through
  the cycle multiple times.  
    * Agile: The cycle/sprint/... is usually one or two weeks
    * Spiral: The cycle is usually a few months

Important agile practices
-------------------------

* Communication with the user - In the end, we're building software
  for someone, so talk to them.
    * Try to think about the different people who use the software.
* Pair programming - Driver and navigator.  Navigator suggests big
  picture approaches, driver codes.  Driver asks questions, Navigator
  serves as reference.  Both challenge each other's ideas.
* Test-driven development.  Write the tests before the code.  Tests
  even document.  Is it ambiguous whether we do X or Y?  The test tells
  us (particularly if we can read it).
* Solve the problem at hand, not the generalized version.
    * Faster: Gets code into the hands of our customer.
    * There are many (?) times you'll never need the generalized version.
    * Smaller
* Ruthless refactoring - Keep your code DRY.  When you find that it's not,
  your highest priority should be to make it DRY.
* Short sprints - Go back to the client regularly to reprioritize.
    * Keep list of possible tasks.
    * Work with client to figure out priority.
* Daily standups - Short time of "what did we do recently?" "what are
  we doing today?" "what stands in our way"
* Principle: Active communication within team and with client.

Why agile?
----------

* Regular feedback - It's helpful to know that you're making progress
  in the right direction.  It's also useful feedback.
    * Exciting to programmer
* Exciting to client
    * Seeing the process
    * Feelings of control
* We don't believe that plan and document sufficiently addresses the
  unknowns in the process.
* Gets "something" out now.
* The context changes regularly, so we assume that our software also
  has to change regularly.
* Good evidence that agile is more likely to build the software that the
  client actually wants.
* Good evidence that agile is more likely to build working software.
    * Although it's a different version of working.

Why not agile?
--------------

* Assumption that it's not long-lasting.  (It may just be that the
  current form is not long-lasting.)
* Personality - "I don't want to work with other programmers."
* It feels like it takes a lot of time to check back in with the clients. 
    * We already told you what we want.
* Some things, like security, take time.
* It's not engineering.
* We are told that software is just another "big construction project".
  Why should we assume that the process that works for *every other*
  big construction project is not going to work for agile.
* Without documentation, how do we know that it meets the requirements?
* Agile seems to be better designed for medium-sized projects (at most
  a few dozen) rather than huge projects.
* Agile seems focused on one set of clients.  What if you have many?

BREAK
-----

_Five minutes_

Explaining Sam's teaching practices in this class (briefly)
-----------------------------------------------------------

* This class is about many different things
    * Learning to use tools
    * Learning practices and principles
* The reading gives you a lot of information.
* My goal is to help you think through that information - its implications,
  its potential complexities, etc.
* Reading journal - encourage closer reading.
    * In this class: To encourage different "kinds" of reading.
* Time in class to talk to each other - You learn by thinking more than
  listening.
    * You also take in new ideas better when you've considered the
      context first.
* Calling on you - Helps enforce the prior, gets a broader set of
  perspectives.

Your questions/comments - Agile
-------------------------------

### Quick / Snarky responses

The concepts are clear.
  : Great.  You can answer some of the questions below.

Nothing really. This chapter wasn’t overly technical, which is most
likely what will confuse me at times.
  : Great.  You can answer some of the questions below.

The book itself is kind of confusing because I don't really learn from
reading from textbooks. I learn better from actually writing code. But
I understand why we're doing these readings because I know it'll be
important for our understanding of Ruby later on and working with our
customers.
  : There's *much* more to software development than writing code.

### Pair programming

I never thought that paired programming would have so many benefits.

Probably the tests that were conducted to estimate the effectiveness of
pair programming. Seems, like the studies weren't done comprehensively
and the results are not all too reliable. Which means, the effectiveness
of pair programming is still like a Schrodinger's cat.
  : In most software design practices, it's more theory than formal
    evaluation.
  : But pair programming has had more formal evaluation than most things.

I was very surprised that the book recommended pair programming. In my
experience pair programming is extremely slow and doesn’t lead to much
better results (though maybe with two high quality programmers things
are different?), so seeing studies to the contrary was pretty surprising.

### Expectations

It seems to me that even in Agile there must be an initial design phase
for a new project in which you, at the very least, sketch an overall
architecture (even if you expect things to change). The SaaSbook,
however, seems to imply that there is no upfront planning for Agile in
the long-term, which seems a bit odd if not confusing.
  : There aren't many different "big picture" designs for systems.
    So you start with one that seems appropriate and go from there.

Agile's de-emphasis on documentation. It's weird that after how much
emphasis was put on documentation throughout the years, agile would tell
everyone that they should focus on things other than documentation. What
is meant by de-emphasizing documentation? Is it saying we should write
fewer comments, or document our daily progress less, or not write detailed
reports on how each function works?
  : Tests document!
  : Documentation goes stale.
  : Of course, pair programming should help

### SOA

I don’t really get what SOA is. It seems like the idea, at least from
the Bezos email, is that it’s the philosophy of designing systems
that are modular, where modular means all ways of interfacing with them
are done through methods provided by those systems. Why is that good
though? Does it make your system more stable?

The concept of Software Oriented Architecture (SOA) says that the
programmer should expose the internal modules used by the program. Is
this not contrary to the idea of 'encapsulation', where only the details
the 'outside world' would use are exposed? Also, wouldn't a single API
for the whole application make it easier to modify, or even switch out,
the internal modules?
   : It's not exposing the whole code.  It's treating a collection of
     stuff (a module) as an independent unit that is encapsulated.

I'm generally confused about siloed software versus SOA.

Answers
  : SOA is "Service Oriented Architecture".  APIs.
  : Have the different components of a larger project communicate
    through APIs (interfaces).
  : Makes it easier to enlarge the project.


### Misc

I am not sure particularly sure why clusters are preferred over big
iron databases. I would imagine updating the software in the big
iron case would be much quicker and in industry I imagine speed is
imperative. Furhermore regardless of how small computers may become,
wouldn't clusters incur higher costs due to larger storage space,
wouldn't one simply make smaller big iron contraptions also if technology
has advanced.

I am a bit confused by the organization of this textbook (also possibly
the order of the readings?). I feel that it contains useful information,
but I don't necessarily know how to apply it to the coursework just yet.

I was confused as to why we would have so many different types of testing
methods. I'd imagine unit testing would do comprehensive tests but I
suppose it's very tedious.

I don't really understand Cloud Computing and it would be great if you
can explain it a bit more.

What was confusing about this readings is what to do with all the
information supplied. There was much talk about ACA and Google+ API's
and Facebook and mentioning of these weird software deployment tools and
terms like 'cucumber' and Scrum. Rather than enriching my knowledge,
it just obfuscated the topic and added to the mystique of software
engineering with all its weird and unintuitive acronyms.

Is the Scrum Master the same person at each meeting, or does the position also rotate around the group like Product Owner?

How should different software design workflows (agile, waterflow, etc)
be chosen, as a function of the type of software you are building,
or as a function of the team you are working with?

I was confused by the plan-and-document style Rational Unified Process
lifecycle. It sounds to me like a disordered version of the Spiral
lifecycle that just goes through random phases and iterations according
to whatever needs doing, or something. I don't really understand the
logic of it.

Your questions/comments/frustrations - Rails Project
----------------------------------------------------

How do I set up a link correctly for the "sort by title"

How is bad spuds organized?  How do we navigate?  Where do I look?
  : That's one of the learning goals.

Where do I find the view?
  : `app/views`

```
-#  This file is app/views/movies/index.html.haml
%h1 All Movies

%table#movies
  %thead
    %tr
      %th Movie Title
      %th = link_to 'Rating', movies_path(sortby: rating)
      %th Release Date
      %th More Info
  %tbody
    - @movies.each do |movie|
      %tr
        %td= movie.title 
        %td= movie.rating
        %td= movie.release_date
        %td= link_to "More about #{movie.title}", movie_path(movie)

= link_to 'Add new movie', new_movie_path
```



How do you examine the application from a fresh state?
  : Run it on C9?

Why doesn't it work on C9 when it works on Heroku?
  : We'll look at that

How do you share a workspace on C9?
  : KY is giving you instructions now.
