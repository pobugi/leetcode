select
    id,
    coalesce(case
        when id % 2 <> 0 then (select student from seat where id = seat_outer.id + 1)
        when id % 2 = 0 then (select student from seat where id = seat_outer.id - 1)
    end, student) as student
from seat seat_outer;