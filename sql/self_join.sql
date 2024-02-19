-- https://www.sqlzoo.net/wiki/Self_join
-- 3
SELECT id, name FROM stops JOIN route ON (stops.id = route.stop)
  WHERE num = 4 and company = 'LRT'
