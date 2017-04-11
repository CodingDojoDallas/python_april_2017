/*1*/
select concat('$',format(sum(amount),2)) as total_rev_mar_2017
from billing
where year(charged_datetime)=2012 and month(charged_datetime)=3;

/*2*/
select concat('$',format(sum(amount),2)) as total_rev_id_2
from billing
where client_id=2;

/*3*/
select domain_name 
from sites 
where client_id=10;

/*4*/
select count(domain_name), year(created_datetime) as year, 
month(created_datetime) as month
from sites
where client_id=1
group by year, month;

select count(domain_name), year(created_datetime) as year, 
month(created_datetime) as month
from sites
where client_id=20
group by year, month;

/*5*/
select count(leads_id) as total_num_leads, domain_name
from leads as l
join sites as s on l.site_id = s.site_id
where date(l.registered_datetime) between '2011-01-01' and '2011-02-15'
group by domain_name;


/*6*/
select count(leads_id) as total_num_leads, concat(c.first_name, " ",c.last_name) as client_name
from leads as l
join sites as s on l.site_id = s.site_id
join clients as c on s.client_id=c.client_id
where date(l.registered_datetime) between '2011-01-01' and '2011-12-31'
group by client_name;

/*7*/
select count(leads_id) as total_num_leads, 
concat(c.first_name, " ",c.last_name) as client_name,
year(l.registered_datetime) as year, month(l.registered_datetime) as month 
from leads as l
join sites as s on l.site_id = s.site_id
join clients as c on s.client_id=c.client_id
where date(l.registered_datetime) between '2011-01-01' and '2011-12-31'
group by client_name, year, month;
