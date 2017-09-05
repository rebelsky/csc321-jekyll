---
title: Eboard 02  Getting started with Ruby
number: 02
section: eboards
held: 2017-08-29
---
CSC 321.01, Class 02:  Getting started with Ruby
================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Good things to do
    * Questions
* A brief introduction to Ruby
* Some exercises
* Duck typing
* Additional characteristics of Ruby

### News / Etc.

* Welcome to day two of CSC 321!  
* Yes, I will take attendance.
* Today and Thursday, we will continue to explore the wonders of Ruby.
* Your mentor will be giving up some class time to have evening mentor
  sessions (increasingly so as the first half of the semester continues).
* I'm still working on the course Web site.
* Yes, I know the assignments were time-consuming.  But we want you to
  practice getting up to speed quickly.  I'm limiting the work for
  Thursday.
* Some concerns and comments
    * If I'm going to use your reading journals to prepare class,
      I really do need them in on time.  (That's my fault for not giving
      a clear due time.)  They will be due at 8 p.m.
    * When I write "Email your ids for the various services to *the mentor* 
      and to me", that means you should send it to both of us.
    * Please follow the instructions for giving titles to email messages.
      You should know why.
* Reminder: Self Gov your workspace

### Upcoming Work

* [A short reflection on Ruby](../ruby2)

### Good things to do

#### Academic

* Community time today at 11:00 am in JRC 101.
* CS Table today in the Whale Room.
* CS Extras Thursday at 4:15 pm.
* Rosenfield Symposium next week.

#### Peer

* ???

### Questions

A brief introduction to Ruby
----------------------------

* Computer scientists and computer programmers are passionate and
  opinionated about their programming languages.
* Two models:
    * Programming languages are designed to help competent programmers
      get their work done as quickly as possible.
    * Programming languages are designed to help competent programmers
      get their work done as correctly as possible.
* Model two: Think about Java
    * At compile time, Java checks carefully to make sure that what you
      are doing is legal.

        public class Foo
        {
          int foo() { return 1; }
        }
        public class Bar extends Foo
        {
          int bar() { return 0; }
        }
        ...
        public Foo f;
        f = new Bar();
        // Does the object that f refers to have a `bar` method? Yes.
        // Can I use that method blithly?
        System.out.println(f.bar());
   * "Java is your nanny"
* Model one: We know what we're doing.  Having to deal with those complaints
  just slows us down.  (When we want to know about possible problems, we'll
  run a "look for problems" program.)
* Type theory snobbery says: We can protect programmers without getting
  in their way.  But type theory snobs have lost lots of oxygen to their
  brain due to traingle holds.
* Ruby (and much of agile) comes from the "trust the programmer world"
* There are also different paradigms (ways of thinking about how you
  express algorithms): functional, imperative, object-oriented, (declarative)
    * In functional programming - think in terms of functions - as 
      first-class value (inputs to other functions, outputs from other
      functions); functions are pure - given the same input you get the
      same output
    * In imperative programming, we think about explicit sequences of
      steps and the state of the system
    * In object-oriented programming, we think about objects (things
      that have both methods and state) along with three core ideas
      of object-oriented programming: inheritance, encapsulation, and 
      polymorphism.
         * Inheritance lets us define new objects or new classes in terms
           of other objects or classes.
         * Enapsulation lets you deal with the complexities of state by
           hiding the state of your object from your clients.
         * Encapsulation lets you group related things (data and the methods
           applicable to those data) into a single whole.
         * Polymorphism  lets you write general functions (or types) that 
           can be applied to a wide variety of values, provided they meet
           some specification.
             * I can write a `double` procedure that will work with any
               object that knows how to add to elements of the same type.
             * I can write a `HomogeneousList<T>` class that will represent
               homogeneous lists of any underlying type.
             * I can write a `SortedList<T>` class that will represent
               lists that are stored in order from least to greatest,
               provided that T is a class that provides a compareTo(T)
               method.
* Ruby, like most modern languages, embodies/includes all three paradigms.
  Ruby's core umwelt is object-oriented.
* Ruby is interesting, in part, because it has a single primary designer,
  Matsumoto.
* Ruby is *very* popular
    * Programmers like the "I can write what I want, quickly" model.
    * Ruby on Rails.
