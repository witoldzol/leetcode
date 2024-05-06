-- https://leetcode.com/problems/tree-node/description/
select id, 
case
   when p_id is null then 'Root'
   else
        case 
            when id in (select p_id from tree) then 'Inner'
            else 'Leaf'
        end
end as type
from tree
