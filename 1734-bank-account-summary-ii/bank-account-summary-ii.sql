# Write your MySQL query statement below
select name, sum(amount) as balance
from Users as u
join Transactions as t on t.account=u.account
group by t.account 
having sum(amount)>10000