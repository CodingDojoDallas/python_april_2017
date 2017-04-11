/*What countries speek Sloven? */
select countries.name, languages.language, languages.percentage 
from countries 
join languages on countries.id=languages.country_id
where (select languages.id from languages where languages.language='Slovene' limit 1)
order by languages.percentage;

/*Total number cities for each country*/
select c.name, count(ci.name) as total_number_of_cities
from countries as c
join cities as ci on c.id = ci.country_id
group by c.name
order by total_number_of_cities;

/*Mexico cities with more than 500000 population*/
select name from cities
where population < 500000
order by population;

/*Languages with percentage greater than 89%*/
select language from languages
where percentage > 89;

/*Countries with surface area below 501 and populaton greater than 100000*/
select name from countries
where surface_area < 501 and population > 100000;

/*Countries with Constitutional Monarchy*/
select name from countries
where government_form='Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

/*Argentina*/
select ci.name, co.name 
from cities as ci
join countries as co on ci.country_id = co.id
where ci.district='Buenos Aires' and ci.population > 500000;

/*Countries by region*/
select count(name), region
from countries
group by region;









