---
title: Eboard 06  An introduction to Rails
number: 06
section: eboards
held: 2018-02-02
link: true
current: true
---
CSC 321.01, Class 06:  An introduction to Rails
===============================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Good things to do
    * Questions
* Version control systems
* Making better use of GitHub 
* Model-View-Controller
* Other rails issues

Preliminaries
-------------

### Admin

* Mentor session Sunday and Tuesday night
* How long did Hartl 1 take?
    * Observation: When things go right, it's reasonable.  But when things
      go wrong, it's really hard to figure out why.
* The Friday PSA will happen in CSC 322
* Don't forget to add yourself to the homework channel!

### Upcoming work

* [Hartl 2](../assignments/hartl-2) due Sunday at 10:30pm.
    * This should take about the same amount of time as the first
      Hartl assignment.
* [Hartl 3](../assignments/hartl-3) due Tuesday at 10:30pm.
    * The response part of this assignment will not be available until
      Sunday (approximately)

### Good things to do (Academic/Artistic)

* Rebecca Wingo: How to Harvest History.  Friday Feb. 2, 4pm, Burling 
  Library Lounge.
    * Workshop: Saturday Feb. 3, 10-1, DLab
    * Register for workshop at <https://grinnell.formstack.com/forms/wingo_workshop>
* Movie Sunday: _I Am Not Your Negro_, 4pm in the Strand
* CS table Tuesday: TBD
* CS extras Thursday: The evolution of CSC 151

### Good things to do (Other)

* Indoor Track and Field Saturday at 9:30 am.
* Swimming Saturday at 1:00 pm.
* Tennis meet Sunday at 10:00 am.
* Posse Plus Retreat Reflections, Community Hour next week (Tuesday,
  11am, JRC 101)

### Questions

Version control systems
-----------------------

* Allow you to keep track of old versions of whatever you are
  writing (usually code).
    * Safe to make changes.
    * Encouragement to describe changes.
    * Ability to see changes.
* Support collaboration.
* Allows others to learn about you.  (The joy of mediocre data science.)
* Good programmers use a version control system to manage the
  complexity of collaboration (and more).
* As you develop as a software designer, you should also develop
  more sophisticated ways to work with your version control system.

Making better use of Git
------------------------

Simplistic view

* `git pull`
* _Make changes_
* `git add .`
* `git commit . -m "asdf"`
* _Make sure the changes work_
* `git pull`
* _Make sure the changes still work_
* `git push`

Improvements to the workflow

* **Make sure the changes work!**
    * Use a tool that checks for you
* Do your work in a branch so that you can have a longer series of steps
  while still being able to commit.
    * Empowers you to work on partial code.
* Add/commit individually (by name) rather than everything.
    * Don't pollute the repo.
    * Don't risk information.
    * Check what files have been added or changed with `git status`
    * Sam prefers that you *never* use anything like `git add .` or
      `git add -A` or `git commit -a`.
* Send pull requests rather than pushing the data.
* These days, Sam does a lot of `git stash save` and `git stash pop`.
* I sometimes find that I need to use `git diff` to recall what changes
  I made.
* Others?

Model-View-Controller
---------------------

_What is it?_

_Why do we use it?_

_How does MVC relate to the three-tier architecture?_

Other Rails issues
------------------

