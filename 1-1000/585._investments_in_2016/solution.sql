select
    round(sum(tiv_2016)::numeric, 2) as tiv_2016
from insurance insurance_outer
where
    tiv_2015 in (select distinct tiv_2015 from insurance where pid <> insurance_outer.pid)
    and (lat, lon) not in (select distinct lat, lon from insurance where pid <> insurance_outer.pid);