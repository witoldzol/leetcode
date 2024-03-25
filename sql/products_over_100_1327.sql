--  https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/
select p.product_name, sum(unit) as unit from Orders o
join Products p on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_name
having sum(unit) >= 100
