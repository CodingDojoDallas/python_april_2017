use twitter;
select concat(first_name, last_name) as Name from users as u
join tweets as t on t.user_id = u.id
where (select count(t.tweet), t.id from t group by t.id where avg(count(t.tweet));