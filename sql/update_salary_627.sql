-- https://leetcode.com/problems/swap-salary/description/
update salary set sex = 
case sex -- this works only because sex is an ENUM!
    when 'm' then 'f'
    else 'm'
end;
-- example with a non-enum value
update Salary
set salary = 
case 
when salary < 5000 then salary * 1.1
else salary
end;

