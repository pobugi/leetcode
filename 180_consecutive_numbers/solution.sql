with data as (select *,
                     (select num = logs_outer.num
                      from logs
                      where id = logs_outer.id - 1) before,
                     (select num = logs_outer.num
                      from logs
                      where id = logs_outer.id + 1) after
              from logs logs_outer)
select
    *
from data where before or after;

select
    distinct num ConsecutiveNums
from logs
where
    (id + 1, num) in (select id, num from logs)
    and (id + 2, num) in (select id, num from logs)
