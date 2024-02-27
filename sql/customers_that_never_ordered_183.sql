-- https://leetcode.com/problems/customers-who-never-order/description/
select name as Customers from Customers
where Customers.id not in (select customerId from Orders)
-- alternative solution with left join
select name as Customers from Customers c
left join orders o on c.id = o.customerId
where o.customerId is NULL
