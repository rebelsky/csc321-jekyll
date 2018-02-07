---
title: HW 4
subtitle: Your first Rails app (Hartl, Chapter 2)
link: true
schedule: 2018-02-05
due: 2018-02-04
due-time: 10:30pm Sunday
---
# {{ page.title }}: {{ page.subtitle }}

_I expect that this assignment should take you about two hours._

_Warning!  This assignment relies on Cloud 9.  Cloud 9 is in transition.
Please use the traditional Cloud 9, if possible.  I've included notes
below to explain of the primary differences._

## A note from Sam

When using `git`, please don't use `git commit -a` or `git add .`.  You
should pay attention to the individual files you're working with.  It takes
only a little while longer, it's better practice, and, in the long term,
it saves you from big mistakes.  (If you don't know the alternative to
`git commit -a`, let me know.)

## Your primary task

**Do all of the steps and exercises in [Chapter 2 of Michael Hartl's
_The Rails Tutorial_](https://www.railstutorial.org/book/toy_app).**
You will then answer some questions on those steps.  You may find it
useful to read the questions in advance.

## What to submit

Send me answers to the following questions in a message entitled "**{{
site.courseid }} {{ site.semester }}, {{ page.title }}: {{ page.subtitle
}} (_Name_)**".  Please replace _Name_ with your name.

0. What is the URL of your Cloud 9 instance?  (E.g., 
`https://ide.c9.io/username/rails-tutorial`.)

1. As you likely noted, `rails generate scaffold` creates a *lot* of files.
Explain the (likely) purpose of each of the following.

    a. `db/migrate/20180111111111_create_users.rb` (you will have a slightly different name)

    b. `app/models/user.rb`

    c. `test/models/user_test.rb`

    d. `app/controllers/users_controller.rb`

    e. `app/views/users/index.html.erb`

    f. `test/controllers/users_controller_test.rb`

2. What files did `rails generate scaffold` modify?  What changes did it make
to those files?

3. What changes would you have to make to the application to show the user
id on the `/users` page?

4. Rails often relies on "convention over configuration".  There's a subtle
instance of that principle in section 2.3.3.  What unstated information is
implicit in the design of the relationship between users and microposts?

5. As Hartl notes, the toy application is not nearly robust enough.  Consider,
for example, the association of posts with users.  As you may have noted, once
we have the validation in place, Rails stops you from adding a post with an
invalid user id.  However, it is possible to end up with a post whose `user_id`
does not reference a valid user.  How?

6. Hartl does not have us commit changes until we are ready to deploy to
Heroku.  What are some earlier steps in which a commit might be appropriate?

7. A student who was experimenting with this application added the following
line to `app/views/microposts/index.html.erb`.  Explain what this code does.

    `<td><%= micropost.user ? micropost.user.name : "???" %></td>`

## Some notes on using the "traditional" `c9.io`

1. Don't forget that your work is in the `workspace` directory rather
than the `examples` directory!

2. Don't forget to start your Rails server with 

    `rails server -b $IP -p $PORT`

3. In section 2.3.4, Hartl references `ApplicationController`.  You may find
that your application is using `ApplicationRecord` instead.

<!-- 
Notes to self

See if they have validated the presence of the content (see Listing 2.16).

-->
