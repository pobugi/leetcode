with distinct_producs as (select distinct product_id
                          from products)

select product_id,
       coalesce(coalesce(
                        (select new_price
                         from products
                         where product_id = distinct_producs.product_id
                           and change_date = '2019-08-16'),
                        (select new_price
                         from products
                         where product_id = distinct_producs.product_id
                           and change_date <= '2019-08-16'
                         order by change_date desc
                         limit 1)
                ), 10)
from distinct_producs;