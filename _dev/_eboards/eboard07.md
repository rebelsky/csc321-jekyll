---
title: Eboard 07  Your first database-backed Rails application
number: 07
section: eboards
held: 2018-02-05
link: true
---
CSC 321.01, Class 07:  Your first database-backed Rails application
===================================================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* Model-View-Controller, revisited
* About files.
* Convention vs. configuration
* The components of a Rails application

Preliminaries
-------------

### News and notes

* Mentor session 8-9 Tuesday night
    * KY recommends that you start the homework in advance.
* My weekend evaporated.  I'm still a bit behind on grading.  Sorry.
* Unfortunately, the solution to some of your problems will sometimes 
  be the equivalent of "reboot".  For example, a student who was having
  trouble with Heroku found it easiest to just set up a new Heroku
  instance.

### Upcoming work

* [Hartl 3](../assignments/hartl-3) due Tuesday at 10:30pm.
* [Reading journal on user stories](../readings/user-stories) due
  Thursday at 9:00pm.

### Good things to do (Academic/Artistic)

* CS table Tuesday: Ownership in the digital age
* CS extras Thursday: The evolution of CSC 151
* Rosenfield symposium this week

### Good things to do (Other)

* Posse Plus Retreat Reflections, Community Hour next week (Tuesday,
  11am, JRC 101)

### Questions

Model-View-Controller, revisited
--------------------------------

_Quick review with partner: Where do these parts of an application reside
in a typical Rails application?_

Where do you find the model?  (i.e., the stuff for dealing with your
collection of data)

* `app/models/MODEL_NAME`
* In the database
    * `sqlite` on c9.io
    * Postgres on Heroku
* Model traditionally contains
    * Field specifications (name, type)
    * Restrictions/validations
* That information is hidden in the database schema (and/or the migration)

Where do you find the view?  (i.e., the UI)

* `app/views/MODEL_NAME/FEATURE.html.erb`
* Detour: What are the `FEATURE.json.jbuilder` files?
    * JSON is a standard format for encoding data on the Web.
      JavaScript Object Notation.
    * Strings and numbers look like "strings" and numbers (312321)
    * Objects `{ field: value, field: value }`
    * Arrays: `[value,value,value]`
    * Having a mechanism for other programs to get stuff from yours
      as JSON is helpful.
    * Rails appears to do this by default.
    * Most of us won't take advantage of this.
* The `routes.rb` describes what "methods" the server should fle.
  (More or less, what actions the user can select and how they select
  them.)
* In some applications (perhaps less-well-designed), the views are
  found in the controller.

Where do you find the controller?  (i.e., the application logic)

* Primarily in `app/controllers/MODEL_NAME_controller.rb`
* Also in the classes they inherit from.

Files!
------

`db/migrate/20180111111111_create_users.rb`
  : Instructions for updating the database to add the users table 
    (and anything else associated with that update)

`app/models/user.rb`
  : A description of the user model.  It explains key fields and
    limitations (some explicitly, some implicitly).

`test/models/user_test.rb`
  : Where tests would live if you had any.

`app/controllers/users_controller.rb`
  : The controller for activities that relate to the user.  Contains
    a variety of implicit and explicit methods.

`app/views/users/index.html.erb`
  : The default view of the list of users.

`test/controllers/users_controller_test.rb`
  : A place where tests for the controller live.  Prepopulated with
    a variety of basic tests.

ERB detour
----------

We see three kinds of instructions in the following.  What does each
do?

```
    <% @users.each do |user| %>
      <tr>
        <td><%= user.id %></td>
```

* `<% ... %>`: Ruby code, take verbatim, don't expect result
* `<%= ... %>`: Ruby code, insert the result.  
    * `<%=` is an angry squid.
    * `<%` is a bouquet of flowers
* Everything else: Inserted verbatin into the output.

Other homework issues
---------------------

* Adding user id: `<%= user.id %>` plus updating the table header.
* Convention vs. configuration.
    * Microposts have a field called `user_id`.  That magically links
      to the `id` field in users.
* Code: `<%= micropost.user ? micropost.user.name : "???" %>`
    * You should know the ?: conditional form from C.  (This is
      a "conditional expression".  Stupid languages like C distinguish
      between statements and expressions.
    * `test ? consequent : alternate`
    * The test in this: Does the user exist?
    * If the user exists, we see the user's name
    * If the user does not exist, we see three question marks
    * Why didn't we use `<%= micropost.user.name %>`.  If the user
      does not exist (e.g., because we write unsafe code that lets
      the user be deleted), `micropost.user` may be `nil`, and
      `nil` has no `name` field.

