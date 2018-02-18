---
title: Reading
subtitle: Modeling
schedule: 2018-02-19
link: true
day: 13
due: 2018-02-18
due-time: 9:00pm 
---
# Reading: {{ page.title }}

{% include due.md %}

Read [Wikipedia on Data Modeling](https://en.wikipedia.org/wiki/Data_modeling).

For the journal send an email message to me titled "**CSC 321 2017F,
Journal for Day 13 (*Your Name*)**" (without the quotation marks) and
with answers to the following questions.

Pick three kinds of compound data that you would expect to see in a
four-year planing system for Grinnell.  (You should think about the objects
you would write in an object-oriented language or the table you would
create in a relational database).  For each kind of compound datum, describe 
the fields and types you would associate with that datum.  If possible,
describe relationships between the three kinds of compound data.

For example, if I had been asked to describe three kinds of compound
data in a movie review database, I mind say that there are movies,
reviewers, and reviews.  A movie has a unique identifier, title, a director, 
a release year, a list of actors/role pairs, and a list of reviews.
The title is a string.  The director is probably a Person object.
The release year is an integer.  And so on and so forth.  A reviewer has
an identifier, a name (alternately: a first name and last name), and a
list of reviews.  A review has an identifier, a movie, a reviewer, and
the contents of the review.  The movie is a movie object.  The reviewer
is a reviewer object.  The contents is a long string.

In something a bit less narrative, I might write the following:

```
Movie
  id: identifier
  title: String
  director: Person
  cast: List of (Person,String) // Represents Actor, Role
  reviews: List of Review

Reviewer
  id: identifier
  name: Name
  reviews: List of Review

Review
  id: identifier
  movie: Movie
  reviewer: Reviewer
  review: String
```

Note that parts of this approach are a bit dangerous, since we see
information duplicated.  Movies link to their reviews and the reviews
link back to the corresponding movie.  There's a chance that things can
get out of synch.  So we *might* design things so that the information
flows only one way.  We'll explore that issue in class.
