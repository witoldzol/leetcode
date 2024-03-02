https://leetcode.com/problems/game-play-analysis-i/description/
-- first attempt using sub-query
select player_id, event_date as first_login from Activity a1
where event_date <= all ( select event_date from Activity a2 where a1.player_id = a2.player_id)
-- using group by
select player_id, min(event_date) as first_login from Activity
group by player_id
