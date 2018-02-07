---
title: Eboard 08  A static site
number: 8
section: eboards
held: 2018-02-07
link: true
current: true
---
CSC 321.01, Class 08: A static site
====================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Notes on your HW
* Discussion: Making homework (more) reasonable
* Start next homework

Preliminaries
-------------

### News and notes

* GitSwag!
* Mentor session 7-8 Sunday night
    * KY recommends that you start the homework in advance.
* Alumni mentors visit next Wednesday.  Please try to clear lunch time,
  4pm for their talk, (and 1pm, if possible).
* The homework has clearly been too long.  I've allocated class time for
  discussing the issue(s).

### Upcoming work

* [Reading journal on user stories](../readings/user-stories) due
  Thursday at 9:00pm.
* [Hartl 5](../assignments/hartl-5) due Sunday at 10:30pm.
    * I need to find a three-hour block to write that assignment.

### Good things to do (Academic/Artistic)

* CS extras Thursday: The evolution of CSC 151
* Rosenfield symposium this week
* MET opera on Saturday.
* Contra dance Friday at 8pm in Younker Lounge.  Live music!
* Two cool shows in the Faulconer.
* Islam week events next week (details forthcoming)

### Good things to do (Other)

### Questions

Notes on your HW
----------------

### Quick notes

* I generally write the homework assignments to get you to think about what
  you are doing and not just copy/paste/run.
* The `LICENSE.md` question was intended to be one of the "Did you read what
  you just copied?" questions.
    * The `README.md` file references `LICENSE.md`.
    * Doesn't that mean you have a responsibility to create `LICENSE.md`
      even if Hartl doesn't tell you to?
    * And is that the right `README.md` and `LICENSE.md` in any case?
    * At what point does ownership switch?

### Refactoring

* My goal was to get you to think about opportunities to refactor.

#### Solution 0

```
class StaticPagesControllerTest < ActionDispatch::IntegrationTest
  
  def setup
    @base_title = "Ruby on Rails Tutorial Sample App"
  end
  
  test "should get home" do
    get static_pages_home_url
    assert_response :success
    assert_select "title", "Home | #{@base_title}"
  end

  test "should get help" do
    get static_pages_help_url
    assert_response :success
    assert_select "title", "Help | #{@base_title}"
  end
  
  test "should get about" do
    get static_pages_about_url
    assert_response :success
    assert_select "title", "About | #{@base_title}"
  end

end
```

#### Solution 1

```
class StaticPagesControllerTest < ActionDispatch::IntegrationTest

  def setup
    @base_title = "Ruby on Rails Tutorial Sample App"
  end
  
  def assert!(page)
    assert_response :success
    assert_select "title", page + " | #{@base_title}" 
  end
  
  test "should get root" do
    get root_url
    assert_response :success
  end

  test "should get home" do
    get static_pages_home_url
    assert!("Home")
  end

  test "should get help" do
    get static_pages_help_url
    assert!("Help")
  end

  test "should get about" do
    get static_pages_about_url
    assert!("About")
  end
end
```

#### Solution 2

```
I have written much DRY-er code on my c9 workspace
```

### Solution 3

"As DRY as I could get it without getting into metaprogramming."

```
class StaticPagesControllerTest < ActionDispatch::IntegrationTest

  def setup
    @base_title = "Ruby on Rails Tutorial Sample App"
  end

  def testResponse (url, title)
    get url
    assert_response :success
    assert_select "title", "#{title} | #{@base_title}"
  end

  test "should get root" do
    testResponse root_url, "Home"
  end

  # Redundant?
  test "should get home" do
    testResponse static_pages_home_url, "Home"
  end

  test "should get help" do
    testResponse static_pages_help_url, "Help"
  end

  test "should get about" do
    testResponse static_pages_about_url, "About"
  end
end
```

### Solution 4

```
class StaticPagesControllerTest < ActionDispatch::IntegrationTest

  def setup
    @base_title = "Ruby on Rails Tutorial Sample App"
    @Home = "Home"
    @Help = "Help"
    @About = "About"
  end
  
  test "should get root" do
    get root_path
    assert_response :success
  end

  test "should get home" do
    get static_pages_home_url
    assert_response :success
    assert_select "title", "#{@Home} | #{@base_title}"
    assert_match "#{@Home}", "#{@Home} | #{@base_title}"
  end

  test "should get help" do
    get static_pages_help_url
    assert_response :success
    assert_select "title", "#{@Help} | #{@base_title}"
    assert_match "#{@Help}", "Help | #{@base_title}"

  end

  test "should get about" do
    get static_pages_about_url
    assert_response :success
    assert_select "title", "#{@About} | #{@base_title}"
    assert_match "#{@About}", "#{@About} | #{@base_title}"

  end
  
end
```

### Solution 5

```
test “combined test” do
  [static_pages_home_url, static_pages_help_url, static_pages_about_url].each do |x|]
    get x
    assert_response :success
    assert_select “title”, /#{@base_title}/
  end
end
```

Discussion: Making homework (more) reasonable
---------------------------------------------

Background

* When I first started assigning Hartl, I did not ask for writeups.  
* My experience was that too many students just typed commands and didn't
  really pay attention to what the steps meant or think more broadly about
  alternatives.
* A portion would also just give up when they hit a roadblock.
* And some wouldn't do it at all.
* So that use of Hartl was a failure.
* But Hartl is *much* better than the code in our textbook, provided
  you pay active attention to what's happening.
* So I added the questions to get you to pay closer attention.
* But "pay attention to Hartl" plus "answer Sam's questions" appears to
  be taking too much time.

What should we do? (Think Pair Share)

* Will working in groups (already permitted) help?
    * Don't force us to work in groups.
    * But allow those of us who want to work in groups
* How many questions is appropriate?
* Make less due
    * Sam will look at the schedule
    * Or at least less "show your work"
* Do we (our successors) need to do chapter 1?
* Stop reinforcing principles
* Do the weirder questions in class, rather than in homework
    * "Be prepared to discuss the following"
* Stretch out the next two homeworks!

Start next homework
-------------------

_Nope, there was not time._

