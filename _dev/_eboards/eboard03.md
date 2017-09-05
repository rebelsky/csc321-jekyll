---
title: Eboard 03  Ruby, continued
number: 03
section: eboards
held: 2017-08-31
---
CSC 321.01, Class 03:  Ruby, continued
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* More reflections on exercises
* Regular expressions
* Duck typing
* Object-oriented programming in Ruby
* Meta discussion
* Q&A

### News / Etc.

* Welcome to day three of CSC 321!  
* Today we conclude our exploration of Ruby and start on Rails.
* Next week, we will mostly explore Rails.
* We will have a visitor for the second half of class on Tuesday.
  Shu-Yang Lin, <http://shuyanglin.com/>.  She will discuss design
  issues and more.
* I'm still working on the course Web site.
* It appears that RubyGems has some vulnerabilities
  <https://www.ruby-lang.org/en/news/2017/08/29/multiple-vulnerabilities-in-rubygems/>.
  I would suggest that you do your devleopment on Cloud 9, rather than on
  your personal computer.
* Thank you to the many of you who submitted your reading journals on
  time.  (Unfortunately, I was reading over algorithms assignments as
  they came in.)

### Upcoming Work

* Do [Rails for Zombies](http://railsforzombies.org/) (Tueday)
* Read [SaasBook, Chapter 4](../readings/saasbook4) (Tuesday)
* Do [The introduction to Rails from SaasBook](https://github.com/saasbook/hw-rails-intro) (Thursday; start before Tuesday)

### Good things to do

#### Academic

* **NEW** Rosenfield Internship Talks, Today at 11 a.m. in JRC 101.
* **NEW** CS Extras today at 4:15 p.m.: Contracts
* **NEW** Writers@Grinnell Reading, Today at 6 p.m. in the Pioneer Bookshop.
* **NEW** Rosenfield symposium, next week.  (Lots of different events)

#### Misc

* **NEW** Tuesday at 11:00 a.m. Community Time Discussion of Discussion
  Across Differences
* **NEW** Tuesday at 11:00 a.m. Strange CLS Harry Potter Event in the
  North Campus Grove

#### Peer

* ???

### Questions

Reflections on exercises
------------------------

For `binary_multiple_of_4?`, here's how I think about it:

A string is a binary multiple of 4 if

Version 0

* The string contains only 0's and 1's.
* AND 
    * EITHER The string is a singleton 0
    * OR The string ends with two 0's

Version 1

* The string is "0"
* OR
   * The string contains only 0's and 1's.
   * The string ends with two 0's.

Version 2

* The string contains only 0's and 1's.
* AND when we convert the string to an integer, the result is evenly divisible 
  by 4.

Comments

* Version 2 is great because it requires little of my thought to understand
  (or to write in Ruby).
* The time complexity of all three should be the same O(length)
* String conversion to integer requires effort, and the effort is not
  necessary.

How do you check if something contains only 0's and 1's?

* Write a loop with a check
  `return false if str[i] != "0" && str[i] != "1"`
* Put that loop into a separate method
         ```
        def only01? str
           for i in [0..str.length] do
             if str[i] != "0" && str[i] != "1"
               return false
             end 
            end
            return true
        end

        def binary_multiple_of_four? str
          return false if not only01? str 
          return str.to_i(2) % 4 == 0
        end
        ```
* Use regular expressions `s[/[01]+/] == str`
    * Side note: `==` is "sensible comparison" not "memory comparison"
      in Ruby, or at least it seems to be for strings.
* Can we improve on
        ```
        def binary_multiple_of_four? str
          return false if not only01? str 
          return str.to_i(2) % 4 == 0
        end
        def binary_multiple_of_four? str
          (only01? str) && (str.to_i(2) % 4 == 0)
        end
        ```
Morals:

* Ruby has a *lot* of things built in.  Learning what is there and
  how to use it is as important as learning the syntax.
* But knowing the Ruby idioms is also useful

Pattern matching

```
def binary_multiple_of_four? str
  (str == "0") || ((s[/[01]+/] == str) && str.endswith("00"))
end
```

Regular expressions
-------------------

* Problem: Represent patterns for pattern matching.  (More generally,
  we want to look for patterns of text in a string.)
* We can write our own instructions.
* Ideally, there are libraries in which you specify patterns and the
  library builds a pattern matcher.
* Church, Kleene, and others developed a language for describing patterns
  (regular expressions) (1930's/1940's). 
* The developers of Unix used those paterns in the design of utilities,
  and they've stuck around since.

A regular expression is one of the following

* Single character, c: Matches one copy of `c`
* A set of characters c1, ..., cn, typically denoted `[pqr]`, matches
  any one of those characters.  Most implementations of REs allow
  ranges, `[a-z]` matches English lowercase letters, presuming we are
  using ASCII or Unicode.
* If R is a RE then  R* (Kleene star) matches zero or more repetitions of R
    * Some implementations of REs allow R+, for one or more repetitions
* If R and S are REs, then RS is a regular expression that matches
  R followed by S `a[pqr]`  `a+[pqr]`
* If R and S are REs, then (R|S) is a regular expression that matches
  R or S.  
     * Generally not included easily.
* There are dialect issues.

Knowing regular expressions in the language you use lets you do pattern
matching "easily".

Plus, recursively defined types are awesome.

Duck typing
-----------

* An important feature of Ruby
* Something about how you define types.
* Includes dynamic (run time) rather than static (compile time, whatever
  that is for Ruby) type checking.
* "If it walks like a duck and quacks like a duck, it might as well be a
  duck." applied to classes and values.
    * That is, even if it's a swimmer in a costume, we can still have it
      do anything we'd have a duck do.
* As long as something implements the methods that you're looking for,
  you can use it.

```
def double x
  x + x
end
```

* What happens if `x` doesn't provide the `+` method?
    * It throws an error
    * Sometimes ... we call the "I can't find the method with this name"
      method associated with `x`.
* Trust the programmer

Object-oriented programming in Ruby
-----------------------------------

* Polymorphism (through duck typing)
* Encapsulation
    * Put values and methods together
    * Hide things from the client
* Inheritance

Encapsulation: Put them in a class

```
class Grinnellian
  def initialize age
    @age = age
  end
  def age
    @age
  end
end
```

Trust the programmer

Inheritance in Ruby

* Can make subclasses.
* Can also do object-based inheritance
    * We can make an object B, that behaves just like A, except in 
      certain situations.
* Good object-oriented programmers find that object-based inheritance
  is as or more powerful than class-based inheritance

Modern object-oriented languages add more features/expectations

* Metaprogramming - You can write code that modifies your objects
  (e.g., declares a field and says that it's a setter or getter)
* Introspection - Not only can you use an object, you can query an
  object for what it can do.
* Mixins - Clever ways of adding functionality that do not use inheritance.
  (Sam thinks of this as a form of metaprogramming.)

Meta discussion (Ways to learn Ruby; `rspec`)
---------------------------------------------

`rspec` is used for unit testing in Ruby.

* Helps me confirm that my code matches the few experiments the designer
  provided.
* Error messages tell you when you haven't met or understood the specs.
* Makes programming more like a video game.
* Observation: There is a way to set things up so that every time you
  save your code, the tests are run automatically.
* If you work with other people, make sure that you run tests before
  you commit to the main branch of the repo (or any shared branch)

Q&A
---

Rails for Zombies!
------------------
