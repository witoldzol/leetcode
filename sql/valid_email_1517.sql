-- https://leetcode.com/problems/find-users-with-valid-e-mails/description/
select * from Users
where mail ~ '^[[:alpha:]]+[A-Za-z0-9\-\.\_]*@leetcode\.com$'
