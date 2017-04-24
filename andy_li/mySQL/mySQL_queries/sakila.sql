-- 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.

select city.city_id, city.city, concat_ws(" ", customer.first_name, customer.last_name) as customer_name, customer.email, concat_ws(" ", address.address, address.address2) as address from customer
join address on address.address_id = customer.address_id
join city on city.city_id = address.city_id
where city.city_id = 312;

-- 2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name from film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
where category.name like "comedy";

-- 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.

select actor.actor_id, concat_ws(" ", actor.first_name, actor.last_name) as actor_name, film.title, film.description, film.release_year from actor
join film_actor on film_actor.actor_id = actor.actor_id
join film on film.film_id = film_actor.film_id
where actor.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.

select store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, concat_ws(" ", address.address, address.address2) as address from customer
join address on address.address_id = customer.address_id
join city on city.city_id = address.city_id
join store on store.store_id = customer.store_id
where store.store_id = 1 and city.city_id in (1, 42, 312, 459);

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.

select film.title, film.description, film.release_year, film.rating, film.special_features from film
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where film.rating like "G" and film.special_features like "behind the scenes" and actor.actor_id = 15;

-- 6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.

select film.film_id, film.title, actor.actor_id, concat_ws(" ", actor.first_name, actor.last_name) as actor_name from film
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where film.film_id = 369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).

select film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name, film.rental_rate from film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
where category.name like "drama" and film.rental_rate = 2.99;

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, concat_ws(" ", actor.first_name, actor.last_name) as actor_name from film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where category.name like "action" and actor.first_name like "Sandra" and actor.last_name like "Kilmer";
