---
title: HW 5
subtitle: A static site (Hartl, Chapter 3)
link: true
schedule: 2018-02-07
due: 2018-02-06
due-time: 10:30pm Tuesday
---
# {{ page.title }} : {{ page.subtitle }}

_I expect that this assignment should take you about two hours._

_Warning!  This assignment relies on Cloud 9.  Cloud 9 is in transition.
Please use the traditional Cloud 9, if possible.  I've included notes
below to explain of the primary differences._

## Your primary task

Do all of the exercises in [Chapter 3 of Michael Hartl's _The Rails
Tutorial](https://www.railstutorial.org/book/static_pages).  You will
then answer some questions on those steps.  You may find it useful to
read the questions in advance.

1. Please share your GitHub or Bitbucket repo with me. (My GitHub username
is `rebelsky` and my Bibucket username is either `rebelsky` or
`rebelsky@grinnell.edu`.

## What to submit

Send me answers to the following questions in a message entitled "**{{
site.courseid }} {{ site.semester }}, {{ page.title }}: {{ page.subtitle
}} (_Name_)**".  Please replace _Name_ with your name.

0. What is the URL of your Cloud 9 instance?  (E.g.,
`https://ide.c9.io/username/rails-tutorial`.)

1. What is the URL of your GitHub or BitBucket repo?

2. What is the URL of your Heroku application?

3. The suggested `README.md` refers to `LICENSE.md`.  Where does that
latter file come from?

4. In connecting your local repo to Bitbucket, you issued a pair of commands 
like the following.

    ```
    git remote add origin git@bitbucket.org:username/hartl-sample-app.git
    git push -u origin master
    ```

    Explain the four parameters to the first `git` command and the four
    parameters to the second `git` command.

5. Right after Listing 3.5, Hartl tells you to use the following `git`
command.

    ```
    git commit -am "Add hello"
    ```

    What command(s) should you use instead if you want to be safer
    (and thereby follow my standards)?

6. At the start of section 3.2.1, Hartl tells you to issue the following
command.

    ```
    rails generate controller StaticPages home help
    ```

    What files does that command modify and add?  What changes are made
    to the modified files?  What seems to be the purpose of each added
    file?  (Note that you may have to finish the chapter to understand
    most of the purposes; it's okay to say "Not referenced" for some
    of them.)

7. Hartl has you look for exact text in the page title, using commands
like

    ```
    assert_select "title", "Home | Ruby on Rails Tutorial Sample App"
    ```

    or

    ```
    assert_select "title", "Home | #{@base_title}"
    ```

    But what if we only want to assert that the title *contains* a
    particular word?  Rewrite the assertions above to check if the
    title contains the word `"Home"`.  Your assertion should hold
    whether the title is `"Home | Ruby on Rails Tutorial Sample App"`
    or `"Home | Sample App"` or `"Sample App | Home"` or even 
    `"I Want To Go Home"`.

    Note that you may not find the answer in Hartl; you'll have to do
    some further exploration of the details of minitest.

8. The tests given in [Listing 3.30](https://www.railstutorial.org/book/static_pages#code-base_title_test) are not yet DRY in that the bodies are
nearly identical.  Rewrite the code to make it more DRY.

9. What did you write for the missing text in [Listing 3.42](https://www.railstutorial.org/book/static_pages#code-root_test)?

## Some notes on using the "traditional" `c9.io`

1. You will continue to work in the `workspace` directory rather than
the `examples` directory.

2. Don't forget that you start the rails server with

```
rails server -b $IP -p $PORT
```

## Some issues you may encounter

You may find that minitest gives up when it encounters an error, rather
than continuing with the remaining tests.  Don't worry; chalk it up to
"I need to fix the code!"  But make sure that all the tests pass by the
time you are done.
