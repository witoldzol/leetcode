-- using cross join ( cartesian product )
delete from Person where id in (select p1.id from Person p1, Person p2
where p1.email = p2.email and p1.id > p2.id)
-- using self join
delete from Person where id in (
    select p1.id from Person p1
    join Person p2 on p1.email = p2.email
    where p1.id > p2.id
)
