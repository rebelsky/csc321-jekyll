---
title: Eboard 17  UML
number: 17
section: eboards
held: 2017-03-01
---
CSC 321.01, Class 17:  UML
==========================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Context
* UML Class Diagrams
* UML Activity diagrams

### News / Etc.

* Faculty are bad at writing recommendation letters on time.  REMIND THEM.
  THEN REMIND THEM AGAIN.  

### Upcoming work

* For Friday

### Good things to do

* CS Extras, Thursday at 4:15 pm, Summer Code Camps

### Questions

Context
-------

* Design is not normally a solo activity.
* We need a way to communicate our designs to other people.
* Code?  (Sometimes obscures the key concepts.)
* English?  (Sometimes ambiguous and inexact.)
* Pictures! (usually ambiguous, but easy to grok quickly)
* Many systems were developed to write pictures about programs
    * Flowcharts!
* OOP generated way too many approaches
* At some point, some leaders worked on developing a relatively common
  set of diagrams.
    * Sam believes it's okay if you are not exact in the system, as
      long as everyone understands what you are showing.
* These systems exist as a way of talking about the design of programs.
* Things we think about
    * Hierarchies
        * Inheritance
        * Interface & implementation
    * Functionality of classes/objects
        * Methods
    * Dependencies and scopes (e.g., we rely on a library or another
      object to do some of our work)
    * Boundaries
    * Interaction between objects
* *Warning!  Sam doesn't use pure UML enough, and pure UML changed at 
  least twice since Sam learned it.*

Static UML class relationship diagrams
--------------------------------------

* Core: The Class
* For classes, represent
    * Name
    * Methods (at least externally facing)
    * Fields (at least as necessary to think about design)
* Relationship between objects
    * Inheritance
    * Have as field 
    * one-one, many-one, many-many
    * Calling capabilities
    * composition vs. aggregation (hah!)
        * Is the relationship one in which the destruction of one object
          should cause the destruction of the other, or not
* Interfaces vs. classes
* Visibility (whoops, Sam is incompetent again)

UML action diagrams

* One column per object
* Draw lines to represent procedure calls as you think about the steps
  that are made in your process.
* Action progresses downward.
* Why draw rather than write the code? 
    * lets you backtrace
    * much faster to grok without switcing between tabs
* Why would we find this useful to draw?
    * As we draw, we talk about which method goes in which object.
    * Helps you understand relationships for when you are making changes
    * Helps you ask about these kind of things
    * Lets you backtrace

Learning goals

* "Oh, drawing diagrams is helpful."
* "I should draw things that look kind of like the things Sam drew"
     * Maybe with local modifications
     * Maybe by looking up the official "syntax"
* "It's not too hard."
