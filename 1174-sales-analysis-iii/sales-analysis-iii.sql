# Write your MySQL query statement below
select P.product_id , product_name
from Product as P
join Sales as S on S.product_id=P.product_id
group by P.product_id
having min(sale_date) >='2019-01-01' and max(sale_date)<='2019-03-31' 

-- SELECT p.product_id, p.product_name
-- FROM Product p
-- WHERE p.product_id NOT IN (
--     SELECT product_id
--     FROM Sales
--     WHERE sale_date < '2019-01-01'
--        OR sale_date > '2019-03-31'
-- )
