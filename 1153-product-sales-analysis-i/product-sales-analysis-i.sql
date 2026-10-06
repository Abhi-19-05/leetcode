# Write your MySQL query statement below
SELECT product_name,year ,price
FROM Sales AS S
JOIN Product AS P ON P.PRODUCT_ID=S.PRODUCT_ID