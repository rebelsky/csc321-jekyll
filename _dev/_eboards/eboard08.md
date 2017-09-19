---
title: Eboard 08  Behavior-driven design (BDD) and Test-driven Devleopment
number: 08
section: eboards
held: 2017-09-19
current: true
---
CSC 321.01, Class 08:  Behavior-driven design (BDD) and Test-driven Devleopment
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

### News / Etc.

* Please let me know when you notice problems on the Web site.  I think 
  I've fixed most of them.
* I'm shuffling the class around a bit today.

### Upcoming Work

* No reading or reading journal for Thursday!  Use the time to work on understanding Cucumber.
* Programming assignment: [Intro rails](../assignments/getting-started-with-rails) (due TONIGHT at 10:30 p.m.)
* Programming assignment: [Cucumber](../assignments/cucumber) (due Tuesday the 26 at 10:30 p.m.)
    * Those working on Python/Django projects may choose to design their own equivalent assignment.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* CS Table today
* CS Extras Thursday

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

_What is the core idea?_

Cucumber basics
---------------

_What is the core idea?_

_What files are involved in a Cucumber test?_

Cucumber samples
----------------

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

_Why is testing important?_ (Three minutes with your pratners.)

Test-driven development
-----------------------

_What are the core concepts?_

_How does what you read about testing relate to your experience testing previously?_

TDD and BDD
-----------

_What are some similarities?_

_What are some differences?_

An example
----------

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

_Why is the getter called `iso8601_ordinal`?_

_What tests would you write?_

_Do you see any obvious bugs?_

