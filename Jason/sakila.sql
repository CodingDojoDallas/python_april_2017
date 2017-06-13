/*Customers inside city_id=32*/
select first_name, last_name, email, address
from customer as cu
join address as ad on cu.address_id=ad.address_id
where ad.city_id= 312;

/*All comedy films*/
select f.title, f.description, f.release_year, f.special_features
from film as f
join film_category as fc on f.film_id = fc.film_id
join category as ca on fc.category_id = ca.category_id
where ca.name = 'Comedy';

/*Actor*/
select ac.actor_id, concat(ac.first_name,' ',ac.last_name) as actor_name, f.title, f.description,f.release_year
from actor as ac
join film_actor as fa on ac.actor_id = fa.actor_id
join film as f on fa.film_id = f.film_id
where ac.actor_id=5;

/*Store & Customer*/
select cu.first_name,cu.last_name,cu.email,cu.address_id
from customer as cu 
join address as ad on cu.address_id=ad.address_id
join store as so on ad.address_id=so.address_id
where so.store_id=1 and ad.city_id in (1,42,312,459);


/*Rating, Feature, and Actor*/
select f.title, f.description, f.release_year, f.special_features
from film as f
where rating ='G' and
special_features like '%behind the scenes%';


