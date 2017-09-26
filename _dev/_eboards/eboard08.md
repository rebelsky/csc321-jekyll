---
title: Eboard 08  Behavior-driven design (BDD) and Test-driven Devlopment
number: 08
section: eboards
held: 2017-09-19
current: true
---
CSC 321.01, Class 08:  Behavior-driven design (BDD) and Test-driven Devlopment
===============================================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Behavior-driven design (BDD)
* Cucumber basics
* Why test?
* Test-driven development
* An example
* Compare and contrast TDD and BDD

### News / Etc.

* Please let me know when you notice problems on the Web site.  I think 
  I've fixed most of them.
* I'm shuffling the class around a bit today.
* Thursday is a lab day on Cucumber.

### Upcoming Work

* No reading or reading journal for Thursday!  Use the time to work on understanding Cucumber.
* Programming assignment: [Intro rails](../assignments/getting-started-with-rails) (due TONIGHT at 10:30 p.m.)
* Programming assignment: [Cucumber](../assignments/cucumber) (due Tuesday the 26 at 10:30 p.m.)
    * Those working on Python/Django projects may choose to design their own equivalent assignment.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* CS Table today
* CS Extras Thursday - Study abroad

#### Misc.

* Happy Kareoke Fun Time activities
    * Musical, Friday 9pm, Gardner.
    * Workshop: Burn your fear.  Saturday, 2pm.  The Wall.
      Email [improv] to sign up.
    * Workshop: Creating through improv.  Sunday, 2pm.  The Wall.
      Email [improv] to sign up.
    * Musical, Sunday, 7pm, Gardner

### Questions

Behavior-driven design (BDD)
----------------------------

_What are the core ideas?_

* Work with user stories.
* Add behavior that corresponds to the story.
* Concentrates more on what the user sees than the underlying code.
* Often: Automated/programmatic

_What else do you note?_

* Wow.  It's verbose.  It includes the user stories.

_Why?_

* Flexible, high-level approach to ensuring that our program does what
  it's supposed to do (from the client perspective)
* Accessible to our client - User stories are how we communicate with
  the client.  We should therefore have a programmatic way to verify
  that we have met the client needs.
* More specific descriptions are better
     * "Easier to code"
     * Closer to what the client wants
     * Helps us communicate

_Example?_

* As a typical Grinnell student, to stay awake in the morning, I need to 
  be able to buy coffee from the machine.
    * When I go to the coffee machine and put in a quarter and press the
      "Joe, Please" button, a cup appears at the bottom filled with 
      six ounces of coffee.
    * When I go to the coffee machine and put in a quarter and put my
      mug under the spout and press the "12 oz" button, 12 oz of
      coffee are added to my mug.

Cucumber basics
---------------

BDD is an important enough concept that people have built tools to
help with it.  In Rails (and elsewhere) one of the popular (or formerly
popular) BDD tools is called Cucumber.

_What is the core idea?_

* BDD stuff can (and should) be automated.

_What things are involved in a Cucumber test?_

* Feature file: User story + Setup for scenarios + List of scenarios
* Step definitions - Turn the scenarios into calls to your Ruby code.
  Something like, regular expression + List of instructions
* Libraries
    * Capybara - A library that provides backing for step definitions for 
      Web stuff.
* The code you are testing.
* Bridge code

Why is there so much crap involved?

* To separate what is custom from what is general.
* Because there is a lot general implemented for you already.
* Problem: To do/test X, you may have to look at a, b, c, and d.

Scenarios

```
Feature: Invites

 Scenario: Accepting the invitation
    Given I sign in as "Mary Jane"
    And I visit the invitation page
    And I click the "Accept invitation" button
    Then I should be redirected to the group page
    And I should see a notice telling me I have access
```

```
@javascript @mobile
Feature: Visit the landing page of the pod
  In order to find out more about the pod
  As a user
  I want to see the landing page

  Scenario: Visit the home page
    When I am on the root page
    Then I should see "LOG IN"
    When I toggle the mobile view
    And I go to the root page
    Then I should see "Welcome, friend"

    When I am on the root page
    And I am not logged in
    Then I should see "Welcome, friend"
    When I go to the mobile path
    Then I should see "LOG IN"
```

Step Definitions

```
#citation: https://github.com/diaspora/diaspora/blob/master/features/step_definitions/posts_steps.rb

Then /^the post should be collapsed$/ do
  first_post_collapsed?
end

Then /^the post should be expanded$/ do
  first_post_expanded?
end
```

Why test?
---------

_Why is testing important?_ (Three minutes with your partners.)

* "Verify" that our code works
    * For ourselves
    * For our clients
    * Edge cases
* Make us comfortable changing code
* Video game! - Fixing tests gives you a concrete set of progress.
* Documents expectations
* Helps us think about our goals
    * Edge cases
* Your company or pointy haired boss may require it
* Some testing strategies require you to think broadly about your code,
  not just what individual procedures do but how the procedures intereact
  and their effect on the final user interface.
* Tests help you write your code - keep you focused.
* May make others more confident in using your code; may make you more
  confident in sharing your code.

Test-driven development
-----------------------

_What are some core concepts?_

* Conceive of coding through testing
* Write tests before you code.
    * Some models are very extreme -
    * Sam generally believes in
        * Write lots of tests, including edge cases
        * Write code
        * Go back and add tests
* Continuous testing - Prefer that tests are run automatically
    * Each time you modify
    * Each time you commit (as a precondition to committing)
* "It it's not tested, it doesn't exist."
* Test coverage

An example
----------

Sometimes we write tests retrospectively.  (But we can also think of them
prospectively.)

Here's an example from the book (or a variant thereof) that I like.

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

_What does this code do?_

* Provides a way to represent/store days as integers and use them
  in other ways.
* The `iso8601_ordinal` procedure provides a string of the form
  "YYYY-DD", where DD is the day of the year using 1 based indexing.
* Assumes no dates before January 1, 1980 are of value.

_Why is the getter called `iso8601_ordinal`?_

* It's a formal name for YYYY-DDD.
* Standards exist; there's a reason to use them.
* XKCD suggests YYYY-MM-DD

_What tests would you write?_

Input -> Output

* 0 -> "1980-0" - NO.  Don't test things that do not make sense.
* 1 -> "1980-1".
* 365 -> "1980-365".
* 366 -> "1980-366" if 1980 is a leap year
* 367 -> "1981-1" - edge case, right after a leap year
* Check for Y2K bugs!
  (+ 366 365 365 365 ...) + 1 => "2000-1"
* An "average" date -> 2006, 1997

_Do you see any obvious bugs?_

* Whoops.  It doesn't work on the last day of a leap year.  Maybe
  they should hve written clearer code.

```
    while (d > days_in_year(y)) do
      d -= 366
      y += 1
    end
```

TDD and BDD
-----------

_What are some similarities?_

_What are some differences?_

