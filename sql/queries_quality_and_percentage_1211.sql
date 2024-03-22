-- https://leetcode.com/problems/queries-quality-and-percentage/description/
select query_name, 
round(
    sum(rating*1.0/position)/count(*)
    ,2
) as quality,
round(
    (count(case when rating < 3 then 1 else NULL end) * 100.00) / count(*)
    ,2
) as poor_query_percentage
from (select distinct * from Queries) as outside
group by query_name
having query_name is not null
