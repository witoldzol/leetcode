select coalesce(first_name, 'na') || ' ' || c.last_name, p.product_name, (select sum(quantity) from items), sum(it.quantity) as sum_per_item from customers c
join invoices i on i.customer_id = i.invoice_id
full join items it on it.invoice_id = i.invoice_id
right join Products p on p.product_id = it.product_id
group by c.first_name || c.last_name, product_name
