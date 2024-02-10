select *
from patients

where case
          when conditions ilike 'diab1%' then conditions ilike 'diab1%'
          else conditions ilike '% diab1%' end
;