select id,
       case
           when p_id is null then 'Root'
           when p_id is not null and (select count(*) from tree where p_id = tree_outer.id) > 0 then 'Inner'
           else 'Leaf'
           end as type
from tree tree_outer;