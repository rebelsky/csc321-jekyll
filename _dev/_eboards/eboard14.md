---
title: Eboard 14  Software design experiences
number: 14
section: eboards
held: 2017-10-10
---
CSC 321.01, Class 14:  Software design experiences
==================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Introducing alums

### News / Etc.

* Welcome to our Rails mentors!
* Thursday is our wrapup class.  We'll debrief on our learning
  outcomes and you will have chances to evaluate the class.

### Upcoming Work

* No more reading journals.
* [The last programming project](../assignments/last-project) is due 
  next Friday night. (Note change)

### Good things to do

#### Academic/Artistic

* CS Extras Today: Alumni
* CS Extras Thursday: ???

#### Other

### Questions

Intro to alums
--------------

IY

* PHP -> Rails at consulting companies -> Independent consultant
* Wrote a book

CK

* PHP -> Rails -> Misc. Consulting
* Wrote big, semi-popular, not-monitized project

AL

*

How do you approach a new project
---------------------------------

* Look at the tech stack: HTML, HAML, JavaScript + Framework
* What's a stack?
    * Back end
        * Rails
        * Database
        * Gems that offer some functionalit
        * (Technically) Operating system
    * Front end
        * Templating - erb or haml
        * Javascript (e.g., Reach, view.js)
    * Other issues
        * Where do I deploy?
* "There's an add-on for that"
* How much do you use Rails as an API?
* Note: Forms don't work well with React.
* Advice for this class: Do not use an additional framework.
* There are too many front-end options.  None is perfect and you will
  regret what you choose.
* Don't always use the latest technology.  Code stability can be far more
  important.
* Testing
    * What is more important: integration test or unit tests?
    * RSpec plus other stuff (or maybe MiniTest)
    * Note: MiniTest comes with Rails.  RSpec is an extra thing that a
      lot of people.
    * Note: Better to use Capybara within RSpec
    * FactoryGirl for populating the database for your tests

Gems
----

* AwesomeRuby for identifying the right Gem
* Remember to seach
* Look for the ones that seem to be well maintained and followed. 
  If it hasn't been updated in a year.
* Gems are unlikely to do everything you want, but they get you much
  further to get there.
* One issue of gems is picking out the problem that is likely common.
  If you don't know what you're looking for it's hard to find the right
  Gem.
* Most Web applications are 90% common stuff and 10% new stuff.  Get
  Gems for the 90%.
* _Should I just write it myself for learning?_  No, not for client
  projects.  But remember that you can look at the source code for
  gems, or even update the gem to make it do new things.

What's an API?  
----------------

_My project all seems to be front end.  Where will Rails be useful?_

Probably as an API.  Do you know what an API is?

_We know, but would like to hear more._

In a typical all-in-one-application, you have a back end that's the
database and the program logic and such.  You serve up HTML and such.
Your whole stack is right together.

More typically, the front end is somewhat independent and sends requrests
to the database and program logic.  You then return data (e.g., in JSON).
That allows other sites to talk to your site, it allows a Javascript front
end to talk to you.

The API is the URLs you use.

API -> Only pay attention to the M and C of MVC.

API is usually restricted to one small set of features.

How much do you tell your clients about ...
-------------------------------------------

E.g.,

* I had a bug that you didn't know about.
* We have this security flaw caused by my predeccesors.

Answers

* You have an ethical responsibility.
* It probably mitigates future issues.
* If it's really severe - Fix it and tell them.
* It depends a bit about the client.  Some clients want to know everything
  and are more technically involved.  Give them as much information as they
  want.  And help them understand the scope of the issues.
* In real world scenarios, you are talking about money, either directly
  or indirectly.  Lets them figure it out based on cost.
* Do clients understand that sometimes they have to pay for bug fixes?  Yes.
* Postmortems are important.  Blame is not useful.  More ... How do I 
  prevent this from happening in the future.
* Focus on potential impact and steps to fix it.  Good clients are usually
  on board with that.
* Time and work vs. fixed cost.  Can be hard conversations with clients.
    * What about contractors who acted in bad faith?  It's hard being a client.
    * Fixed cost is probably charging twice what they think it will actually take.  
* Under promise and over deliver.

How long did it take until you felt competent with Rails?
---------------------------------------------------------

* A few years. [x4]
* Rails represents a collection of tools that enable very specific
  solutions and that represent a very specific perspective.
* Rails also represents a wide variety of technologies.
* Lots of stuff seems magic.  It's not clear how all of it is working.
  And various things are tied to different technologies.  You just have
  to accept some of it.
* Rails is much higher than any of the things we're doing.

How do you learn a new technology?
----------------------------------

* It depends.  Download and mess with it.  "If I know the questions to 
  ask, I'll Web search them."
* I have no centralized resources.
* Some people like to buy the O'Reilly book and read that.
* Each technology has its own good sources.  Start with the official
  thing.  Go to the site, use the guide and the tutorial.  Cross your
  fingers that its' good.
* Ask programmer friends.
* For Javascript stuff, don't buy a book; they are out of date as soon
  as they are published.
* CHECK THE DATE!
* For Rails, Rails has changed a lot.  Something from 2012 is probably
  too old.  The same is true of StackOverflow.  The Rails Guides on the
  Rails web side are good.
* Set up small goals.
* General: Learn by doing.  Choose small projects.
* It's figuring out the particular details.
* Sometimes doing it in the context of a real project.  A spike.  For
  a limited amount of time, in a branch, we'll try this thing to see how
  it works out in practice.  You almost always throw the spike away.

What are the technologies you use / What should they use?
---------------------------------------------------------

* Still use Slack for communication.
* Big need one: Keep track of what needs to be done and what is currently
  prioritized.  Trello serves that role.  Github has something.  Post-it
  notes on a whiteboard.  Pivotal Tracker (lots of buzzwords).  Pivotal
  is very opinionated.  Keeping track of stages can be important (e.g., 
  Pivotal).
* Deploying code: AWS, Heroku, Docker
    * Docker is a container to put your application in.  Helps you
      avoid server setup.  (How is my application running on the server?
      It explains what to install and such.)  Heroku also does that.
* ScreenHero for remote pairing.
* Macs: The Web development world is a monoculture.  It gives you
  *nix plus commercial apps.
* Integration sever that runs all of your tests before you deploy
  it.  Travis.CI does this.
* Git and GitHub are popular for version control.

Git
---

* Don't use really complicated movements.
* Don't force push until absolutely necessary.
* Don't work on the master branch.
* Be comfortable using branches.  Do all of your work in branches.
  It's easy to merge.
* Understand "the flow".  It's too easy for things to go very wrong.
* "The flow" may depend on the context.
* Important: Merge the master before you push your things back up.
  Treat the master as sacred.  Do small commits.  Do not commit
  once per day.  Being able to roll back a few changes is better.
* Be careful about how long-lived branches are.  You don't want them
  to get too far from the main branch.
* Good commit messages: "wip" is not helpful.
* Use pull requests to encourage someone else to look at your change.
  Get a second set of eyes before you merge into master.
    * That's a good general idea.
* Use good language in your responses during reviews.  Questions are
  also good.
* Maybe do some testing.

Takeaways
---------

* Software development is collaborative.
* Seek out help.
