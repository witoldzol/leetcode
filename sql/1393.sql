-- https://leetcode.com/problems/capital-gainloss/description/
select  stock_name, (total_sell - total_buy) as capital_gain_loss from
(
  select stock_name, sum(buy) total_buy, sum(sell) total_sell from
  (
    select
    stock_name,
    case 
    when operation = 'Buy' then price
    end as buy,
    case 
    when operation = 'Sell' then price
    end as sell
    from Stocks
  )
  group by stock_name
)
