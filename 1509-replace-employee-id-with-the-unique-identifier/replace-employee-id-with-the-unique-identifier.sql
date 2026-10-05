# Write your MySQL query statement 
SELECT unique_id, name
FROM   Employees AS E 
LEFT JOIN  EmployeeUNI AS E1 ON E1.id=E.id
