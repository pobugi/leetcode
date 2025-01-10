with salary_categories as (select account_id,
                                  case
                                      when income < 20000 then 'Low Salary'
                                      when income between 20000 and 50000
                                          then 'Average Salary'
                                      else 'High Salary'
                                      end as salary_category
                           from accounts),
     categories as (SELECT column1 AS category
                    FROM (VALUES ('Low Salary'),
                                 ('Average Salary'),
                                 ('High Salary')) AS dummy_data(column1))

select category, count(account_id) accounts_count
from categories
         left join salary_categories
                   on categories.category = salary_categories.salary_category
group by category
;