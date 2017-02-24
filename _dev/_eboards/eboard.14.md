---
title: Eboard 14  Behavior-driven design (BDD)
number: 14
section: eboards
held: 2017-02-22
---
CSC 321.01, Class 14:  Behavior-driven design (BDD)
===================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions

### News / Etc.

* Sam broke the Web site.  Sorry.
* Look over the reading journal assignment for today, but don't do it.
     * If you want to do it to make up for missing a previous reading
       journal assignment, that's fine.
* "Sam, there are all these references to BadSpuds in the SaasBook reading.  
  Do we have to do all of the coding for RottenPotatoes?"
     * No way, no how!
     * But that means you have to spend a bit more time reading code whose
       context is less clear to you.

### Upcoming work

* There is a reading journal assignment for Friday.
* You should also do the Sinatra Hangman exercise in SaaSbook/SPOC for
  Friday.
    * <https://github.com/saasbook/hw-sinatra-saas-hangperson>

### Good things to do

### Questions

Behavior Driven Design

* Idea: Write user stories in a way that both programmers and clients
  can understand.  Run those as tests against your code base.
* E.g., "I want users sorted by first name on the 'list users' page.
  If there are multiple users with the same first name, I want them
  in alphabetical order by last name.  For example ..."
    * We try to run these as tests.
* In order to do this, we need appropriate tools
    * Have the stories independepent of the testing code.  
        * Need to translate from story to code.
        * (Cassie seemed to recmmend this.)
    * Have a system in which the stories are "automatically" translated
      to test code.
* For the automatic system, we need
    * A standard syntax for expressing the parts of the user story
        * As a ROLE, I want to ACTION so that I can GOAL.
    * A way to parse the non-standard parts of the standard syntax
      so that you know what's in the test (Translation of tests to code).
        * Automatic?
        * We write?
        * Both.
    * A library that implements common actions (e.g., "Given these
      values are in the system."  "When the user clicks on the button
      labeled 'Login'")
        * Capybara provides the latter.
    * Underlying testing system
    * UI
* Cucumber (supposedly) provides all of this
* Cucumber and Capybara and Rails can all be used independently
* It looks really simple; the English tests are really nice to write
  and to read.  The parsing stuff gets more complicated.  
* Preset step definitions are sometimes nice.

BDD is a practice

* You are using stories to guide your development.
* You measure progress by the number of stories that pass.
* Important question: "Do my old stories pass?"
    * Too often, adding a new feature breaks something else.
* Good tools show you your progress.
    * Red: Story (or part of your story) does not pass
    * Green: Story (or part thereof) does pass
    * Who cares that Red/Green is the most common form of color blindness,
      affecting approximately 5% of the population?
    * Shoot for green.

Activity

* Find a project that uses Cucumber.
* Try to find the various parts of the Cucumber tests.
* Be prepared to report back on what you found.
* <https://github.com/CSC322-Grinnell/notifications>

