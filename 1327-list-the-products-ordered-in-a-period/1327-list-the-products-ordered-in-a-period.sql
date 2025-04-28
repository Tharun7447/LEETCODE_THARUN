# Write your MySQL query statement below
select product_name ,sum(unit) unit from products p
inner join orders o
on p.product_id = o.product_id
where date_format(order_date, '%Y-%m')='2020-02'
group by product_name
having unit >= 100