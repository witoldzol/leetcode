-- https://www.sqlzoo.net/wiki/Self_join
-- 3
SELECT id, name FROM stops JOIN route ON (stops.id = route.stop)
  WHERE num = 4 and company = 'LRT'
-- 5
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 and b.stop=149

