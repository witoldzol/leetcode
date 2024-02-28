-- subquery matching two values
select d.name as Department, e.name as Employee, e.salary as Salary from Employee e
join Department d on d.id=e.departmentId
where (departmentId, salary) in  (select  departmentId, max(salary) from Employee e
group by departmentId )
-- using ALL >=
select d.name as Department, e.name as Employee, e.salary as Salary from Employee e
join Department d on d.id=e.departmentId
where e.salary >= all(select salary from Employee e2 where e.departmentId=e2.departmentId and e.name != e2.name)
