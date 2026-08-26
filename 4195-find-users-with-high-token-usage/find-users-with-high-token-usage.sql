# Write your MySQL query statement below
select user_id, 
       count(prompt) as prompt_count,
       round(sum(tokens) / count(tokens), 2) as avg_tokens 
from prompts
where user_id in (
    select user_id
    from prompts 
    group by user_id
    having count(*) >= 3
)
group by user_id
having max(tokens) > sum(tokens) / count(tokens)
order by avg_tokens desc, user_id asc;
