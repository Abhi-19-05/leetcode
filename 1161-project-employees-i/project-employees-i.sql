# Write your MySQL query statement below
SELECT project_id, round(sum(experience_years )/count(E.employee_id),2) as average_years 
FROM Project  as P 
join Employee  as E on E.employee_id=P.employee_id
group by project_id