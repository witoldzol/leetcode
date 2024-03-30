-- https://leetcode.com/problems/group-sold-products-by-the-date/description/
select a.sell_date,
count(distinct a.product) as num_sold, 
array_to_string(array_agg(distinct a.product), ',') as products
from Activities as a
group by a.sell_date
