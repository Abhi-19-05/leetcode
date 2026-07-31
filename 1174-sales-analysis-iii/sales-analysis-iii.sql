# Write your MySQL query statement below
select P.product_id , product_name
from Product as P
join Sales as S on S.product_id=P.product_id
group by P.product_id
having min(sale_date) >='2019-01-01' and max(sale_date)<='2019-03-31' 