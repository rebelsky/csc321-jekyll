---
title: HW 1
subtitle: Getting started with Ruby
link: true
schedule: 2018-01-24
due: 2018-01-23
due-time: 10:30pm Tuesday
current: true
---
# {{ page.title }}

_Warning!  This homework assignment should take you about five hours.
Make sure that you start with enough time and that you plan breaks to
ask questions._

1. Do the [Codecademy Ruby Tutorial](https://www.codecademy.com/learn/learn-ruby) through section 10a.  (Everything other than do "Banking on Ruby" and the final project.)  For those who care about clarity, please note that shift-tab should allow you to re-indent code.

2. Answer the following questions.

    a. There are at least three techniques for reading a line of text,
    dropping the newline character, and converting to lowercase.

    <pre>
    ; version 1
    text = gets
    text.chomp!
    text.downcase!

    ; version 2
    text = gets.chomp
    text.downcase!
 
    ; version 3
    text = gets.chomp.downcase
    </pre>

    Explain the difference.  Which does the codecademy course seem to
    prefer?  Which do you think I prefer?  Why?

    b. In the exploration of loops, you wrote a short program that
    replaced each instance of a word with the text `REDACTED`.  Rewrite
    that program without a loop.

    c. In the histogram example, the introductory code includes the following
    line.

    <pre>
    frequencies = frequencies.sort_by {|a, b| b }
    </pre>

    Explain what is going on in this example in the context of what you
    know of hash tables from CSC 207.

    d. You may have observed that Ruby methods permit a variable number
    of parameters and default values.  Explain the syntax for each.

    e. Suppose `B` is a subclass of `A`.  How do we design `B` so that 
    `B.new` calls the `A`'s `initialize` method?  How do we design
    `B` so that `B.new` does *not* call `A`'s `initialize` method?

3. Expand the movie database project from section 6 so that

    a. It provides somewhat better feedback.
    
    b. It continues to prompt the user for choices (and carry out the 
    corresponding action) until the user types `"quit"`.

    c. It does some error checking (e.g., on the rating).

4. Email me your answers and code in the *body* of an email message entitled 
"**{{ site.courseid }} {{ site.semester }}, {{ page.title }}:
{{ page.subtitle }} (_Name_)**".  Please replace "_Name_" with your name
and do not include the quotation marks.
