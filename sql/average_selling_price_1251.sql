-- https://leetcode.com/problems/average-selling-price/description/
select p.product_id, 
coalesce(round(sum(
    (units)*price)
    /
    sum(((units*1.00))),2),0)
as average_price FROM Prices p
left join UnitsSold u on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id
