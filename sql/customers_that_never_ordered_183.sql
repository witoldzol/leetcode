-- https://leetcode.com/problems/customers-who-never-order/description/
select name as Customers from Customers
where Customers.id not in (select customerId from Orders)
