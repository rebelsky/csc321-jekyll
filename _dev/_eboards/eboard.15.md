---
title: Eboard 15  Test-driven development (TDD)
number: 15
section: eboards
held: 2017-02-24
---
CSC 321.01, Class 15:  Test-driven development (TDD)
====================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Your thoughts about TDD
* Why test?
* Looking ahead: An example to consider

### News / Etc.

* I've seen two different guidelines on when this class runs.  One
  guideline says that it's the first seven weeks of the semester.  The
  other says that it's until spring break.  Do you have preferences?
  (I will also ask CSC 322.)
* I'll probably continue some of today's topics on Monday, particularly
  your various questions.

### Upcoming work

* For Monday, read SaaSbook Chapter 9 and sections 10.4-10.9
  (Yes, there is a writing journal.)
* If you have not completed the Sinatra homework, continue working on it.

### Good things to do

* Diving today at 2pm.
* Jazz band tonight at 7:30 pm.
* Screenagers documentary, 10 am, Saturday, Strand
* Met Opera Live in HD showing of _Rusalka_, Saturday, Feb. 25.
  Talk 11:30-noon, opera noon-3pmish.
* Diving tomorrow at noon.
* CS Table, Tuesday at noon: ???
* W. Kamau Bell, Tuesday at 6pm, Harris.
* Prazak Quartet, Tuesday, 28 February 2017, 7:30 p.m., Herrick.
* CS Extras, Thursday at 4:15 pm, Summer Code Camps

### Questions

Test-driven design: Your comments
---------------------------------

*How does Fox and Patterson's presentation of test-driven development
compare to your prior experiences with unit testing?*

This is a much more detailed and complicated presentation of TDD compared to my own experience. And honestly I think my only experience with unit testing is just from the Hartle book. I don't think I have experienced a lot though.

Usually I've written unit tests after I write code. Unit tests are usually things I come up with by thinking to myself "what could I do to stress out the program and make it fail?" TDD is more about thinking about user stories and then applying a testing method to check to make sure a program does what it is supposed to do in a given context, which we do before we write the code. Also with TDD you focus on writing just enough to make it pass the test, rather than using testing to root out bigger problems like with unit testing.

Unit testing, as I have done it, usually requires that code be written first, and that tests be written for each part of the code that needs to be tested. However, TTD writes the tests first without having written any code. The logic for this seems to be so that you know immediately when your code does not do what you expect of it, and it can help guide and structure how the code will be written.

Fox and Patterson's presentation of test-driven development are similar to my prior experiences with unit testing in that both include writing tests for small testable parts of an application. Also, in both cases, you would write small tests for general and corner cases. They differ in that TDD asks to write failing tests first, then write code to make the test pass. However, my prior experiences with unit testing included writing code first then writing tests to see if my code worked. TDD, according to Fox and Patterson, drives the code which is different than my prior experiences with unit testing. 

*What do you see as the most important or enduring concept in this
chapter overall?*

Testing seems the most important seeing as most of the sections are about testing.

It is telling you how to use spec to write tests. 

The enduring concept to me is developing a testing method that works and knowing when to start, when to stop testing, and what the goals will be along the way. The beginning of the chapter was more about using TDD and writing tests early. Then it became more about writing good tests and then more about finalizing the testing procedure.

Having good tests is very important because software projects might be big and staying on track of all the details might be hard. Doing testing first helps us to organize our thoughts, envision software better and saves a lot of time in the future because we can check our code as we go. For these reasons the authors emphasize the importance of testing and go into details into how to write good tests. 

Most enduring concept is how to construct tests and then passing tests in the fewest lines possible and then refactoring

That even though TDD may seem backwards and more work, that in reality, TDD is more efficient and leads to more clear, concise and bug-free code in less time than non-TDD. I really need to get used to writing tests before writing code, especially for CSC322.

The most important or enduring concept of this chapter was testing. Writing FIRST (fast, independent, repeatable, self-checking, and timely) tests are very important in driving quality code.  Learning different tests and testing techniques is important to writing great code. 

Usually my practices are pretty far from a test-driven development format when writing code. It is usually unlikely that I have enough of an idea about what I need to do to solve a given problem at the start, and I therefore find it difficult to begin writing tests before actually writing any code. If I were more familiar with rails and had more experience programming in situations like this, I think that test-driven development would be a good way to save time and to write good code from the start.

Fox and Patterson's presentation of TDD is more formally defined than my past experiences with unit testing. All I have done has been carefully chosen test that covered the range of reasonable circumstances I thought could have arisen with my code. These tests were typically written before the code and were made to pass. In that regard, my experience with testing is very similar. However, I have never seen testing as formally stated (with as many diagrams and flowcharts) as Fox and Patterson do. For example, I have done the Red-Green-Refactor model before without knowing that was what people called the process.

*What do you see as the relationship(s) between BDD and TDD?  Which
do you prefer?*

BDD is kind of like a subset of best practices for TDD. I like TDD because I like how it incorporates user stories into testing. I like this practice because I think it is very rooted in what something that is easy to understand and simplistic. I think that with some of the more abstract thinking that is necessary for software development, having parts of the process that are very rooted in these important use cases seems reasonable and helpful. I prefer BDD because it employs some ideas and concepts that I think are useful. For example, I think it is good how BDD focuses on the behavior of a program rather than specific functionality. I think that although this could arguably lead to buggy code it would also lead to programs that do what they are supposed to do.

BDD looks at the behavior of the code in general while TDD looks at the specific small parts of the code. I think BDD and TDD can go along well because TDD will ensure that small details of the code are correct while BDD will ensure that program behaves correctly.

Similarities between BDD and TDD are that tests are one of the first things written to help check code. However, with TDD, tests come before code. Like BDD, TDD is done with the intent to know immediately if app code is working as expected/desired. Due to my dislike of "breaking" tests by tricking them into thinking that code exists, I prefer BDD. BDD also gave the impression of being more client-oriented, meaning tests were based off of stories.

Both BDD and TDD help the programmer ensure a project that meets the needs of their clients BEFORE they start programming at all. This seems to be an expansion on Weinman's favorite adage: "Hours of coding can save you minutes of planning" I like behavior driven design more because I like interacting with our clients and because I remain unconvinced that it is helpful/good to write all these tests before you have any code in your program. 

BDD seems like the corporate thing your boss makes you do and that nobody really likes. This is mostly coming from hearing  horror stories about cucumber. But in general, I  would rather write my tests in code rather than in pseudo English that might not work. TDD seems like a fun way to develop, but it seems like maybe it could be gamed by writing bad code on purpose that still passes tests. 

I think in this part the most important concept from the chapter was the idea of making sure that you have complete coverage of the tests.

Why test?
---------

What are some important reasons we use testing?  (Three minutes with your
partners.)

An example
----------

Sometimes we do retrospective testing.  Consider the following code.

```
class TimeSetter
  def initialize(d)
    @d = d
  end

  def self.iso8601_ordinal
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

What does this code do?

What tests would you write for it?  
