-- # Write your MySQL query statement below
(select m.title as results
from MovieRating mr 
join Movies m on m.movie_id = mr.movie_id
where mr.created_at like "2020-02-%"
group by mr.movie_id
order by avg(mr.rating) desc, m.title
limit 1) union all
(select u.name as results
from MovieRating mr 
join Users u on u.user_id = mr.user_id
group by mr.user_id 
order by count(mr.user_id) desc, u.name
limit 1)