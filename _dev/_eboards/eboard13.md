---
title: Eboard 13  Design patterns
number: 13
section: eboards
held: 2017-10-05
---
CSC 321.01, Class 13:  Design patterns
======================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Questions
* Why design patterns?
* Exploring patterns
* Example Pattern: Iterator
* Example Pattern: Adaptor
* Pattern: Factory
* Pattern: Dependency injection
* Pattern: Observer
* Pattern: Strategy
* Pattern: Prototype
* Pattern: Flyweight

### News / Etc.

* The CSC 322 mentors arrive next week.  Tuesday will be spent meeting
  with the mentors.  Please plan to meet with them at lunch and at 11,
  if possible.  (Also plan to attend their Tuesday Extra.)
* Next Thursday is our wrapup class.  We'll debrief on our learning
  outcomes and you will have chances to evaluate the class.

### Upcoming Work

* No more reading journals.
* [The last programming project](../assignments/last-project) is due 
  next Friday night. (Note change)

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic/Artistic

* CS Extras Today: Grad school
* Film tonight: _Together_, <http://togetherfilm.org>.
  8:00-9:15 p.m. in Bear 205.

#### Other

* Plays!
* Sporting events!

### Questions

Why design patterns?
--------------------

* As we grow as programmers, we start to realize that there are common
  approaches that work well, make us more efficient, make our program
  more reliable, make our programs more extensible, ...
* E.g., the CSC 151 student learn that there's a "pattern" to a procedure
  that finds an extreme value in a list (e.g., largest, furthest from zero,
  longest, westernmost, most colorful, ...)

    ```
    (define BEST
      (lambda (lst)
        (if (null? (cdr lst))
            (car lst)
            (BETTER (car lst)
                    (BEST (cdr lst))))))
    ```

* Functional programmers then say: "Oh, I should just write a hop."
    ```
    (define make-best
      (lambda (better)
        (lambda (lst)
          (let ([body (lambda (lst)
                        (if (null? cdr lst)
                            (car lst)
                            (better (car lst)
                                    (body (cdr lst)))))])
           body))))
    (define make-best-alt
      (lambda (better)
        (lambda (lst)
          (let kernel ([lst lst])
            (if (null (cdr? lst))
                (car lst)
                (better (car lst)
                        (kernel (cdr lst))))))))
    (define largest (make-best max))
    (define smallest (make-best min))
    (define westernmost (make-best (lambda (city1 city2)
                                     (< (longitude city1) (longitude city2)))))
    ```
* Some of the patterns you develop are just small tricks.  In C, you
  should generally write `(CONSTANT == VAR)` rather than `(VAR == CONSTANT)`.
* Experienced programmers have a much richer set of patterns than novice
  programmers.  
* Let's communicate those ideas so that others can use them.
* Christoper Alexander, _A Design Language_.  Architecture book.
* Computer scientists, in reading Alexander, decided that they should do
  the same thing.
* Design Patterns: A set of patterns for typically large object-oriented
  programs.  We tend to focus on the patterns in the book _Design Patterns_
  by GoF.
* Reaction one (positive): When faced with a problem, I should always look
  at the list of patterns and find the ones that are appropriate; I know
  this will make programs better / more reliable / easier to maintain /etc.
* Reaction two (negative): Patterns limit programmer creativity.  Patterns
  make you lazy.
* Reaction three (intermediate): Knowing patterns helps you think more
  broadly, but treat them as ways of thinking rather than explicit solutions.
  Patterns give you a language to talk to other programmers/SWEs/etc..
* Patterns are popular enough that people have started doing patterns
  for all sorts of things.
    * CS Education patterns
    * Web design patterns
    * DEVops patterns
    * Antipatterns

Exploring Patterns
------------------

For each pattern, it is useful to explore the problem it addresses,
the core idea in the solution, the details of the solution, and one
or more semi-realistic examples of the pattern in use.  

(Unfortunately, too many of the examples online are completely
made up examples.)

