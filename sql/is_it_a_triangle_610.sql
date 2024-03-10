-- https://leetcode.com/problems/triangle-judgement/submissions/1199360172/
select *, CASE
  WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
  ELSE 'No'
END as 'triangle'
from Triangle


