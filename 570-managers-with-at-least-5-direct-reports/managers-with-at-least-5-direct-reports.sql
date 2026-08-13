# Write your MySQL query statement bel
SELECT 
    e.name
FROM 
    employee e
join employee as e1 on e1.managerId=e.id
group by e.id 
having count(*)>4

