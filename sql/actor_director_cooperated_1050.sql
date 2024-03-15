-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/
select actor_id, director_id from ActorDirector ad
group by actor_id, director_id
having count(timestamp) > 2
