# Write your MySQL query statement below
# Write your MySQL query statement below
select  
case when max(salary) =null then null
     else max(salary)
  end as SecondHighestSalary 
from Employee
where salary not in (
    select max(salary) 
    from Employee
)
order by salary 