-- solution 1
select (select distinct salary from Employee
order by salary desc
limit 1
offset 1)
as SecondHighestSalary

-- solution 2
