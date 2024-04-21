  -- https://leetcode.com/problems/rearrange-products-table/
  select a.product_id, 'store1' as store, store1 as price from Products a
  where store1 is not null
  union
  select a.product_id, 'store2' as store, store2 as price from Products a
  where store2 is not null
  union
  select a.product_id, 'store3' as store, store3 as price from Products a
  where store3 is not null
