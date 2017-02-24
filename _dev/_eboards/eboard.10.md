---
title: Eboard 10  Extending your Rails application (1)
number: 10
section: eboards
held: 2017-02-13
---
CSC 321.01, Class 10:  Extending your Rails application (1)
===========================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Accessibility
* Important Web technologies and their roles
* Lab time

### News / Etc.

* Food!
* Warning!  Friday the 13th falls on a Monday this month.
* I'm working on getting some grading done.  Soon!

### Upcoming work

* Hartl, Chapter 6 due Wednesday.  (Do as much as you can within your time box.)
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.11)
  due Wednesday.

### Good things to do

*Nope, no extra credit.*

* CS Table, Tuesday, 14 Feb 2017, noon: Slots, Whales, Etc.
* Thursday extras, Thursday, 16 Feb 2017, 4:15 p.m., Science 3821: 
  4-1 Program with UIowa.
* Senior day for basketball on Saturday.
* Swimming and diving this weekend.
* Orchestra Saturday.

### Questions

Accessibility
-------------

* Responsibility to make our sites accessible to people who do not have
  the same abilities or resources as we do.
    * Limited vision
    * Limited mobility
    * Different languge skills
* As an institution of higher education, we have a *legal* responsibility
  to make our sites accessible.
* We also have a *moral* responsibility to make educational materials
  accessible.
* *Three minutes to chat or Web search or both.*
* Note: Lots of people in FOSS communities talk about a11y and i18n.
  (accessibility and internationalization)
* Note: Sam left out other issues, some of which may be applicable to our
  projects.
    * Limited Internet access (or technology access)
    * Limited technical skills
* Caption videos.  (Manually!)
    * Narrate/describe videos.
* Use multiple languages / let the user choose.
    * Make it easy to choose / set.
* Make sure that colors contrast, both for the color blind and those with
  less good eyesight.
    * There are tools that let you check your Website as viewed by those
      with different color vision.
* Think about physical setup.
* Google says to use the Bootstrap accessibility plugin
* How do you support the illiterate?
    * Explanatory images
    * Ask them to have screen readers (how do you support them?)
* Design of screen readers.
* Clear text for "click here".  E.g., "Our help page"
    * And think about when you might be repeated text.
* Provide good alt text for all of your images.
* Low requirements.  Don't expect them to have good graphics cards to
  load your site.
* Try to limit what is downloaded.
    * There's a reason we use uglify.
* Use sensible markup that we hope that screen readers can support.
* Add "skip to text" if you have a large nav section.
* Use a toolkit like Bootstrap will make sure that you work on a wide
  range of browsers.

Important Web technologies and their roles
------------------------------------------

* HTML/HTML5 - Describes the content of pages.
* Markdown - Simplified Markup.
* CSS - Describe the appearance of pages.
* Javascript - Add interactivity to Web pages.
* JSON and XML - Common data formats.
* HTTP - The protocol used to send information back and forth.
* erb and haml - Extended markup languages that let you put Ruby in the
  middle of the page.
* DOM - Document object model: How we typically represent a Web page
  within a Javascript program.
* Plugins like Adobe Flash and Oracle Java.
    * Do people really still use Flash?  Yes.  Large numbers of Amazon
      apps, as well as many other things.  

Lab time
--------

Work on Hartl 5 or Hartl 6 or both.
