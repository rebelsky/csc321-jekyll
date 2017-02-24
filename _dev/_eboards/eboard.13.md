---
title: Eboard 13  Software as a service
number: 13
section: eboards
held: 2017-02-20
---
CSC 321.01, Class 13:  Software as a service
============================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* DRYing out your code

### News / Etc.

* I know that there is a planned student protest on March 1.  I will still
  hold class, but I will not penalize you for missing class.
* Sorry about Friday's class.
* Note for next semester: Sam should rearrange.

### Upcoming work

* Read SaaSbook chapter 7 on Behavior-Driven Design for Wednesday.
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.14)
  due Wednesday.
* Sinatra Hangman exercise from chapter 2 of the SaasBook for Friday.
  (It should be in "Intro to BDD, TDD, and SaaS" on the MOOC.  I'll work
  on getting links updated tonight.)
* There was no reading journal for today.  Sorry.

### Good things to do

*Nope, no extra credit.*

* Executive debate for SGA elections.  Thursday 8pm JRC 101.
* CS Table, Tuesday, 21 Feb 2017, noon: Net neutrality.
* Women in CS, Tuesday, 21 February 2017, 7pm
* CS Extras, Thursday, 23 February 2017, 4:15 pm: The future of MathLAN

### Questions

DRY
---

* It means: "Don't Repeat Yourself."
* Why is this an important principle?
    * Only fix or improve code once
    * Often makes the code cleaner and easier to read.
    * Can improve efficiency or locality (less code means it is more
      likely to stay in the cache)
    * Makes programmers more efficient

### What are techniques we know to help us avoid repeating ourselves?

#### Write functions instead of writing the same code multiple times.

    (define irgb-flatten
      (lambda (color val)
        (irgb (* val (round (/ (irgb-red color) val)))
              (* val (round (/ (irgb-green color) val)))
              (* val (round (/ (irgb-blue color) val))))))

    (define component-flatten
      (lambda (component val)
        (* val (round (/ component val)))))

    (define irgb-flatten
      (lambda (color val)
        (irgb (component-flatten (irgb-red color) val)
              (component-flatten (irgb-green color) val)
              (component-flatten (irgb-blue color) val))))

    ; And yes, we could improve this even more
    (define irgb-flatten
      (lambda (color-val)
        (apply irgb (map (section component-flatten <> val) 
                         (irgb->list color)))))

Another example

    // Volume of prism one
    prism1vol = prism1width * prism1height * prism1depth;
    prism2vol = prism2width * prism2height * prism2depth;
    prism3vol = prism3width * prism3height * prism3depth;
    prism4vol = prism4width * prism4height * prism4depth;

    int
    volume (int width, int height, int depth)
    {
      return width * height * depth;
    } // volume

    prism1vol = volume (prism1width, prism1height, prism1depth);
    prism2vol = volume (prism2width, prism2height, prism2depth);
    prism3vol = volume (prism3width, prism3height, prism3depth);
    prism4vol = volume (prism4width, prism4height, prism4depth);

I think that's more readable.  What is evidence that it's not DRY?

* It doesn't look DRY.  (It looks WET.  Weirdly Excessive Typing.)
* Sam wrote it by copy-and-paste.  Copy-and-paste is generally a sign
  that you are not writing DRY code.

How would you dry out that code?

Idea 1: We should be using objects or structs to represent prisms
(prismi?).

Idea 2: We could use a list or array along with a for loop.

    for (int i = 0; i < prisms.length; i++)
      {
        prismVol[i] = volume (prismWidth[i], prismHeight[i], prismDepth[i]);
      }

    for (int i = 0; i < prisms.length; i++)
      {
        maxDim[i] = max (prismWidth[i], prismHeight[i], prismDepth[i]);
      }

We could dry out this repetition using lambdas and/or iterators

    prismVol = prisms.map { volume }
    prismMaxDim = prisms.map { max }

### Repetition

   print (1);
   print (2);
   print (3);
   print (4);
   print (5);
   print (6);
   print (7);

   for (i = 1 ; i <= 7; ++i)
     {
       print(i);
     }

### Detour

Is there a difference between

   for (i = 1 ; i <= 3; ++i)
     print (i);
   // 2 3

and

   for (i = 1 ; i <= 3; i++)
     print (i);
   // 1 2 3 

How does a for loop work?

   for (init ; check ; increment)
     body

1. init.  In both cases, i is 1.

2. check.  In both cases, i is <= 3.

3. body.  Both print 1.

4. increment.  In both cases, i is 2.

5. check.  In both cases, i is <= 3.

6. body.  Both print 2.

7. increment.  In both cases, i becomes 3.

8. check.  In both cases, 3 <= 3.

9. body.  Both print 3.

10. increment.  In bothc ases, i becomes 4.

11. check. In both cases i ! <= 3


Is there a difference between

   i = 5;
   x = i++;
   // i = 6, x = 5

and

   i = 5;
   x = ++i;
   // i = 6, x = 6

### Quick review

* Functions to extrract common components
* Arrays + Repetition
* Repetition
* Iterators
* HOP

### How else?

* Generics, for languages that support them.  Rather than writing the
  same code again and again for different types, you just write one
  set of generic code.
* Libraries: Don't reinvent the wheel (unless it's a bad wheel).
* Interfaces and polymorphism.
    * Write code that works with similar objects, even if they are
      different types.  (Works well with duck typing.)
        * If it walks like a duck and squawks like a duck, it must
          be a duck.
        * I can write a sorting routine for anything that provides
          a compareTo method.
* Inheritance.
    * Don't reimplement the methods of your parent
* Global constants.
    * PI, rather than 3.14159
    * MAX_ARRAY_SIZE rather than 128
    * BIGNUM rather than 128
* Ruby's yield and blocks (a kind of HOP)
* Ruby's funky repetition statements, like 5.times
* Ruby's metaprogramming (e.g., for getters and setters)
* Ruby's mixins

Use these techniques as you go.  Pay attention to non-DRY code, and use
one or more to DRY your code out.
