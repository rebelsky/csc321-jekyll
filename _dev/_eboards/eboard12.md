---
title: Eboard 12  Legacy code and the UML
number: 12
section: eboards
held: 2017-10-03
---
CSC 321.01, Class 12:  Legacy code and the UML
==============================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Detour
* Legacy code
* Code smells
* The UML

### News / Etc.

* We hope that the students who are heading off to conferences have a
  great time.

### Upcoming Work

* [Reading journal for class 13](../readings/design-patterns) due Wednesday night.
    * It's our last reading journal!
* [The last programming project](../assignments/last-project) due next
  Tuesday night.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic/Artistic

* Grinnell Prize Events
* CS Table today
* Wednesday, 5pm, Mary Beth Tinker Talk
* CS Extras Thursday

#### Other

* Plays!
* Sporting events!

### Questions

Detour: Big picture of CSC 321
------------------------------

CSC 321's primary goals are 

* To improve the quality of the software you build
* To prepare you to write the CSC 322 projects - To ground the other ideas
  we talk about in actual code
* At times it feels like a bit of a frankenstein's monster of a course.
  
Today and Friday we focus on ways to help you think and talk better
about program design

I'm talking about UML because of an alum.

Legacy code
-----------

* "Legacy code is code inherited from previous projects"
* "As I understand, legacy code is the type of code which lacks sufficient test coverage to be able to tell if the code that you're going to modify is going to cause any behavioral change in the program, regardless of the author who wrote it or time it was written in."
* "Legacy code is mostly understood as reusable code that still meets a customer need, although its implementation design and structure maybe outdated and needs refactoring. The term “legacy” may imply poorly understood code and can also mean that the code lacks sufficient tests."
* "Legacy code is code that stays in use because it meets a customer need or is critical to the functioning of the project, even though it may be outdated, inefficient, poorly documented, or poorly programmed."
* "My favorite definition of legacy code was any code that doesn't have tests checking its behavior, and therefore cannot be reliably changed as needed. I would personally add a note that while legacy code is likely to be old, poorly structured, or undocumented, that is not necessarily the case. "

If you are going to write code that other people will use

* Document it 3.
* Include tests  1.
* Follow good programming practices  2.
* Follow the code history standards of your organization 4.
* Reflect on the impact on people 0.

Code smells and refactoring
---------------------------

Small group discussions: 

* What do you notice as code smells? (Use your own words; don't worry about
  the book's terms)  
* How do you typically approach them?
* What's a new smell you learned from the book?

What are some smells that your group discussed that you think others
didn't?

* People who don't free memory (we tell by running valgrind or more
  modern tools).  (Untrustworthy programmers.)
* Long chains of method calls.  (A few is okay; more gets rediculous)a
    * Break it into natural parts
    * Name the things
    * Show the explicit flow of control
* Code that doesn't make chronological sense (maybe stuff that's been
  patched in, a declaration in the middle of the code, branching
  in "random" directions.  `goto(random(100))`  Generally, hard to follow.
    * Read through and understand.  "Refactor"
* Doing too many things in one function
    * Split it up into multiple functions that make logical sense
    * Sometimes people just want to get all of their ideas out.
    * Sometimes more efficient to do multiple things at once.
* Clear misunderstanding of the language.
* Lots of parameters - Group into an object or struct
* Magic numbers - Define constants instead.
* Bad formatting.  Reformat.
* Inconsistent formatting - smell for "throw something in and see if
  it works."

Detour: Passing arrays in C
---------------------------

```
int
length (int values[])
{
  return sizeof (values) / sizeof(int);
} // length
```

* `sizeof` generally returns the number of bytes associated with a type.
  The one exception is that it will tell you the number of bytes associated
  with a statically declared array within the same block as that array is
  declared.
* In C, there is NO WAY to compute the length of an array (unless you 
  follow some stupid standard, like putting a sentinel at the end).  Hence, 
  you *must* pass the size of an array along with the array.

How does `free` know how much memory to free?

* There could be a table somewhere that, for each pointer created by
  `malloc`, shows how much memory is associated with that pointer.
* Most implementations of malloc have some hidden memory they allocate
  immediately before the pointer they return.

Code smells example
-------------------

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

* Smells: Bad variable names.  
    * `d` -> `days_since_jan_0_of_current_year`, `y` -> `year`
    * A comment might be better for this.
* No documentation?
* Magic numbers
   * `365` - `DAYS_IN_NORMAL_YEAR`
   * `366` - `DAYS_IN_LEAP_YEAR`
   * `4` - `UM` (or maybe there isn't a better name for this magic number)
   * `100` - `HUH`
* A strange computation: y%400 etc.
* Overly complicated conditionals
        ```
        if (is_leap_year y) && (d > 366)
          d -= 366
          y += 1
        else if (is_leap_year y) && (d <= 366)
        else
          d -= 365
          y += 1
        end
        ```
* Conditionals without alternatives are sometimes problematic.  The
  rewritten version shows that potential problem.
* Repeated code.  In both cases, we're adding 1 to y and subtracting 1
  from d.

```
class TimeSetter
  def initialize(d)
    @d = d
  end

  def self.is_leap_year(y)
    (y % 400 == 0) || ((y % 4 == 0) && (y % 100 != 0))
  end

  def self.days_in_year(y)
    if (is_leap_year(y))
      return 366;
    else
      return 365;
    end
  end

  def iso8601_ordinal
    y = 1980    # The current year.  Microsoft believes time started in 1980
    d = @d      # The number of days since the end of the prior year.  E.g.
                # 1 is January 1 and 32 is February 1.
    while (d > (days_in_year y)) do
      d -= days_in_year y
      y += 1
    end
    return y.to_s + "-" + d.to_s
  end
end
```

Note that the magic numbers did not have to be named and are now much less
magic.  (They also get used only once, which helps.)

The UML
-------

When talking about object-oriented design we want to think about the
objects/classes in our program and how they relate.  Like most of CS,
we should think about static relationships and dynamic relationships.

How do we discuss designs?

* English
* Code
* Pictures 

Pictures can be especially useful, particlarly early on when you want
to make lots of changes/experiments/etc.

Computer scientists and software designers and the ilk like to formalize.
So there were a bunch of "languages" created to describe OO designs.

* Result: A plethora of languages for describing object-oriented design

The software engineering community decided that a single language for
communicating was better.  That's the UML.  But things change, so UML
is changing.

Why use UML or UML-like languages?

* Pictures provide a way to communicate.  Pictures communicate better
  if we have some shared understanding.
    * What goes in the picture.  (E.g., classes, inheritance)
    * How you represent those things (E.g., arrow with open head from
      subclass to superclass represents inheritance)
* People can write programs that let you build diagrams and then
  generate code from those diagrams.

Static

* "This is a class"
* "This is an interface"
* "This class extends this class" (or implements this interface) - is-a
* "This class has these fields (of these types)"
* "This class provides these methods"
* Distinguish between class methods and object methods (and class variables
  and object variables)
* Protection levels of those methods and variables
* "This class is parameterized by subclasses of this class"
* "This class includes objects of this other class" 
* "Each object in this class is included in exactly one object of
  this other class."
* "Each object in this class may be included in more than one object
  of this other class."
* "Each object in this class may send messages to objects in this other
  class."
* ...

Dynamic

* "This is an object in my program"
* "When X event happens, this new object is created"
* "To execute this method, I call the following methods on the following
  objects.  Those objects call ..."
