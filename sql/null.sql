-- https://www.sqlzoo.net/wiki/Using_Null
-- 1
select teacher.name from teacher, dept where teacher.dept=dept.id
-- 2
SELECT teacher.name, dept.name
 FROM teacher INNER JOIN dept
           ON (teacher.dept=dept.id)

