(select users.name as results
 from movierating
          inner join users on movierating.user_id = users.user_id
 group by movierating.user_id, users.name
 order by count(*) desc, users.name
 limit 1)
union all
(select m.title as results
 from movierating
          inner join movies m on movierating.movie_id = m.movie_id
 where to_char(created_at, 'YYYY-MM') = '2020-02'
 group by movierating.movie_id, m.title
 order by avg(rating) desc, m.title
 limit 1)
;