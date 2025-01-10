with prepared_data as (select visited_on,
                              visited_on - 6 week_before,
                              amount
                       from customer),
     aggregated_data as (select distinct visited_on,
                                         (select sum(amount)
                                          from customer
                                          where visited_on between prepared_data.week_before and prepared_data.visited_on) amount
                         from prepared_data
                         where
                             week_before in (select distinct visited_on from customer))
select visited_on, amount, round(amount::numeric / 7, 2) as average_amount
from aggregated_data;
