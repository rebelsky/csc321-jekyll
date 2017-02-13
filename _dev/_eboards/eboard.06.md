---
title: Eboard 06  A static site
number: 6
section: eboards
held: 2017-02-03
link: true
---
CSC 321.01, Class 06: A static site
====================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
* Assorted questions
* Yielding

### News / Etc.

* Don't be afraid to ask for help!  (From me, from your classmates, from
  Adam, from the Interweb.)
* Office supplies in the commons.  Free will donations.
* I realize that some of you will leave class early today to meet with
  a client for CSC 322.
* Please let me know ASAP if you notice things missing from the Web site.
  I'm still getting up to speed on Jekyll.

### Upcoming work

* [SaaSbook, chapter 1 and sections]({{ site.baseurl }}/readings/saasbook-1).
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.07).
* Finish [Hartl, Chapter 3]({{ site.baseurl }}/assignments/hartl-3).

### Good things to do

*Nope, no extra credit.*

* CS Table, Tuesday, 7 Feb 2017.  Something on privacy.
* Scholars Convocation, Thursday, 9 Feb 2017, 11:00 a.m., JRC 101.
  David Orr: *Climate Change and the Crisis of American Democracy*.
* Thursday extras, Thursday, 9 Feb 2017, 4:15 p.m., Science 3821: 
  Gary Meyer: Image-based rendering and yadda yadda yadda (visitor 
  from UMN).

### PSA

* I care about you.
* Take care of yourselves and each other.

Potential questions to discuss
------------------------------

I know we had to write about `yield`, but can we talk about it, too?

Can we talk about what REST is? it's mentioned briefly in the reading
and I remember someone telling me about REST objects in React, but I
don't really understand it.

Can we go over the basics of html? I never really formally learned this
language (except for a few weeks in 11th grade).

I would like to discuss `.erb` files more in class, and interesting 
things that you can do with them.

I really hope we can talk about the exercise questions for 3.4.4 tomorrow
in class.  (Testing for root route).

How the config/routes.rb file works.  I'm not really sure why we need
to change config/routes.rb everytime. What is the definition of a route?

In class I think we should talk about how/why/when yield is preferable to a function call

Could you explain the rails db:migrate command? 

I’d like to discuss the generic code for making the home, help, and
about page.

I would like to discuss when it is appropriate to use the rails'
`generate` command, compared to when it is more apt to simply create
all the controllers and files by hand.

Questions with quick answers
----------------------------

I don't know that this needs to be discussed in class, but I'm still
rather confused about where to go to find certain parts of code (what
files) and how to know what to enter. I assume I'll gain that information
as I continue doing the readings/exercises, but maybe a broad idea of
what's happening when we write something would be beneficial.

> Practice.

> Grep, Find.  (Unix utility to search files.)

> Bingle.

> Stack overflow.


Can Ruby be embedded in most places with HTML blocks?

* Yes, provided the file is marked as an erb file.
* We will consider another markup system, called haml, which has a different
  kind of embedding.

Is there a better way to create the new files and attach them to the
routes file? It seemed that we were doing extra work by creating a
file (either manually or with the touch command) and then adding it to
the routes.

* We will eventually work on writing general routes.

Questions we will cover later in the course
-------------------------------------------

The chapter introduces the concept of testing. In this section we only
reached the basics of making a test suite, but something worth discussing
would be how do you know what to test for? Also when is it appropriate
for your intended audience to begin testing the product? (For instance
trying to figure out the computer knowledge of the average mayflower
resident to ensure usability to the client.

* We will explore behavior-drive design (BDD) when we do test-driven 
  development.

I'd like to discuss the benefits/drawbacks of doing TDD (test-driven
development)

* We will cover that a week or two.

One thing that I would like to discuss more in class is testing.

* We will cover this later.

I would like to discuss testing and the cycle that is used. 

* We'll get to that in a week or two.

I think going through the automated testing part, and how that works in Ruby; and talking about why automated testing is important and how it works in general will be interesting.

* Yup!  Wait a week or two.

I want to discuss about the test. This chapter taught us about Guard. I
know it is a very convenience tool that we can use it to automate
the running of the tests. And Guard monitors changes in the file
system. However, in the book it mentions that there is an interaction
bug between Guard and Spring. I am very interested in this and would
like to see some examples and wish we can discuss about it.

* We will cover this later.

To be honest, I got pretty lost by 3.6.2 about what we were actually doing with the Guard file, and what the Guard file actually is for. If this is important, I would like to know more.

* Not essential right now.

I would like more information about the optional action items that can
be added onto a generate controller command.

* Manual pages help

Yielding
--------

* It turns out that it's really useful to pass "code blocks" as parameters
  to other procedures.
* Example: If we're writing a generalized sorting algorithm, we want to
  pass in a procedure that compares values.
* Example: If we want to conceal some internal design issues, we might
  want someone to pass in a procedure that does someting with our values.
    * Iterators
* Language designers need to find ways to accommodate this desire.
    * PM: "In a type-safe way."
* Multiple issues in the design:
    * Follows conventions
    * Easy for programmers to express
    * (Maybe I'm too lazy to look at what others do.)
* Multiple semantic issues, most of which I will get wrong.
* Passing code in Ruby
    * Pass blocks as parameter / yield
    * Pass functions as parameter / lambda
* Suppose we are writing an iterator for an array (and they don't
  exist already).
    * stuff.each (...)a
    * We're passing in something you want to do to each (maybe a
      procedure)

        for (i = 0; i < arr.length; i++) 
          {
            fun(arr[i]);
          }

    * Another perspective: We are yielding control to another piece
      of code.

        for i in 0..arr.length
          yield arr[i]
   
    * In effect, `yield` is the generic name for the parameterized 
      block that is passed in to our procedure.

*

        def whatever
          i = 0;
          arr = [4,1,2,7,6]
          while (i < arr.length)
            puts (yield arr[i])
            i = i + 1
          end
        end
