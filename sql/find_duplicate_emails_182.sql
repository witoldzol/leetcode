-- https://leetcode.com/problems/duplicate-emails/
select email as Email from Person
group by email
having count(email) > 1
-- alternative 
select distinct p1.email from person p1, person p2
where p1.id <> p2.id and p1.email=p2.email
