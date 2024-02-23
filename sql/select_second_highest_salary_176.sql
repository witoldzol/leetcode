-- solution 1
select (select distinct salary from Employee
order by salary desc
limit 1
offset 1)
as SecondHighestSalary

-- solution 2 using self join
select max(e1.salary) as SecondHighestSalary from employee e1
join employee e2 on (e1.salary < e2.salary)
