with categories as (select case
                               when income < 20000 then 'Low Salary'
                               when income between 20000 and 50000 then 'Average Salary'
                               when income > 50000 then 'High Salary'
                               end as category,
                           1       as total_count
                    from accounts),
     all_categories as (select category, total_count
                        from (values ('Low Salary', 0),
                                     ('Average Salary', 0),
                                     ('High Salary',
                                      0)) as dummy_data(category, total_count)),
     union_categories as (select category, total_count
                          from all_categories
                          union all
                          select category, total_count
                          from categories),
     aggregated_all_categories as (select category, sum(total_count) as accounts_count
                                   from union_categories
                                   group by category)
select * from aggregated_all_categories;