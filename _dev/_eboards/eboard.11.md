---
title: Eboard 11  Modeling basics
number: 11
section: eboards
held: 2017-02-15
current: true
---
CSC 321.01, Class 11:  Modeling basics
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions

### News / Etc.

* Sample departmental schedule should be distributed later today.

### Upcoming work

* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.12)
  due Friday.

### Good things to do

*Nope, no extra credit.*

* Thursday extras, Thursday, 16 Feb 2017, 4:15 p.m., Science 3821: 
  4-1 Program with UIowa.
* CS Table, Tuesday, 21 Feb 2017, noon: Net neutrality.
* Senior day for basketball on Saturday (women's and men's).
* Swimming and diving this weekend.
* Orchestra Saturday.
* Slavic coffee house, Saturday, 5:30-7:00 p.m. Bucksbaum Rotunda.

### Questions

Modeling Data
-------------

* Almost every non-trivial application will have different kinds of data
  with which you will work.
* As a designer, you have a responsibility to think about the different
  kinds of data you have, what values are associated with each kind of
  data, and how the values relate.
* Although agile may seem to suggest that you can clean up from your choices,
  some early choices can have very negative implications.
    * Example: Head start phone notification
    * Models: Students, Parents, each student has exactly one parent;
      each parent has exactly one student.
        * Data duplication!
        * Not possible to do some things
* Getting models somewhat right early on is important
* Model: 
    * List of information to store for each "thing" of a particular type
        * Post: 
            * ID: identifier
            * Date/Time posted: datetime
            * Title: string
            * Contents: string
            * Tags: ???
            * Writer: ???
        * Writer
            * ID: identifier
            * Name: 
                * Option 1: string
                * Option 2: first name string, last name string
                    * May have duplication
                    * Cultural expectations
                    * Family name and individual name
                    * Not everyone has two names
                    * Pre-marriage name and post-marriage name
                * Option 3: name datatype
            * Posts: ???
            * Fake biography: String
     * In some cases, we have a clear basic type (or complex type),
       in others, we have relationships to other objects
         * Each post has one writer; each writer may have many posts
           (one to many relationship)
         * Good modeling systems let you "rip out" those relationships,
           and express them separately, so that they can deal with them
           behind the scenes
         * Three general kinds of relationships
             * 1:1 relationships
                * ideally, we wouldn't replicate names
                * each writer has a unique id, each unique id refers to one writer
             * 1:many relationships
                * One writer has many chirps 
             * many:many relationships
                * each child may have multiple guardians, each guardian may have multiple children
                * each chirp can have many tags, each tag can be associated with many chirps

Doing modeling

* List the kinds of values you will deal with (e.g., students and guardians
  or chirps and beaks)
* For each kind of value, list the key fields (ignoring id and relationship)
* List relationships

Alumni.grinnell.edu

* Values
    * Users (alumni, current students, ...) [0,5]
        * re'sume's, type: data
    * Donations [1]
    * News stories [2]
    * Photographs [3]
    * Events [4]
* Relationships
    * E.g., Each user has many (or zero) donations

*Task: Figure out the data you would associate with each person*

### Models

User

* name: name
* cv: data      /* can also hold r&eacute;sum&ecute;s */
* home-phone-number
* work-phone-number
* mobile-phone-number
* facsimile-phone-number
* other-phone-number
* info-public?
* contact-me?
* home-email
* work-email
* location: address
* biography: string
* linkedin: URL
* Facelessbook: URL
* relationships
    * user:major is a many-many relationship
    * user:job is a one-many relationship
    * user:event is a many-many relationship, with annotations

Donation

* id: (implicit)
* amount: long;
* currency: string;
* anonymous?: boolean - a signal that we are not supposed to reveal
  the donor's name
* recipient: string
* additional-notes: string

Detour: Currency

* name: string
* conversion rate to US dollars: ratio of two unsigned integers
    * doubles round

News story

Photograph

* photographer: (either with a relationship to an author model or name)
* datetime: datetime
* caption: string
* description: string
* image size
* image type
* image resolution
* relationships
    * 1 event, many photographs
    * many-many: photograph tag


Event

### Relationships
