---
title: HW 3
subtitle: Getting started with Rails (Hartl, Chapter 1)
link: true
schedule: 2018-02-05
due: 2018-02-04
due-time: 10:30pm Sunday
---
# {{ page.title }} : {{ page.subtitle }}

_Warning!  This assignment relies on Cloud 9.  Cloud 9 is in transition.
Please use the traditional Cloud 9, if possible, since that does not
require you to enter a credit card.  But know that you will encounter
a very different UI in getting your virtual machine set up.  See the 
notes below for more information._

## Primary task

**Do all of the steps and exercises in Chapter 1 of Hartl.**

## Submit

Then send me answers to the following questions in a message entitled
"**{{ site.courseid }} {{ site.semester }}, {{ page.title }}: {{
page.subtitle }} (_Name_)**".  Please replace "_Name_" with your name
and do not include the quotation marks.

1. What new `git` commands, if any, did you learn?

2. You modified a variety of files in this chapter.  List the files you
changed, describe each change, and explain why Hartl asked you to make
the change.

## Some notes on using "traditional" `c9.io`

1. You'll use a different set of steps to log in and create the workspace.
When you create the VM, make sure to select the "Rails Tutorial" template.
See the screenshots below for details.  

    a. Start by clicking on "Login for existing c9.io users".

    ![A Web page for AWS CLoud 9.  The button labeled "Login for existing c9.io users" is circled](../images/c9-setup/c9-01)

    b. Next, click on the big plus sign to create a new workspace.

    ![A Web page with a bunch of boxes.  A grey box with a plus sign that says "Create a new workspace" is circled.](../images/c9-setup/c9-02)

    c. Make your workspace public and select "Rails Tutorial".

    ![A Web page entitled "Create a new workspace.  A radio button labeled "Public" is circled, as is a picture button labeled "Rails Tutorial"](../images/c9-setup/c9-03)

    d. And you're ready to go.

    ![The Cloud 9 IDE.  The word "Cloud 9 IDE" is in ASCII art.](../images/c9-setup/c9-04)

2. Your code will be in `~/workspace/hello_app` rather than 
`~/environment/hello_app`.

3. In **Section 1.3.2**, use the following commands.

   ```
   $ cd ~/workspace/hello_app/
   $ rails server -b $IP -p $PORT
   ```

---

