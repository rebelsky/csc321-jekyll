---
title: Eboard 10  Modeling basics
number: 10
section: eboards
held: 2017-09-26
---
CSC 321.01, Class 10:  Modeling basics
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Modeling data
* Strategies for doing modeling
* An exercise in basic modeling
* Exploring relationships between data
* Extending our sample model

### News / Etc.

* Please let me know when you notice problems on the Web site.  I think 
  I've fixed most of them.  (Okay, something is massively wrong with the
  generation of readings in the schedule, but that turns out to be a programming
  problem I don't have time to address.)

### Upcoming Work

* [Reading journal for class 11](../readings/models) due tomorrow night.
* Cucumber stuff due TONIGHT.
* No programming work for the following Tuesday.  Your final programming 
  assignment will be assigned Thursday and due Tuesday of week seven.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* The various Google activities.

#### Misc.

* Volleyball Wednesday night
* GHS Homecoming Parade Thursday night

### Questions

Modeling data
-------------

* Programs follows MVC
    * View: UI
    * Controller: Program logic
    * Model: Data and how we describe those data
* In designing programs one of the key/important things to do is to come
  up with model/models for your data.
* Objects w/o methods, structs in C, whatever
    * The "big picture" kinds of data (e.g., which objects do I need)
    * The individual components of each big-picture datum
        * Conceptual
        * Types
    * Example: Donors have names.  What type is name?
        * Option 1: A name is N strings: forename, surname, title, ...
        * Option 2: A name is a single string; we're smart enough to
          know how to parse those strings.
            * "Doe, John, Jr."
            * "John Doe, Jr."
        * Option 3: Rely on a separate "name" type
    * Example: Donations have dates.  What type is date?
        * Option 1: A triplet of three integers (day, month, year)
        * Option 2: A string, which we can parse
        * Option 3: An integer: Days since the start of time
        * Option 4: A built in type
   * Don't use slashes in your dates.  5/3/2018 could be May 3 in the
     the mixed up US system or March 5 in the more sensible European
     system.  2018-05-03 is unambiguously May 3.
* Note: We generally assume each value has its own unique id.
* What data do I want to model, what goes in each model, and what type
  is each component?
* Agile says: It's okay if you make some initial assumptions and then 
  change your mind later.
* Sam says: Adapting models can be incredibly difficult.  Good models
  are core to any project.
* Example: Head start phone notification system.
     * Original model had the following fields for students: ID, Name,
       Parent's name, Parent's phone number, Classroom
     * Whoops.  Some people have more than one parent or guardian.
* We need to start with good models
* It will take some effort to build them

Strategies for doing modeling
-----------------------------

* Consider options
* Know/use "the literature"
* Consider use cases
* DRY
* Pairs (or N's)

An exercise in basic modeling
-----------------------------

What are the models you expect to see in bad spuds, a database of
information on movies and reviews of those movies?

Movie

* title: string
* release-date: date
* director: Director (only one?)
* duration: int
* genre: string (?)
* roles: list-of(Actor*String)
* ...

Review:

* rating: real
* movie: Movie
* reviewer: Reviewer
* comment: text

Reviewer:

* name: ...
* reviews: list-of(Review)
* reputation: ...
* ...

Actor:

* name: ...
* dob: date
* gender: ...
* roles: list-of(Movie*String)
    * Robert Downey Jr is Iron Man in Spider Man, Homecoming
    * Robert Downey Jr is Tony Stark in Spider Man, Homecoming
    * Robert Downey Jr is Iron Man in Age of Ultron
    * Robert Downey Jr is ...
* ...

Director

* name: ...x
* dob: date
* gender: ...
* movies: list-of(Movie)

Studio

* name: string
* ...

Theatre

* name: string
* ...

Exploring relationships between data
------------------------------------

* There are many connections between models in any real system.
    * A movie has multiple actors
    * A review has a reviewer and a movie
    * A reviewer has multiple reviews
* We need to think about those relationships
    * OO relationships, such as is-a (inheritance) and has-a (inclusion)
    * We have some relationships that are one-to-one.  A movie has exactly
      one title.
    * We have some relationships that are one-to-many (and, conversely,
      many to one).  A movie may have multiple reviews.  A review is
      of only one movie.
    * We have some relationships that are many-to-many.  A movie has
      multiple actors.  Actors belong to multiple movies.
* How do we deal with these relationships?
* How do we want to deal with these relationships?

Dealing with relationships in Java.  

* E.g., the review:movie relationship.
    * Every movie has a list of review objects (or, implicitly,
      references to review objects)
    * Every review has a movie field that contains  
        * the title of the movie being reviewed. NO
        * the reference to the review object YES
* E.g., the reviewer:review relationship.
    * Every reviewer has a list of review objects (or, implicitly,
      references to review objects)
    * Every review has a reviewer field that contains a reference
      to the reviewer object
* Why don't we have just the title?  
    * The title may change.  
    * Links are easy to follow and we can get the title from the link.
    * You are storing more data.  Titles are bigger than references.
    * Titles are not unique.  There are at least two Bedazzleds and
      two Jumanjis and two Magificent Sevens and ...
* What principle does your design violate?  It isn't DRY.  We've 
  represented the relationship twice.
    * That means that there is a *potential* for a violation

Improving our approach?

* Indicate some aspects of the relationships and rely on the system 
  (or a library) to help with the rest.
* The most common language for modeling data is SQL
    * Describing a model in SQL is a lot like describing an object in Java
      in the sense that you give names and field types.
    * One key difference: No lists allowed.  One-to-many relationships
      get handled by the info being only in one object.
    * To find all the reviews for a movie, we will search the collection
      of reviews for those that link to that movie.
        * Sounds inefficient, but lots of work has gone into
          implementing these databases so that we can quickly gather
          such info.
    * Second key difference: Instead of explicit references we associate
      an id with each item and refer to those ids
* 1:1 relationship and one model clearly dominates, just shove the fields
  of the dominated model into the primary model.  Alternately, pick one
  to link to the other.
* 1:many relationship, the one contains the id of the many
* How do we handle many:many relationships, given that we don't have
  lists in our models?
    * Add another object that has a one:many relationship to movies
      and a one:many relationship to actors.
    * Sam would call that "role"

Rails takes this a step further: You just describe the relationship
you want, it handles things behind the scenes.

Extending our sample model
--------------------------

Identify all of the relationships in our simple model.

* Studio:Movie is many:many
* Role:Movie is one:many, at least in some perspectives
* Role:Actor is one:many, at least in some perspectives
* Review:Reviewer is many:one
* Movie:Setting is many:many
* Movie:Title is just confusing (okay, it's probably many:one)

Note: It is sometimes better to write your programs so that they adapt
from one to many values in a field.  (E.g., rather than assuming you have
one title, even though you do, write code that assumes you have many.)

Typography detour
-----------------

When writing, we often use a horizontal line between things.  

* Connector: Sam is an anal-retentive person.  Connect with hyphen.
  One dash.  Also used in dates in IEEE format, 2017-09-25.
* Range: Sam worked at Grinnell 1997--present.  Traditionally, typographers
  use a longer dash than a hyphen in these situtions.  That symbol is
  called an en-dash (or ndash).  Its width is approximately that of an
  n in the current typeface.
* Separator: Sam---who some consider the strangest person to teach at
  Grinnell---has trouble coming up with examples.  Typographers traditionally
  use an even longer dash in these situations.  It's an em-dash.
