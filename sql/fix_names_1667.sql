-- https://leetcode.com/problems/fix-names-in-a-table/description/
select user_id, upper(left(name, 1)) || substring(lower(name) from 2) as name from Users
order by user_id
