-- https://www.sqlzoo.net/wiki/Self_join
-- 3
SELECT id, name FROM stops JOIN route ON (stops.id = route.stop)
  WHERE num = 4 and company = 'LRT'
-- 5
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 and b.stop=149
-- 6
select a.company, a.num, stopA.name, stopB.name from route a
join route b on (a.company=b.company and a.num=b.num)
join stops stopA on (a.stop = stopA.id)
join stops stopB on (b.stop = stopB.id)
where stopA.name='Craiglockhart' and stopB.name='London Road'
-- 7
select a.company, a.num from route a 
join route b on (a.company=b.company and a.num = b.num)
where a.stop = 115 and b.stop=137
group by a.num
-- 8
select a.company, a.num from route a
join route b on (a.company = b.company and a.num = b.num)
join stops sA on (a.stop = sA.id)
join stops sB on (b.stop = sB.id)
where sA.name = 'Craiglockhart' and sB.name = 'Tollcross'
-- 9
select distinct stops.name, a.company, a.num from route a 
join route b on (a.num = b.num and a.company = b.company)
join stops on (a.stop = stops.id)
where a.company = 'LRT' and b.stop = 53
order by b.num
-- 10
-- solution explained here : https://hackernoon.com/learning-self-join-queries-with-sqlzoo-xc163ue7
select r1.num, r1.company, s1.name, r4.num, r4.company from route r1
join route r2 on ( r1.company = r2.company and r1.num = r2.num)
join stops s1 on ( r2.stop = s1.id)
join route r3 on ( s1.id = r3.stop )
join route r4 on ( r3.num = r4.num and r3.company = r4.company )
where r1.stop = (select id from stops where name = 'Craiglockhart')
and r4.stop = (select id from stops where name = 'Lochend')
order by r1.num, s1.name, r4.num
