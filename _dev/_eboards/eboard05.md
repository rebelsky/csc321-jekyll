---
title: Eboard 05  More fun with Rails
number: 05
section: eboards
held: 2017-09-07
---
CSC 321.01, Class 05:  More fun with Rails
==========================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Introducing Rails, round 2
* Introducing Rails, round 3

### News / Etc.

* Today we continue with Rails.
* Sorry for the delayed reading journal assignments.  Stay tuned for more.
  (Today's is posted.)
* We appear to have lots of sick students this a.m.
* Reminder: Friday is Add/Drop deadline.  And yes, that includes music
  lessons, too.
* Please submit Dudle poll on mentor session times.

### Upcoming Work

* Read [SaasBook, Chapter 1 and sections 10.1-10.2](../readings/saasbook1) (due Monday at 8 p.m.)
* Do [The introduction to Rails from SaasBook](https://github.com/saasbook/hw-rails-intro) (due Tuesday at 10:30 p.m.)

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* Convo today at 11am in JRC 101.
* Talk today at 4pm in JRC 101.
* Former governor Brandstadt tonight at 7pmish in JRC 101.

#### Peer

* Les Duke Saturday at 9 a.m. at the Golf Course.

#### Other

* Math/CS picnic Sept. 15 sign up by noon Sept. 8.

### Questions

Introducing Rails, round 2
--------------------------

We'll spend the first ninety minutes or so working on Chapters 1 and 2 of
_The Rails Tutorial_.  

<https://www.railstutorial.org/book/beginning>

Should we do all of our Rails work on Cloud 9?
  : Yes

Should we build a new VM for each project?
  : It's up to you.  You'll find that Hartl (today) and SaaSbook have
    different base VMs, so setting up a new one is good.

Do we have to use Bitbucket rather than Github?
  : No.  You can use Github.  Your repo will just be public.

Didn't you say that Rails was "convention over configuration".  What's
with this GemFile thingy?
  : Well, some configuration is necessary, particularly since APIs change
    so quickly.

Wow, there are a lot of magic incantations
  : Yup.  Doesn't that seem like a great opportunity for a cracker?

### Debrief

Why did we do both c9 and Heroku?  (Why don't we just run our servers on C9?)
  : c9 is designed for development; Heroku is for deployment.  You should
    not mix the two.
  : Development/deployment lets you preview/test changes without affecting
    your users.
  : Using different systems lets you keep track of what you're doing.
  : The platforms are built for different purposes.

What did you learn about setting up your system to run Rails?
  : I have to do lots of set up my system to run Rails.  (Yes, that's one 
    of the things that happens as you transition to being a software
    professional.  You no longer get to work with pre-configured systems.
    Some of you have more experience at this than others; CSC 321/22
    should help everyone.)
  : Minor details have incredible significance.
  : We rely on lots and lots of libraries ("Gems").  They change.  Even
    minor changes have ripples.  So we have to be careful in specifying
    versions.

Introducing Rails, round 3
--------------------------

We'll spend the last twenty minutes or so getting started with the
"clone and update" first Rails assignment from the SaaSbook.

<https://github.com/saasbook/hw-rails-intro>

[Or not]
