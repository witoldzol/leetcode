-- not working
delete from Person where id in (select p1.id from Person p1
join Person p2 on p1.email=p2.email
where p1.id != p2.id and p2.id > p1.id)
