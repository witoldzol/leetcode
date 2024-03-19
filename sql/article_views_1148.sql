-- https://leetcode.com/problems/article-views-i/description/
select distinct author_id as id from Views
where viewer_id = author_id
order by author_id asc
