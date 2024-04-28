-- https://leetcode.com/problems/employees-with-missing-information/description/
select t.employee_id from 
(
    select * from Employees e
    full join Salaries s using(employee_id)
) t
where t.name is null or t.salary is null
order by t.employee_id asc
