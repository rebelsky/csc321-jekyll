---
title: Eboard 02  Getting started with Ruby
number: 02
section: eboards
held: 2018-01-24
---
CSC 321.01, Class 02:  Getting started with Ruby
================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Reflections on the assignment
* Comments on Ruby

Preliminaries
-------------

### Admin

* Please ask your homework questions on the Slack #homework channel.
* Some of you are getting check-minus grades on the assignment.  
    * For assignments, that will still count as a 90.  (You should not 
      get lower than the timebox value, provided that it's clear that
      you've put in an appropriate level of effort and time.)
    * For journals, that will count lower.
* Today is the last day to fill out the data buddies survey
  <https://cerp.co1.qualtrics.com/jfe/form/SV_3UH7q6TmdZ8YRPD>.
  Surveys are more meaningful if we get higher participation.

### Upcoming work

* [Learn Ruby](../assignments/ruby-codecademy) (Due 10:30 pm last night)
    * The three of you who neither submitted it nor submitted a note 
      explaining why it was late will receive late grades.
* [Read chapter 1 + sections 10.1--10.2 of the SaaSBook](../readings/saasbook1)
  (Due 9:00pm THURSDAY)

### Good things to do (Academic)

* Convocation Thursday at 11 in JRC 101: 
  Democracy at the Roots: Culture and Sovereignty in Haiti
* CS extras Thursday: Summer research opportunities in CS.

### Questions

About how long is the typical question response in a journal entry?
  : A paragraph.  So, say, 50-100 words.

Reflections on the assignment
-----------------------------

In reading your responses, I see that there are still some significant
confusions.  We're going to talk through them.

### General comments

* Most of you need to work on clear and precise writing.  Some of you need
  to work on grammar.  While this is not an essay class, I do expect that
  you will write well when you write for me.
* Some of you were worried about the amount of time you spent.  "Approximately 
  five hours" does include six hours.
* Please format your code correctly.

### Chomping and more

Three versions

```
# v1
text = gets
text.chomp!
text.downcase!

# v2
text = gets.chomp
text.downcase!

# v3
text = gets.chomp.downcase

* `chomp` is a pure operation.  It returns a new string.
* `chomp!` is a mutator.  It changes the underlying string.
* `downcase` is a pure operation.  It returns a new string.
* `downcase!` is a mutator.  It changes the underlying string.

Some questions

* What do you think happens if we give `downcase` a string that is
  already lowercase?  Does it give you the same string or a
  copy?
    * A copy.
    * Why?  So that we can change the two independently.
* What value do we get from `downcase!` if the string is already
  lowercase?  It doesn't change the string, but what does it
  return?
    * `nil`.  
    * Why?  Provides a signal to the caller.  The primary goal
      is to mutate the string.  We return nil to say "No changes
      necessary"  We return the string to say "Changed!"
    * Although it may be tempting to write 
      `text = gets.chomp!.downcase!`, you can't.
* Why use strategy 1? (Sequence of side-effecting operations)
    * Might want to reuse
    * Saves memory!
    * Some people like the clarity of "one instruction per line"
* Why use strategy 3? (Chained pure operations)
    * Concise and clear; saves programmer conceptual time
    * May help avoid problems (e.g., I mistyped a variable name)
    * We might actually want all three versions (although this
      form doesn't give it to us)
         ```
         text1 = gets
         text2 = text1.chomp
         text3 = text2.downcase
         ```
* Why use strategy 2? (What the Tutorial uses)
    * A good middle ground.
    * No one really wants the one with the newline.

### Redaction

* Most of you figured out that `gsub` is the way to go.
* But it's complicated.  
* You don't want to use `text.gsub(redact, "REDACTED")`.
    * Why not?
    * The redacted thing can appear *within* a word

```
irb(main):008:0> text = "concatenate those cats, catherine!"
=> "concatenate those cats, catherine!"
irb(main):009:0> redact = "cat"
=> "cat"
irb(main):010:0> text.gsub(redact,"READACTEASDFDA")
=> "conREADACTEASDFDAenate those READACTEASDFDAs, READACTEASDFDAherine!"
irb(main):011:0> text
=> "concatenate those cats, catherine!"
```

_Conclusion: Sam should have been nicer on grading this one._

### Hash tables

```
frequencies = frequencies.sort_by {|a, b| b }
```

* A hash table is an array of key-value pairs (or, more frequently,
  lists of key-value pairs)
* We run a hash function on the key, mod by the table size, and
  add to that bucket in the array.
* Given that hash tables are necessarily stored according to hash value,
  it makes no sense to think of sorting a hash table in place.
* What might `sort` therefore do?
    * We could have a separate sorted list of keys for when we want
      to iterate.
    * `sort` could return a list of key/value pairs that are sorted by
      the key.  (That's what Ruby does)
* Sam thinks that any sensible language would disallow this.
    * Before assignment statement, `frequencies` is a hash
    * After assignment statement, `frequencies` is a list of pairs

### Superclass constructor

* Most of you noted that we can use `super` to call the parent's constructor.
  (You can also use `super` in other cases; it normally means "the procedure
  with the same name in my parent")
* There is one other case in which the parent's constructor is called: If
  you don't define a constructor for the class.

### Reading integers

What do you think about this code?  (Apologies to the author)

```
def get_rating
  begin
    puts "Enter movie rating: "
    rating = gets.chomp    
    rating = rating.to_i
    puts "Please enter a rating between 0 and 10" if rating < 0 || rating > 10
    end while rating < 0 || rating > 10
    return rating
end
```

* We might use `rating = gets.chomp.to_i`.
* The indentation is wrong!
* Uses a structure we don't know.
* Logic issue.  Any non-number will give 0.
* Positive: Nice refactoring
* Potential UI issue: If I enter 3.5, it does not store 3.5 and I 
  don't know that.

### Mixins

_Nope, we didn't get this far.  We might on Monday or Wednesday._

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

This code "fixes" that problem, but introduces another problem.  What is it?

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

This code fixes that problem, but introduces another.  Can you tell what
it is?  (You may not be able to tell from inspection.)

```
Module Action
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

Broader reflections on Ruby
---------------------------

_Nope, we didn't get this far.  We might on Monday or Wednesday_

_Think->Share->Pair_

* What struck you as particularly interesting or confusing about Ruby?
* How do you see Ruby as similar to other languages you've learned?
* How do you see Ruby as differing from the other languages that you've
  learned?
