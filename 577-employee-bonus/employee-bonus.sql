# Write your MySQL query statement below
SELECT name , bonus
FROM Employee as E
left  join Bonus  as B on B.empId =E.empId 
where bonus <1000 or  bonus is null