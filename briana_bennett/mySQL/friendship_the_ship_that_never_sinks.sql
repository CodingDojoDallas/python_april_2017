-- use mydb;
-- insert into users (first_name, last_name)
-- values('Chris', 'Baker');
-- 
-- insert into users (first_name, last_name)
-- values('Diana', 'Smith');
-- 
-- insert into users (first_name, last_name)
-- values('James', 'Johnson');
-- 
-- insert into users (first_name, last_name)
-- values('Jessica', 'Davidson');

-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- values (1,3, now(), now());
-- 
-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- values (2,4, now(), now());
-- 
-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- values (3,1, now(), now());
-- 
-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- values (4,3, now(), now());
-- 
	-- insert into friendships (user_id, friend_id, created_at, updated_at)
-- 	values (4,1, now(), now());

select users.first_name, users.last_name, friend.first_name as friend_first_name, friend.last_name as friend_last_name from users
left join friendships on friendships.user_id = users.id
left join users as friend on friendships.friend_id = friend.id
order by friend_last_name desc;




