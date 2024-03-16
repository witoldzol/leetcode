-- https://leetcode.com/problems/product-sales-analysis-i/description/
select p.product_name, s.year, s.price from Product as p
right join Sales s on p.product_id = s.product_id
