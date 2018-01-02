---
title: Eboard 11  Modeling, continued
number: 11
section: eboards
held: 2017-09-28
current: true
---
CSC 321.01, Class 11:  Modeling, continued
==========================================

_Overview_

* Preliminaries
    * Notes and news
    * Upcoming work
    * Extra credit
    * Questions
* SQL basics
* Lab

### News / Etc.

* Apologies for the late start today.
* Please let me know when you notice problems on the Web site.  I think 
  I've fixed most of them.  (Okay, something is massively wrong with the
  generation of readings in the schedule, but that turns out to be a programming
  problem I don't have time to address.)
* I'll be generating today's lab live today.  Sorry!

### Upcoming Work

* [Reading journal for class 12](../readings/legacy) due Monday night.
* [The last programming project](../assignments/last-project) to be
  posted tonight, due a week from Tuesday.

### Good things to do

_Note: I do not do extra credit in two-credit classes._

#### Academic

* Convocation today.
* CS table Tuesday
* CS extras Thursday: Grad school

### Questions

SQL basics
----------

Common problem: We want to model data in our program.

A model is a collection of names/types that describe some kind of data.

Traditionally, we think about grouping these fields together in an object
or in a table in which each row is one "thing" and the columns correspond
to the fields.

We then want to do things with the tables

* I want all of the faculty members whose specialization is Vision
* I want all of the movies whose rating is PG
* I want all of the movies released before 1970
* I want all of the movies released before 1970 whose rating is PGa

We often want to ask compound things, too

* I want the release dates of all the movies that Sam Rebelsky
  reviewed.

How do you implement this?  Lots of strategies, most bad.

Solution: Build programs whose only job is to manage tabular data.
The programs that manage this are Database Management Systems.

Note: Common syntax is probably important.  SQL.  Standard/structured
query language, designed for working with data in the "related tables"
format.  ("Relational databases; "relation" is another name for "table")

* SELECT columns FROM table
* SELECT columns FROM table WHERE restrictions
* SELECT columns FROM table1,table2 WHERE restrictions
     * SELECT reviews.reviewername FROM movies,reviews WHERE
       movie.moviename = 'Star Wars' AND review.movieid = movie.movieid
* UPDATE table SET column=value WHERE ...
* INSERT columns VALUES values INTO table
* CREATE TABLE name ... (Sam always looks this one up)

These kinds of things are popular among the many popular implementations
of SQL (MySQL, Oracle, SQLite, PostgeSQL, 

There are also other models of data that are less standardized and less
focused on tables.

Unfortunately, SQL misses many things you want to do.

* List all the tables in the database.
* Determine what columns are in a table.
* Write a script

Lab
---

1. Open your C9 account and navigate to your first Rotten Potatoes instance.

2. Start the command-line database manager with `rails dbconsole`.

3. Type `.help` to determine what commands are available.

4. Determine what tables are available by typing `.tables`.  (The command
is different in every DBMS.)

5. Determine the structure of the movies table by typing `.schema movies`.

6. Get all the movie data with `SELECT * FROM movies;`

7. Get all the movie titles with `SELECT title FROM movies;`

8. Get all the movie titles plus ids plus ratings.  Separate the fields
with commas.

9. Get all the movie titles plus ids plus ratings where rating is PG

10. Get all the movie titles plus ids plus ratings plus year where year is at least (pick a year).

11. Get all the movie titles plus ids plus ratings where year is at least (pick a year).  [Note, we are selecting by year, but not displaying year.]

12. Add two more movies, specifying everything besides id. (You will need
to look up the INSERT syntax to get it right.)  
    * `INSERT into TABLE (fields) VALUES (values);`

13. Try to add a movie with a duplicate id.

14. Create a new table, `reviews`, that contains the following columns.
(You will need to look up the CREATE TABLE syntax to get it right.  You
may also want to use `.schema movies` for ideas)
    * `id` (auto generated), 
    * `movieid`, an integer which references an entry in the movie table, 
    * `reviewer`, a string 
    * `review`, a string. 

15. Verify that you created the table correctly with `.schema`.

16. Generate four sample reviews for at least two different movies

17. Try the command `SELECT * from movies,reviews` to see what you get.

18. Figure out how to select just the reviews for one movie.

Debrief
-------

_What do I expect you to take away from all of this?_

* You can master the basics of SQL in about two hours.
* You will, however, miss some subtleties, such as how to set up tables
  that automatically generate and check keys.
* Some of the commands are *really* powerful and therefore *really*
  timeconsuming.
    * It takes a bit of time to understand the subtleties of join
    * But there are lots of good articles
* Spend three (eight hour) days of your life learning this stuff.  It's
  valuable.
* When you are working in rails, it's all done for you.
