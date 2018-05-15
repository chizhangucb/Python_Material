-- the union of two select statements is a table containing the rows of both of their results.
-- The result of a select statement is displayed to the user, but not stored. 
-- A create table statement gives the result a name.
-- sqlite3 -init monday.sql
-- load monday.sql into sqlite

-- Cities
create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Children of Abraham: barack and clinton
select child from parents where parent = "abraham";

-- Fillmores: F is greater than "A", "D"
select parent from parents where parent > child;

-- Fur
create table dogs as
  select "abraham" as name, "long" as fur union
  select "barack"         , "short"       union
  select "clinton"        , "long"        union
  select "delano"         , "long"        union
  select "eisenhower"     , "short"       union
  select "fillmore"       , "curly"       union
  select "grover"         , "short"       union
  select "herbert"        , "curly";

-- Parents of curly dogs
select parent from parents, dogs where child = name and fur = "curly";

-- Siblings
select a.child as first, b.child as second
  from parents as a, parents as b
  where a.parent = b.parent and a.child < b.child;

-- Grandparents
create table grandparents as
  select a.parent as grandog, b.child as granpup
    from parents as a, parents as b
    where b.parent = a.child;

-- Grandogs with the same fur as their granpups
select grandog, granpup, c.fur from grandparents, dogs as c, dogs as d
  where grandog = c.name  and
        granpup = d.name and
        c.fur = d.fur;


