-- CS 61A Fall 2014
-- Name: Chi Zhang
-- Login: 

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- Q1
-- The names of all "toy" and "mini" dogs
CREATE TABLE dogs_size AS
  SELECT a.name AS name, b.size AS SIZE
    FROM dogs AS a, sizes AS b
    WHERE b.min < a.height AND a.height <= b.max;

SELECT name FROM dogs_size WHERE SIZE = 'toy' OR SIZE = 'mini';

-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- Q2
-- All dogs with parents ordered by decreasing height of their parent
SELECT child FROM parents, dogs WHERE parent = name ORDER BY height DESC;

-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Q3
-- Sentences about siblings that are the same size
WITH 
  childs_size(parent, child, child_size) AS (
	SELECT a.parent, a.child, size FROM parents AS a
	INNER JOIN dogs_size as b ON a.child = b.name
	)

SELECT a.child || ' and ' || b.child || ' are ' || a.child_size || ' siblings'
  FROM childs_size AS a, childs_size AS b 
  WHERE a.parent = b.parent AND a.child < b.child AND a.child_size = b.child_size;

-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Q4
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
WITH 
  dogs_sum_heights(names, n, sum_height, last_height) AS (
	SELECT name, 1, height, height FROM dogs UNION
	SELECT a.names || ", " || b.name, n+1, sum_height + b.height, b.height
	  FROM dogs_sum_heights AS a, dogs as b 
	  WHERE a.last_height < b.height AND n<4
	)
SELECT names, sum_height FROM dogs_sum_heights 
  WHERE sum_height >= 170 AND n = 4 ORDER BY sum_height

-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- Q5
-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS 
  WITH
    non_parents(ancestor, descendent) AS (
      SELECT a.parent, b.child FROM parents AS a, parents AS b
	    WHERE a.child = b.parent UNION
	  SELECT ancestor, child FROM non_parents, parents 
	    WHERE parent = descendent
	)
  SELECT ancestor AS first, descendent AS second FROM non_parents;

CREATE TABLE no_order AS
  SELECT first as one, second as two FROM non_parents UNION
  SELECT second      , first         FROM non_parents;

SELECT a.one, a.two
  FROM no_order AS a, dogs as b, dogs as c
  WHERE a.one = b.name AND a.two = c.name  
  ORDER BY b.height - c.height

-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


