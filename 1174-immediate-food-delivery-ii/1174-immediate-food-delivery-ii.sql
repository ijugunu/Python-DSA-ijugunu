# Write your MySQL query statement below
select round(sum(if(customer_pref_delivery_date=order_date,1,0))*100/count(customer_id),2) as immediate_percentage
from Delivery
where (customer_id,order_date) in (
select customer_id,min(order_date) as first_order_date
from Delivery
group by customer_id);