* Way too multi-expressive.  We have two numbers, a and b.  In the
  cases in which b is strictly larger than a, print "Hello"
    * `if a < b then puts "Hello" end`
    * `puts "Hello" if a < b`
    * `puts "Hello" unless b <= a`
    * `unless b <= a [some syntax that Sam doesn't use] puts "Hello"`
* Wow, that's a pain because it becomes harder to read.  Given four
  programmers, you'll find five different approaches to doing the same
  thing, and that adds cognitive load.
* Wow, that's awesome because it gives you a lot of options and 
  lets you match how you might say things in English
* Lets us match the other langauges we think in.
* More variations - More chance that you'll remember one
    * Or if you're Sam, you'll remember one incorrectly.

Some exercises
--------------

_We will explore the ways in which you solved some of the problems 
from the SaaSbook.  Explain your high-level approach and then the
details._

### `sum_to_n?`

_Define a method `sum_to_n?(array, n)` that takes an array of integers
and an additional integer, `n`, as arguments and returns true if any
two elements in the array of integers sum to n. `sum_to_n?([], n)`
should return false for any value of n, by definition._

Contextual question one: What is `sums_to_n?([2,3],4)`?
  : false

Contextual question one: What is `sums_to_n?([2,2],4)`?
  : true 

Contextual question two: What are some other "interesting" inputs?

What is the time and space overhead of each?

#### Strategy one: Nested loops

* Outer loop: For each index
* Inner loop: For each subsequent index
* Time efficiency: O(n^2)
* Space efficiency: O(n) for the arrays (given to us); O(1) for the
  additional values.

#### Strategy two: Nested loops, with additional stuff

* Outer loop: For each value
* Inner loop: Clone of the array, remove elements, for each
* Time complexity: O(n^2)
* Space complexity: O(n)

#### Detour

* How would you implement array.drop(k), which returns an array like
  the original but without the first k elements?  (If you were in a pure 
  language?  If you were in an impure language?  If you could define 
  the semantics?)
* O(1) or in between or O(n) or worse

##### Option 1

* Create a new array
* Copy over elements
* Space: O(n-k)
* Time: O(n-k)

##### Option 2

* Return something like what you get from `arr+k` in C.
* That is, it refers to a subset of the memory allocated to arr.
* Space: O(1)
* Time: O(1)

#### Strategy 3: 

* Sort the array
* Start at the two ends, moving inward, and checking pairs
* Running time O(sort + n), which is almost certainly O(nlogn)

#### Strategy 4:

* Make all pairs
* Add all pairs
* See if any of them equal the desired sum, using find.
* About two lines of Ruby!
* Making all pairs might by O(n^2)

Code

```
def sums_to_n? arr, n
  arr.combinations(2).find({|x,y| x + y == n})
end
```

This, to me, is like the inner product you should write in Scheme.

Inner product: Given two lists, A and B, of the same length, compute
a0*b0 + a1*b1 + a2*b2 ....

* `(reduce + (map * A B))`

Short code

* Is likely to have fewer mistakes
* May be clearer
* Is likely faster to write
* Makes assumptions about efficiency of underlying operations

### `binary_multiple_of_4?`

_Define a method `binary_multiple_of_4?(s)` that takes a string
and returns true if the string represents a binary number that is a
multiple of 4. NOTE: be sure it returns false if the string is not a
valid binary number!_

#### Solution 1

```
def binary_mutiple_of_4?
  return false if s == "0"
  return s.to_i % 4 == 0
end
```

#### Solution 2

```
def binary_multiple_of_4?
  return false if s.length==0 || s.match(/[^01]/);
  s.to_i(2) == 0
end
```

#### Solution 3

```
def binary_multiple_of_4? s
  last = s.length - 1
  i = 0
  until i == last
    if (s[i] != "0") && (s[i] != "1")
      return false
    end
    i += 1
  end
  return s.end_with?("00")
end
```

#### Solution 4

```
def binary_multiple_of_? s
  n = 0
  for i in 0..s.length
    if (s[i] != '0' && s[i] != '1')
      return false
    end
    n *= 2
    n += s[i].to_i
  end
  return n%4 == 0
end
```

Duck typing
-----------

_Not covered_

Additional characteristics of Ruby
----------------------------------

_Not covered_
