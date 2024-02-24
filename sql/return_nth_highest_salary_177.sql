CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select distinct Employee.salary  from Employee
    order by salary desc
    limit 1 offset (N-1) -- this fails when N=0
  );
END;
$$ LANGUAGE plpgsql;
