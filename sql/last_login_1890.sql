-- https://leetcode.com/problems/the-latest-login-in-2020/description/
select user_id, max(time_stamp) as last_stamp from Logins
where time_stamp >= '2020-01-01' and time_stamp <= '2020-12-31'
group by user_id
having max(time_stamp) is not null
