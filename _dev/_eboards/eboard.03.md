---
title: Eboard 03  Ruby, continued
number: 03
section: eboards
held: 2017-01-27
current: true
---
CSC 321.01, Class 03:  Ruby, continued
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* A brief introduction to Ruby
* Some exercises
* Interesting characteristics of Ruby
* Q&A

### News / Etc.

* I realize that there have been some problems getting up and running
  with Ruby and Cloud 9 and everything.  That's to be expected.  
* Journals should generally be submitted by 9pm on the night before
  so that I can read them before class.
* Most of you confirmed that (a) the online tutorial took about five
  hours and (b) it was the best way to learn Ruby.
* Do I need to give a quick lecture on regular expressions?
* I really appreciated the following: *The autograder is good, but the
  prompts could be more specific. It can lead to frustration when it
  isn't clear exactly what it wants. But it's mostly my fault for not
  carefully reading the debug report, which seemed to be quite good.*
* Yes, I'm throwing you in the deep end.  It's a 300-level course.  You
  should have the habits to swim.
* **Friday PSA**

### Upcoming work

* Read and do Hartl, chapter 1.

### Good things to do

* Various dance activities.
* CS table, Tuesday: Planning for the semester.
* CS extras, Thursday: LaTeX.
    * Also session Sunday at 3pm in Math commons

### Questions

A brief introduction to Ruby
----------------------------

* Ruby is a modern programming language: imperative, object-oriented, and
  functional (or at least it has characteristics of each)
* It is primarily object-oriented, in that everything is an object.
* Dynamic.
* "Fun" for many programmers.
* One designer (or one original designer)
* Multiple ways to do any one thing.
* Example of conditionals: TEST + CONSEQUENT
* In C, `if ( TEST ) { CONSEQUENT }`
* In Ruby
        if TEST
          CONSEQUENT
        end
* In Ruby
        CONSEQUENT unless not TEST
* In Ruby
        CONSEQUENT if TEST
* In Ruby
        unless not TEST CONSEQUENT
* In Ruby
        if TEST CONSEQUENT
* Incredibly popular, partially because of Rails.
* Rails makes it "easy" to spin off database-backed Web sites.
* Some of you will hate rails.  "Custom over configuration."
* Lots and lots of libraries.  And an easy system for installing.

Some Ruby exercises
-------------------

*We will explore some of the examples from today's assignment to see
the different ways in which students approached problems.*

### `sums_to_n?`

Write `sums_to_n?(vals,val)` that returns true if any two distinct
values from `vals` (a list of values) sums to `val`.

#### Sol'n 1

    def sum_to_n?(vals,val)
      vals.combination(2).any? do |x,y|
        if val == x+y return true
      end
      return false
    end

* Seems correct.
* Easy to read.
* Running time?  It depends on how combination works.
* May have additional overhead (space or time) for the combination.

#### Sol'n 2

    def sum_to_n?(vals,val)
      for i in 0...vals.length
        for j in i+1...vals.length
          return true if vals[i] + vals[j] == val 
        end
      end
      return false
    end

* Seems correct
* Problem interpretation: What does "unique" mean?
  `sum_to_n?([1,2,1],2)` => `true`
* Worry `sum_to_n?([1,5,3],10)`.  Will it double-add the 5?  No.
  There is sometimes an advantage to using indices rather than a for-each
* Running time?  O(n^2), assuming that getting the ith element of a list
  is O(1).

#### Version 3

    def sum_to_n?(vals,val)
      !!vals.uniq.combination(2).detect { |x,y| x+y == val }
    end

* The `!!` ensures that we get a Boolean
* If our interpretation of unique allows multiple copies of a value,
  this version is incorrect.  Of course, there were no unit tests to
  tell the programmer that they were incorrect, so it's "correct".
    * Black box testing is hard.

#### Version 4

    def sum_to_n?(vals,val)
      !!vals.combination(2).detect { |x,y| x+y == val }
    end

* Fixed!

#### Version 5

    def sum_to_n?(vals,val)
      vals.each do |x|
        if vals.contains(val-x)
          return true;
        end
      end
      return false;
    end

* Correct?  No.  It will double-count.  `sum_to_n?([1,2,3],6) => true`
* Running time?  O(n^2)

### `multiple_of_4?

Write `multiple_of_4?(bitstring)` that takes a string of 0's and 1's
(representing an unsigned integer) as input and returns true if the
string represents an integer divisible by four.

#### Strategy one: Code to the tests.

They need better tests!

#### Strategy two: Convert to integer and mod by 4.

Doesn't work correctly for invalid binary strings.

#### Strategy three: Convert to character array, make sure all 0's and 1's, then convert to a number and mod by 100.

    s = str.split('').each { |ch| return false if (char != '0') and (char != 1) }

#### Strategy four: Use regular expressions

    return str /^([10]*00)|0$/

Write `starts_with_consonant?(str)` that determines if a string
starts with a consonant.

Additional characteristics of Ruby
----------------------------------

*What did you see as important characteristics of Ruby?*

Something interesting and new I have learned about Ruby is the different ways for iteration and how Ruby can identify the type or class of an object based on its characteristics. This is something that is different from Java. Although much of the basics are similar to Java and other Object-Oriented languages, I felt like Ruby was easier to read and comprehend. However, there are many ways to write the same thing in Ruby. 

I am pretty impressed that essentially everything in Ruby is an object. This elegantly solves type-casting problems that plagued some of my Java code. I also found it interesting how all function calls are methods of objects (as demonstrated by the video).

I thought that the unless method was really cool since I haven't found
such a capability in any other languages I've worked with. It seems like
something I would use in the future.

The syntax for regular expressions is painless and very efficient (after
further reading online).

I had never heard of duck typing before, but I like it. Cool concept. 

I found a thing that let me create all my getters and setters in one line and that was really cool. 

I think it is interesting to see that a language is much easier to write than C, Java, or Scheme; with fewer semi-colons, brackets, and )s. I worked with Python over the summer, and I thought the code looked similar to python's code; so it was interesting to see the differences and the similarities with different languages. Something new that I saw, was the unless option, I had never thought about a unless loop and only thought about putting nots in my loops. It got me thinking about other functions that could make code more readable to people that do not know a lot about code.

I liked the idea that an array can contain multiple types because there
were times when this kind of array could have been handy.

Something new and interesting that I've learned about Ruby are blocks and procs.

Something I both love and hate about Ruby so far is the millions of ways they provide to do any one thing. I'm curious about why the language was designed that way, especially if it makes working on someone else's code more difficult.

Q&A
---
