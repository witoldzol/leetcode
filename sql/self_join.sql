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
