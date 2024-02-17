-- https://www.sqlzoo.net/wiki/More_JOIN_operations

-- 14
select title, count(actorid) from movie
join casting on (casting.movieid = id)
where yr=1978
group by movieid
order by count(actorid) desc, title
