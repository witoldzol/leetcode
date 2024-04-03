-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/
select r.contest_id, 
round(
  count(r.user_id)/( (select count(*) from Users ) * 1.0 ),
  4
) * 100 as percentage from Register r
group by r.contest_id
order by percentage desc, r.contest_id asc
