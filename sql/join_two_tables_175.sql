-- https://leetcode.com/problems/combine-two-tables/
-- postgresql
select firstName, lastName, city, state from Person as p
left join Address as a using(personId)
