-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/
select activity_date as day, count(distinct user_id) as active_users from Activity
where activity_date between TO_DATE('2019-07-27', 'YYYY-MM-DD') - INTERVAL '30 days' and '2019-07-27'
group by activity_date
