-- https://www.sqlzoo.net/wiki/Using_Null
-- 1
select teacher.name from teacher, dept where teacher.dept=dept.id
-- 2
SELECT teacher.name, dept.name
 FROM teacher INNER JOIN dept
           ON (teacher.dept=dept.id)
-- 3
select teacher.name, dept.name from teacher
left join dept on teacher.dept = dept.id
-- 4
select teacher.name, dept.name from teacher
right join dept on teacher.dept = dept.id
-- 5
select name, COALESCE(mobile, '07986 444 2266') from teacher
-- 6
select teacher.name, coalesce(dept.name, 'None') from teacher 
left join dept on teacher.dept=dept.id
-- 7
select count(teacher.name), count(mobile) from teacher
-- 8
select dept.name, count(teacher.name) from teacher
right join dept on dept.id=teacher.dept
group by dept.name
-- 9
select name, case when teacher.dept=1 or teacher.dept=2 then 'Sci' else 'Art' end as pre from teacher 
-- 10
select name, case 
  when teacher.dept=1 or teacher.dept=2 then 'Sci' 
  when teacher.dept=3 then 'Art'
  else 'None'
end as pre 
from teacher 