I'll do two, then I'll give you some time to prepare your own answers
for a variety of others.

Example Pattern: Iterator
-------------------------

Problem: You have a collection of values.  You want to do something with
or to every element of the collection (e.g., print it out).

Philosophy: Whatever you do, focus on abstraction.  So don't rely on the
underlying details too much.

Bad (traditional) solution:  Rely on the underlying details.  If you are
iterating an array (or that you think is an array), keep track of the
index.  If you iterating a linked list, keep a pointer.  (Or maybe have
your list have a "current" element.)

Why this strategy is bad: Violates ideas of encapsulation.  "current"
makes it difficult to iterate the list multiple times simultaneously.
Does not support polymorphism.

Solution: Require/assume that every collection provide a method,
that returns a new Iterator object.  Iterators let you visit the values
one by one.  (Simplest iterators: `current`, `next!`, `any-left?`)

Now, you can write things like

```
for (it = collection.iterator(); it.any-left?; it.next!) {
  it.current.print();
}
```

Note: Good languages implement this already.

Example: Skip

Example Pattern: Adaptor
------------------------

Problem: We need an object that does X.  ("implements interface X").
We have an object that does Y, which is incredibly similar to X.  What
do we do?

Philosophy: Provide a bridge that lets us treat Y's as X's.

Solution: Write a class, Adaptor, that implements X and either extends
or includes Y.  Delegate each call to an X method to a Y method.

Example:

Want: To do list.

```
public interface ToDoList {
  public void addTask(Task t);
  public Task nextTask();
  public boolean moreTasksP();
} // interface ToDoList
```

Have: Queues

```
public class Queue {
  public void enqueue(Object o);
  public Object dequeue();
  public boolean emptyP();
}
```

Solution:

```
public class ToDoQueue implements ToDoList
{
  Queue q;

  public void addTask(Task t) { q.enqueue(t); }
  public Task nextTask() { return (Task) q.dequeue(t); }
  public boolean moreTasksP() { return q.emptyP(); }
}
```

Why bother creating adapters?  (E.g., why should I have ToDoQueue rather
than just using a Queue instead of a ToDoList in my code that uses ToDoList?)

* One of our goals in object-oriented design is that things should be
  clear and readable.  Saying that we have a ToDo list makes it clearer
  what we're doing.
    * Helps people read your code.
* One of the classes may need/have more methods; this avoids muddying the
  waters.
* One of the goals of OO design is to specify at a high level what functionality
  you want.
* Makes it easy to change the underlying implementation.

### A related pattern: Decorator

Problem: Want to add functionality to an existing class.

Example: I want to be able to query my class for the number of times
any method is called.

```
public interface Analyzable
{
  /** Find out how many times procName has been called. */
  public int numCalls(String procName);
}
```

Philosophy one: Use something like an adapater.

```
public class AnalyzableQueue
  extends Queue
{
  HashTable h;
  
  private count(String procname)
  {
    if (h.get(procname) == null)
      h.set(procname, 1);
    else
      h.set(procname, h.get(procname) + 1);
  }

  public void enqueue(Object o) { count("enqueue"); super.enqueue(o); }
  public Object dequeue() { count("dequeue"); return super.dequeue(); }
  public boolean emptyP() { count("emptyP"); return super.emptyP(); }

  public int numCalls(String procName)
  {
    // Sanity check
    ...
    val = h.get(procname);
    if (val == null) return 0;
    else return val;
  }
}
```

Sam (and many other people) call these "Wrappers".

Solution 2: Add a language feature that lets programmers decorate methods,
adding things that happen before or after the methods.  And let the
programmers "introspect" the classes, getting things like a list of
methods.

```
for method: Class.super.methods
  Class.method = prepend(method, "count(method.toString())")
```

Pattern: Prototype
------------------

Pattern: Factory 
----------------

Pattern: Observer
-----------------

Pattern: Dependency injection
-----------------------------

Pattern: Strategy
-----------------


