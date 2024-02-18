-- https://www.sqlzoo.net/wiki/More_JOIN_operations

-- 14
select title, count(actorid) from movie
join casting on (casting.movieid = id)
where yr=1978
group by movieid
order by count(actorid) desc, title

-- 15
select distinct name from casting 
join actor on (actorid=actor.id)
where name != 'Art Garfunkel' and
movieid in (select movieid from casting
join movie on (movieid=id)
 where actorid=
(select id from actor
where name = 'Art Garfunkel'))
