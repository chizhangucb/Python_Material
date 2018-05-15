------------
-- Cities --
------------

create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,              71,              "Cambridge"        union
  select 45,              93,              "Minneapolis"      union
  select 33,             117,              "San Diego"        union
  select 26,              80,              "Miami"            union
  select 90,               0,              "North Pole";

create table cold as
  select name from cities where latitude > 43 union
  select "Chicago";

select name, "is cold!" from cold;

create table distances as
  select a.name as first, b.name as second,
         60*(a.latitude-b.latitude) as distance
         from cities as a, cities as b
         where a.name != b.name
         order by a.longitude;

select second from distances where first="Minneapolis" order by -distance;

-- Maybe not a good idea

create table phrase as select 'hello, world' as s;

select substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) from phrase

create table lists as select 'one' as car, 'two, three, four' as cdr;

select substr(cdr, 1, instr(cdr, ',')-1) as cadr from lists;

---------------
-- Sentences --
---------------

create table nouns as
  select "the dog" as phrase union
  select "the cat"           union
  select "the bird";

select subject.phrase || " chased " || object.phrase
       from nouns as subject, nouns as object
       where subject.phrase != object.phrase;

-- != or <> can mean "not equal to"

create table ands as
  select phrase from nouns union
  select first.phrase || " and " || second.phrase
         from nouns as first, nouns as second
         where first.phrase != second.phrase;

select subject.phrase || " chased " || object.phrase
       from ands as subject, ands as object
       where subject.phrase != object.phrase;

