---
title: Eboard 04  Ruby, continued
number: 04
section: eboards
held: 2018-01-29
link: true
---
CSC 321.01, Class 04:  Ruby, continued
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Leftover software design topics
    * Compare and contrast three models
    * Key agile practices
    * Agile positives and negatives
* Duck typing
* Debrief on exercises
* Unit testing and `rspec`
* Interesting characteristics of Ruby

Preliminaries
-------------

### Admin

* Apologies for being behind in grading.  I have a busy next 
  few days, but I will do my best to catch up.
* Take a playing card.  It will determine where you sit in class.
    * Why?  I want you to practice discussing things with other
      people.
* Reminder: Please ask your homework questions on the Slack #homework 
  channel.  Context is always helpful on questions.  Not "c9 is not
  working" but "When I try to do X on c9, I get the following error."
* Your mentor will be offering one-hour mentor sessions the night 
  assignments are due.
    * Please fill out the Doodle poll today.

### Upcoming work

* Reading journal due Tuesday at 9pm: [Web technologies](../readings/saasbook2a)
  SaaSbook chapter 2, introduction and 2.1--2.4.
* [Hartl 1](../assignments/hartl-1) due Thursday at 10:30pm.
    * Mentor hours at ...

### Good things to do (Academic/Artistic)

* CS table Tuesday: Spectre and Meltdown (I think)
* CS extras Thursday: Sam's students

### Questions

Models of software engineering
------------------------------

The book covers three models of software engineering.

* Plan and document approaches
    * Waterfall
    * Spiral
* Agile

_What do you see as their similarities and differences?_

* All have client, planning, build, test, maintain
* All have iterations
    * Waterfall: 1
    * Spiral: LONG
    * Agile: Short/small
* Agile just has really small iterations

Important agile practices
-------------------------

_What do you see as the most important agile practices?_

* Strong client involvement; regular feedback from client
    * On current state of project
    * On priorities of what to do next
* Frequent team meetings
    * Daily stand-ups
    * Weekly or bi-weekly planning sessions
* Insufficient documentation
    * (Document through tests rather than text)
* Test-driven development
* Pair programming - We develop better in teams
    * Centrality of communications
    * Cleaner code
    * Can help us follow practices
* "Beautiful code"
    * If you expect to have to come back and change it,
      you develop it differently.
* Focus on the problem at hand, rather than general code.
* Refactor ruthlessly
    * Test-driven development lets you make change.

**All of these interact.**

Why agile?
----------

_Why do our authors (and others) promote agile approaches?_

* Better able to respond to change.
* Plan and documents generally fail.  Incomplete, over budget,
  and more.
    * We need something better
* Agile project generally succeed.
    * But that's because they get to change their requirements.
* Power of involving the client

Why not agile?
--------------

_There are critics of agile.  What might people critique?_

* Less focus on clear documentation (at multiple levels);
  something harder to understand.
* Hard for control freaks.
* Some projects have very specific goals and fairly specific
  deadlines.  (You don't want change.)
* Not all clients are regularly accessible.
* Agile seems best suited for small/medium teams.  You would not
  do agile with 1000 people.
* "You wouldn't build a bridge with agile."
* As a client, you don't know what you're getting for your money.

Duck typing
-----------

OOP has three key principles/practices.

* Inheritance.  We can define a new object/class in terms of an
  existing object/class.
* Polymorphism.  The idea that we can use different things in
  the same situation.
    * Parametric: We can define things like ListOf<T>.
    * Subtype: If A is a B, then we can use an A wherever we
      use B.
* Encapulation.
    * Group state and behavior together
    * Limit access to state

_What object-oriented principles and practices does duck typing support?_

* If it walks like an array and quacks like an array, it must be an arry.
* Duck typing is basically a "casual" version of subtype polymorphism, "If A provides the methods of B, we can use A wherever we expect a B."
* Good for people who understand polymorphism well and don't make mistakes.
* Bad for people who regularly make type mistakes.

Some exercises
--------------

### `sum_to_n?`

```
def sum_to_n?(arr, n)
  bool = false
  if (n.is_a? Integer) == false
    return bool
  end
  arr1 = arr.clone
  for i in 0 ... arr.size do
    for j in 0 ... arr1.size do
      if ((arr[i] + arr[j]) == n) && (i != j)
        bool = true
      end
    end
  end

  return bool
end
```

```
def sum_to_n?(arr, n)
  for i in 0 ... arr.size do
    for j in i+1 ... arr1.size do
      return true if (arr[i] + arr[j]) == n
    end
  end

  false
end
```

```
def sum_to_n? arr, n
  new_arr = arr.combination(2).to_a
  i = 0
  while i < new_arr.length
    if sum(new_arr[i]) == n
      return true
    end
    i += 1
  end
  return false
end
```

```
def sum_to_n? arr, n
    if arr.empty? || arr.length == 1
        return false
    end
    arr.combination(2).to_a.each { |combo|
        return true if sum(combo) == n}
end
```

```
def sum_to_n? arr, n
  return false if n.zero?
  return false if arr.empty?
  arr.combination(2).any? {|x, y| x + y == n}
end
```

### `binary_multiple_of_4?`

```
def binary_multiple_of_4? s
    if s =~ /^[0-1]+$/
        return s.to_i(2) % 4 == 0 unless s == "0"
    end
    false
end
```

```
def binary_multiple_of_4?(s)
  if s == "0"
    return true
  end
  num = s.to_i(2)
  if s == " " || s == "" || s == nil || num == 0
    return false
  end
  if num%4 == 0
    return true
  end
  return false
end
```

```
def binary_multiple_of_4? s
  # Checks that either number is 0 or is valid binary and ends with 2 0s
  return /^0+$/.match(s) || /^[0-1]+00$/.match(s)
end
```

```
def binary_multiple_of_4? s
  return true if s == "0"
  return true if /^[10]*00$/.match(s) != nil
  return false
end
```

Using `rspec`
-------------

_We did not get to this topic._

I'm not sure where we currently stand in terms of experience with
unit test frameworks in our curriculum.

* Did using `rspec` seem like a familiar pattern or something new?
* What did you like or not like about `rspec`?

Interesting characteristics of Ruby
-----------------------------------

_We did not get to this topic._

* Duck typing
* Regular expressions (but help me understand them).
* Huge library of built-in functions
* Metaprogramming
* Introspection / reflection
* Poetry mode
* Yield statement and blocks
    * Sam hates that Ruby has four things that look like functions,
      all with slightly different syntax and semantics.
* Dynamic typing

