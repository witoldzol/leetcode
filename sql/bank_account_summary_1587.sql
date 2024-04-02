-- https://leetcode.com/problems/bank-account-summary-ii/description/
select u.name as NAME, sum(t.amount) as BALANCE from Transactions t
join Users u on t.account = u.account
group by u.name, t.account
having sum(amount) > 10000


-- pandas
