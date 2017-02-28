---
title: Eboard 16  Legacy code
number: 16
section: eboards
held: 2017-02-27
current: true
---
CSC 321.01, Class 16:  Legacy code
==================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Some notes on testing
* Our example, continued

### News / Etc.

* I forgot the clickers.  Maybe Wednesday.

### Upcoming work

* For Wednesday:
    * Wikipedia on UML.  <https://en.wikipedia.org/wiki/Unified_Modeling_Language>
    * Saasbook: 11.2 (Just Enough UML)
* No additional programming assignments.

### Good things to do

* SAAC presentation Tuesday at 11am in JRC 101.
* CS Table, Tuesday at noon: Face recognition
* W. Kamau Bell, Tuesday at 6pm, Harris.
* Prazak Quartet, Tuesday, 28 February 2017, 7:30 p.m., Herrick.
* CS Extras, Thursday at 4:15 pm, Summer Code Camps + PM Students

### Questions

Testing
-------

* "What is it with all these stubs and mocks and doubles and seams?"
* Problem 1: Computer scientists and software developers are inconsistent
  and imprecise in their use of terminology.  (As long as you know generally
  what the terms mean, and the context, you should be okay.)
* Problem 2: Fox and P tend to focus on RSpec, and RSpec changes.
* Testing has a number of chicken and egg problems.
    * Object 1 depends on object 2
    * Object 2 depends on object 1
    * Help!
* Computer scientists have developed a number of techniques to handle
  these issues.
* Basic idea: We make a "stunt double" for the thing we need. (also
  "temporary placeholder" that we can use during development, testing,
  etc.
* You've been using a kind of stunt double: Few serious applications use
  SQLite3
* In an ideal world, languages and frameworks make it easy to create 
  placeholders.
* We need a variety of placeholders.
    * Objects that react to certain methods.
    * Methods that return a useful value, but not necessarily a
      computed value.  (Or not necessarily an efficiently computed
      value.)
* Some variation
    * If our program is running right, *this method* of *this object*
      gets called.
    * We might also want to have a log of how the methods have been
      called / objects have been used.
* Mock: An object that you can create on-the-fly with specified methods.
* Stub: A placeholder method (at least as Sam uses the term)
* Double: The most general term
* Seam: How we replace methods in existing objects.
    * Seams are easy in Ruby.

In Java, how could we create a single object in which the
`foo` method is overriden?

```
class CompactDisplay
{  
   int foo(...)
   {
     ...
   } //
   ...
} // CompactDisplay
```
* E.g., I want to see that when I create a `Podium` and pass in a 
  `CompactDisplay`, the `foo` method is called.
* Here's what the normal code looks like.  `new Podium(new CompactDisplay())`
* I want to write the test code that asks "Does the Podium constructor
  call `foo`?"
* Option 1: Ugly and painful.

```
public class TestCompactDisplay 
  extends CompactDisplay
{
  @override
  public int foo(...)
  {
    alert("Yup, foo was called!");
  }
}
```
* Option 2: Anonymous inner class
```
final bool called = false;
new Podium(new CompactDisplay() { public int foo() { called = true; } });
```

Google "Martin Fowler TestDouble" for a nice short taxonomy.

Example, Continued
------------------
```
class TimeSetter
  def initialize(d)
    @d = d
  end

  def iso8601_ordinal
    d = @d
    y = 1980
    while (d > 365) do
      if ((y % 400 == 0) || (y % 4 == 0) && (y % 100 != 0))
        if (d > 366)
          d -= 366
          y += 1
        end
      else
        d -= 365
        y += 1
      end
    end
    return y.to_s + "-" + d.to_s
  end
end
```

*What smells do you observe in this code?*

* Weird numbers without explanation (400, 365, 366, 4, 1980).
    * Use constants (NAME = VALUE).  In Ruby, things that
      start with a capital letter are assumed to be constants,
      although you can still overwrite them.
    * DAYS_IN_NORMAL_YEAR = 365
* Repeated code (two sections that are d-= NUM and y += 1)
    * Helper procedure
    * Move the y+= 1 elsewhere.
    * Maybe always subtract the 365 and then subtract
      another day in leap years.  (Rethink proram logic)
* Complicated conditionals
    * Write helper methods
    * Some sensible definitions
* Short and unreadable variable names
    * Better names: year and day_of_year
* Complex condition in the nested conditionals
* No comments!
    * Add comments

How would you fix this code?

```
class TimeSetter
  def initialize(d)
    @d = d
  end

  DAYS_IN_NORMAL_YEAR = 365

  def is_leap_year(year)
    return ((year % 400 == 0) || (year % 4 == 0) && (year % 100 != 0))
  end

  def iso8601_ordinal
    day_of_year = @d
    year = 1980
    while (day_of_year > DAYS_IN_NORMAL_YEAR) do
      if (is_leap_year(year))
        if (day_of_year > (DAYS_IN_NORMAL_YEAR + 1)
          day_of_year -= (DAYS_IN_NORMAL_YEAR + 1)
        end
      else
        day_of_year -= DAYS_IN_NORMAL_YEAR
      end
      year += 1
    end
    return year.to_s + "-" + day_of_year.to_s
  end
end
```

Sam's solution

```
class TimeSetter
  def initialize(d)
    @d = d
  end

  # The year Microsoft was founded
  START_OF_TIME = 1980

  def is_leap_year(year)
    return ((y % 400 == 0) || (y % 4 == 0) && (y % 100 != 0))
  end

  def days_in_year(year)
    if (is_leap_year(year))
      366
    else
      365
    end
  end

  def iso8601_ordinal
    day_of_year = @d
    year = START_OF_TIME

    while (day_of_year > days_in_year(year)) do
      day_of_year -= days_in_year(year)
      year += 1
    end

    return y.to_s + "-" + d.to_s
  end
end
```
