-- https://leetcode.com/problems/employees-whose-manager-left-the-company/description/
select employee_id from Employees e 
where 
salary < 30000
and 
manager_id not in (select employee_id from Employees o)
order by employee_id
