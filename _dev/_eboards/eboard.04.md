---
title: Eboard 04  Deploying Rails applications
number: 4
section: eboards
held: 2017-01-30
---
CSC 321.01, Class 04:  Deploying Rails applications
===================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Detour: A brief introduction to regular expressions
* Wrap up Hartl 1
* Start Hartl 2

### News / Etc.

* In general, I'll have you start on the Hartl on your own and we'll
  work on finishing it up during class.
* Don't be afraid to ask for help!  (From me, from your classmates, from
  Adam, from the Interweb.)

### Upcoming work

* [Hartl chapter 2]({{ site.baseurl }}/assignments/hartl.02).
* [Reading Journal]({{ site.baseurl }}/assignments/reading-journal.05).

### Good things to do

*Nope, no extra credit.*

* CS table, Tuesday: Planning for the semester.
* Women-in-CS, Tuesday, 7pm: Discussion of _Hidden Figures_.
* Teach-in on executive order, Wednesday at 7pm.
* CS extras, Thursday: LaTeX.
* Swim meet Saturday, maybe Friday.

### Questions

A brief introduction to regular expressions
-------------------------------------------

* We want to look for text
* It in a long, unstructured file.
* Individual lines.
* When we have common problems, we build a library.
* We also look for "optimal" (or at least good) solutions to the problem.
* Almost everyone uses "regular expressions" for doing pattern matching
  in text.
* People don't agree on syntax or even on capabilities.
* Regular expressions are defined recursively.
* In Ruby, we can use `STR =~ PATTERN`, which appears to return
  the number of times the pattern matches or `nil`, or we can
  use `PATTERN.match(STR)`, which returns a match object.
* Match objects allow you to extract information.

**Exact matches of individual characaters**.  `a` matches `a`.
  If your regular expressions are designed to accept substrings, `a`
  matches "alphabet" or "hello, it's a lion!" or anything that includes
  `a`

```
irb(main):001:0> "hello" =~ /l/
=> 2
irb(main):002:0> "hello" =~ /a/
=> nil
```

**Composition of regular expressions.** If R is a regular and S is a
regular expression, then RS is a regular expression, matches R and then
S.  `aa`, `ac`

```
irb(main):003:0> /aa/.match("aardvark")
=> #<MatchData "aa">
irb(main):004:0> /aa/.match("antelope")
=> nil
irb(main):005:0> /aa/.match("aa it's eh aardvark")
=> #<MatchData "aa">
```

**`.` matches any one character.** `a.a`

```
rb(main):006:0> /a.a/.match("aardvark")
=> nil
irb(main):007:0> /a.a/.match("alabama")
=> #<MatchData "ala">
irb(main):008:0> /a.a/.match("a aardvark")
=> #<MatchData "a a">
irb(main):009:0> /a..a/.match("alabama")
=> nil
irb(main):010:0> /a...a/.match("alabama")
=> #<MatchData "alaba">
```

**`*`, the Kleene star.**  If R is a regular expression, R* matches
0 or more repetitions of the regular expression.  Some implementations
of regular expressions also allow a + for one or more repetitions.
* binds more tightly than concatentation.

**Parentheses group**

```
irb(main):012:0* /a*/.match("um")
=> #<MatchData "">
irb(main):013:0> /a*/.match("aardvark")
=> #<MatchData "aa">
irb(main):014:0> /a*/.match("aardvaaaaark")
=> #<MatchData "aa">
irb(main):015:0> /ab*/.match("abababab")
=> #<MatchData "ab">
irb(main):016:0> /(ab)*/.match("abababab")
=> #<MatchData "abababab" 1:"ab">
irb(main):017:0> /(ab)*/.match("ababcababab")
=> #<MatchData "abab" 1:"ab">
irb(main):018:0> /c(ab)*/.match("ababcababab")
=> #<MatchData "cababab" 1:"ab">
irb(main):019:0> /d(ab)*/.match("ababcababab")
=> nil
irb(main):020:0> /(a.)*/.match("alabama")
=> #<MatchData "alabam" 1:"am">
irb(main):021:0> /(.a)*/.match("alabama")
=> #<MatchData "" 1:nil>
irb(main):022:0> /.a/.match("alabama")
=> #<MatchData "la">
irb(main):023:0> /.a/.match("alabama")
=> #<MatchData "la">
irb(main):024:0> 
irb(main):025:0* /.*a/.match("alabama")
=> #<MatchData "alabama">
irb(main):026:0> /.*a/.match("88888888888alaba888888888ma")
=> #<MatchData "88888888888alaba888888888ma">
```

Parentheses also create separate entries in the match data, which
you can then use as an array.

```
irb(main):030:0> /(.*)fox(.*)dog(.*)/.match("the quick brown fox jumps over the lazy dog.")
=> #<MatchData "the quick brown fox jumps over the lazy dog." 1:"the quick brown " 2:" jumps over the lazy " 3:".">
irb(main):031:0> /(.*)fox(.*)dog(.*)/.match("the quick brown fox jumps over the lazy dog.")[1]
=> "the quick brown "
```

**Literal interpretation of special characters**  Use a backslash.

```
irb(main):027:0> /*/.match("3 * 4")
SyntaxError: (irb):27: target of repeat operator is not specified: /*/
        from /usr/bin/irb:11:in `<main>'
irb(main):028:0> /\*/.match("3 * 4")
=> #<MatchData "*">

Others: `\.`, `\\`, `\*`, `\(`, `\^`, `\)`, `[`, `\]`, ...
    
**Sets of characters** `[characters]`.  Negate with `[^characters]`.
Also predefined sets.  Does not work with regular expressions, only
individual characters.

**Bound to location in string.**  `^` start of the string, `$` end.

irb(main):035:0> /[aeiou]*/.match("boo")
=> #<MatchData "">
irb(main):036:0> /[aeiou]/.match("boo")
=> #<MatchData "o">
irb(main):037:0> /[qrs]/.match("boo")
=> nil
irb(main):038:0> /[^qrs]/.match("boo")
=> #<MatchData "b">
irb(main):039:0> /^o/.match("observe")
=> #<MatchData "o">
irb(main):040:0> /o$/.match("observe")
=> nil
irb(main):041:0> /[aeiou]*$/.match("boo")
=> #<MatchData "oo">

**`|` for either/or**

```
rb(main):042:0> /and|or/.match("this and that")
=> #<MatchData "and">
irb(main):043:0> /and|or/.match("this or that")
=> #<MatchData "or">
irb(main):044:0> /and|or/.match("this but not that")
=> nil
```

**We do not have general negation (or we should not).**

Sam's favorite hard regular expression to write: C comments, which
start with slash-star and end with star-slash, and can have almost
anything in between.  Try to extract the contents of the comment.

Some things you should not match, or not match completely.

* `3 / 4 * 5 * 6 / 7` - slash and star must be neighbors
* `/* hello */ /* goodbye */` - two comments
* `/* hello */ */` - invalid; bind closing comments tightly

One incorrect solution: `/\/\*(.)*\*\//.match(...)[1]`

What do you do with the match data?  Typically, (a) check that it
exists (there's a match); (b) extract parts.

Wrap up Hartl 1
---------------

Start Hartl 2
-------------

