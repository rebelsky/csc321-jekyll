---
title: Eboard 03  An introduction to software engineering
number: 03
section: eboards
held: 2018-01-26
current: true
---
CSC 321.01, Class 03:  An introduction to software engineering
==============================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Mixins
* Some questions from the reading.
* Service-oriented architecture (SOA)
* Software as a service (SaaS)
* SOA vs. SaaS vs. Cloud
* Models of software engineering
* Important agile practices
* Why agile?
* Why not agile?

Preliminaries
-------------

### Admin

* Take a playing card.  It will determine where you sit in class.
    * Why?  I want you to practice discussing things with other
      people.
* Please ask your homework questions on the Slack #homework channel.
* Please take the journals seriously.
    * Correct grammar and spelling.
    * Thoughtful responses.
    * On the last question, "Explain it in your own words" means 
      "explain the concept" not just "explain your confusion".
    * Example: "I did not fully understand the differences in the different types of testing described on page 70 e.g BlackBox Testing, Regression Testing, etc. The descriptions in the book aren't very informative and hard to understand."
        * Page number: Great!
        * e.g., ... etc.: Shows carelessness.
        * Does not attempt to explain.
* Your mentor will be offering one-hour mentor sessions the night 
  assignments are due.

### Upcoming work

* [Read chapter 1 + sections 10.1--10.2 of the SaaSBook](../readings/saasbook1)
  (Due 9:00pm LAST NIGHT)
* [Read SaaSBook 3.1--3.4](../readings/ruby1) (Due 9:00 pm Sunday)
* [HW2: Ruby adventures, continued](./assignments/ruby-saasbook) (Due 10:30 pm Sunday)

### Good things to do (Academic/Artistic)

* Met Opera Saturday
* CS table Tuesday: Spectre and Meltdown (I think)
* CS extras Thursday: Sam's students

### Questions

Where do I find the videos?
  : We are relying on a MOOC on EdX
  : Sign up for it.  It's Berkeley 169x or something similar.

Ruby reflections resume: Mixins
-------------------------------

Question: Find the total distance a critter has jumped, not
just the amount the critter jumped.

* Can you figure the Ruby involved?
* What does your design look like?  In particular, how did
  you decide to report it?

Why don't I like the following code?  (Apologies to the author.)

```
module Action
  def jump
    @distance += rand(4) + 2
    puts "I jumped forward #{@distance} feet!"
  end
end

class Rabbit
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
    @distance = 0
  end
end

class Cricket
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
    @distance = 0
  end
end
```

Problems

* We've lost the "I've jumped this far" knowledge.  We should
  not have lost that.
* `@distance` is used in the mixin, but not defined in the
  mixin.  This issue is not documented.  Hidden assumptions
  that cross class barriers are hard to track down.  They
  should be rare, even when documented.
* `Rabbit` and `Cricket` have the same internals.  (Perhaps
  we plan to use them differently).  We should probably make
  a superclass.

```
class Jumper
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
    @distance = 0
  end
end

class Rabbit < Jumper
end

class Cricket < Jumper
end
```

The following code "fixes" the primary problem, but introduces another problem.  What is it?

```
module Action
 @@total_distance = 0
 def jump
   @distance = rand(4) + 2
   puts "I jumped forward #{@distance} feet!"
 end
 
 def total_distance
   total_distance = @@total_distance + @distance
 end
end

class Rabbit
 include Action
 attr_reader :name
 def initialize(name)
   @name = name
 end
end

class Cricket
 include Action
 attr_reader :name
 def initialize(name)
   @name = name
 end
end
```

* `@@total_distance` is a class variable.  It is shared by
  all instances.
* If it's shared by all instances, one thing jumping probably
  changes the total distance of another.
* Better testing would have caught this issue.

This code fixes that problem, but introduces another.  Can you tell what
it is?  (You may not be able to tell from inspection.)

```
module Action
  @overall_dist = 0

  def jump
    @distance = rand(4) + 2
    @overall_dist += @distance
    puts "I jumped forward #{@distance} feet!"
  end
end

class Rabbit
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
  end
end

class Cricket
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
  end
end
```

* Doesn't run.

Broader moral

* Ruby mixins aren't quite as nice as you would hope.
* Things that should be simple and "obvious" aren't.

Sam's solution

```
module Action
  def jump
    @distance = rand(4) + 2
    @overall_dist ||= 0
    @overall_dist += @distance
    puts "I jumped forward #{@distance} feet!"
  end

  def total
    puts "I have now jumpted a total of #{@overall_dist} feet!"
  end
end
```

Some shorter questions
----------------------

Note: SOA was the most common question, so I'll leave that to later.

What is synthesis?  Why is it helpful?

* Automatic code generation.  The `attr_reader` above is a simple example.
* Can provide clearer code.
* Can provide more uniform code.
* But can obscure important issues.

Can you explain the different types of testing?

* We'll talk about them on the testing day (and probably elsewhere)

Why don't people just throw away and rebuild legacy code?

* The cost.
* Sometimes they discover that it's harder to build the software than
  they thought.
* And some people do throw away legacy software and start again.
* "Every piece of software feels like legacy software to someone new to
  the project."

Service-oriented architecture (SOA)
-----------------------------------

* Traditional model: All that parts of the application live together
  and interact with each other. 
* That model leads to assumptions about availability of data,
  availability of features, etc. etc.
* Good object design says: Segment with clear interfaces
  (interface: things you can call and meaning of returns)
* SOA: Does this at the larger application level
* N (at least) big advantages
    * Easier to distribute work 
    * Easier to scale
    * Easier to reuse (e.g., Facebook login system)
    * So our services can become services to other applications
* Largest disadvantage
    * Can affect efficiency

Software as a Service (SaaS)
----------------------------

* How your program relates to the user.
* Traditional model: The application runs on your computer.
* SaaS model: The code for the program lives in cyberspace
  and is accessed through your Web browser (typically)
* Great for rolling out updates
* Great for spying on your users
* Not so great as a user if someone decides to cancel the
  "service"

Contrasting SOA, SaaS, and cloud
--------------------------------

* SOA: Software design from the architect's perspective
* SaaS: Where does my program live?
* Cloud: Potentially, a lower-level SOA.  "Storage" and "CPU"

Models of software engineering
------------------------------

The book covers three models of software engineering.

* Plan and document approaches
    * Waterfall
    * Spiral
* Agile

_What do you see as their similarities and differences?_

Important agile practices
-------------------------

_What do you see as the most important agile practices?_

Why agile? (on your own)
----------

_Why do our authors (and others) promote agile approaches?_

Why not agile? (on your own)
--------------

_There are critics of agile.  What might people critique?_

