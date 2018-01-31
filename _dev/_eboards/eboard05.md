---
title: Eboard 05  Web technologies
number: 05
section: eboards
held: 2018-01-31
link: true
current: true
---
CSC 321.01, Class 05:  Web technologies
=======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* A broad overview of Web and related technologies
* Three-tier architecture
* Some notes on cookies 

Preliminaries
-------------

### Admin

* Fruit snax!
* Classroom?  Here or 3813?
* Apologies for being behind in grading.  I have a busy next 
  few days, but I will do my best to catch up over the weekend.
* Last reminder: If you have TuTh afternoons available for the next few
  weeks, you should consider Megan Goering '08's "Design Thinking" 
  course.  TuTh 2:00-3:50, JRC 209. starting tomorrow.
* Many of you received comments that you should be more thorough on your
  journal answers.  Here's an appropriate length one for part 1 of t he
  latest journal:
  _DNS (Domain Name System) -- The Domain Name System matches hostnames to IP addresses so that a browser user does not have to remember the IP addresses of each site they want to visit. The browser asks a DNS server where a given hostname is, and then receives an IP address that refers to the same place._.
* Mentor session 6-7:30pm tomorrow.

### Upcoming work

* [Hartl 1](../assignments/hartl-1) due Thursday at 10:30pm.
    * This should be less time-consuming than the Ruby exercises.
* [Hartl 2](../assignments/hartl-2) due Sunday at 10:30pm.
    * This should take about the same amount of time as the first
      Hartl assignment.

### Good things to do (Academic/Artistic)

* CS extras Thursday: Sam's students
* Rebecca Wingo: How to Harvest History.  Friday Feb. 2, 4pm, Burling 
  Library Lounge.
    * Workshop: Saturday Feb. 3, 10-1, DLab
    * Register for workshop at <https://grinnell.formstack.com/forms/wingo_workshop>

### Good things to do (Other)

* WinC 6pm on Thursday.  (Every other week.)
* Posse Plus Retreat Reflections, Community Hour next week (Tuesday,
  11am, JRC 101)

### Questions

What topics did people want to hear about?
  : Here's the approximate list I recorded.

* HTML: 3
* Three-tier model: 2
* Broad overview: 2
* Security: 2
* Networks and network protocols: 2
* Cookies: 2
* Push vs. pull: 1
* Stateless: 1
* XML: 1
* Alternatives to Rails: Python+Django, Node.js, PHP, ...: 1
* WEBrick and comparison to other servers: 1
* Horizontal scaling: 1
* MVC: 1

What's with this "check" garbage?  What does it mean in terms of my letter grades?
  : Check means "satisfactory".  If everything is satisfactory, you get a B.
  : Applies to reading journals only.  "Satisfactory" on homework
    is an A-.

How do you timebox?
  : I spent N hours.  This is what I achieved.
  : So you should probably stop at N hours minus 20 minutes
    to give yourself time to write something.
  : About three hours per Hartl assignment.
 
A broad overview of Web technologies
------------------------------------

* TCP/IP - How do you get information from computer to computer
  on a network of computers.
    * Routing
    * Breaking a larger message into smaller pieces (and rearrange)
    * Providing feedback and error messages 
    * Etc.
    * Byte order (yay endian wars)
* TCP/IP was designed so that you can layer other protocols on
  top of it.  Dozens (if not more) for particular 
  applications/situations/types of data.  HTTP, FTP, Gopher,
  smtp, etc.
* Early 1990's TBL develops WWW.
     * HTTP
* HTTP
    * Specifies the kinds of requests 
       * GET a resource
       * POST a resource or request (typically interpreted
         as "here's a request plus additional information")
       * UPDATE a resource (rarely used)
       * DELETE a resource
       * Each Web application can have its own general semantics
         for what to do for each request.
    * Specifies the forms of responses
       * Numeric code (success or failure)
       * 404 - Not found
       * If it succeeds, type of data and content
    * "Stateless"
       * A stateful protocol remembers the state of the communication
         (e.g., where you are in a directory structure, what you've
          said recently, that you've authorized)
       * Stateless protocols don't remember state (except for
         some tricks)
       * Assumption: If you call the same operations on the same
         values (that is, ask for the same URL), you get the same
         response.
* Problem: How do I refer to information?  URL.
    * Originally designed just for Web, but now expanded.
    * Protocol: http, https, ftp, gopher, mailto, file, ...
    * Machine (or related info): 
    * User information (and authentication)
    * Resource
    * Additional info
    * http://www.cs.grinnell.edu/~rebelsky/Courses/CSC321/2018S/
    * "Parameters" with a question mark and more info
    * Combination of "what I tell my Web browser" and "what my Web
      browser tells the server"
* Problem: What do data look like?  HTML
    * Information plus meta-information
    * Surround information with "tags" like `<p>...</p>`
* It turns out that this isn't as much as we'd like for many
  "applications" of the Web.
    * State - Cookies.  Browser sends information to client.
      Client should send it back to browser with the next
      request.
        * Loses purity of reference of URLs
        * Raises security risks
    * Interactivity: We need programs to run on the page.
        * Java - Embedded application that should not talk
          to the rest of the page.
        * Flash - Embedded application that might be able to
          talk to the rest of the page and is written by people
          who don't understand security.
        * JavaScript - Embedded code that is expected to interact
          with the page.  (Good security model?  We hope.)

Technologies mentioned (or that I should have mentioned)

* TCP/IP
* HTTP
* HTTP Cookies
* HTML
* URI
* JavaScript
* CSS - Didn't cover
* DNS - Didn't cover
