# Write your MySQL query statement below
-- update Users
-- set name =  CONCAT(
    -- UPPER(LEFT(name, 1)),
    -- LOWER(SUBSTRING(name, 2)))
select user_id ,concat(upper(left(name,1)), lower(substring(name,2))) as name
from Users
order by user_id asc
