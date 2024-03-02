-- https://leetcode.com/problems/rising-temperature/description/
select id from Weather w1
where temperature > (select temperature from Weather where recordDate = w1.recordDate - 1 )
