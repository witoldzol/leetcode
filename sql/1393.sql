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

-- alternative solution

-- group sell & buy per each company
with operation_sums as 
(
    select stock_name, operation, sum(price) as price
    from stocks
    group by stock_name, operation
)
-- calculate difference
select stock_name, 
(
  sum ( case when operation = 'Sell' then price else 0 end)
  -
  sum ( case when operation = 'Buy' then price else 0 end)
) as capital_gain_loss
from operation_sums
group by stock_name 

-- pandas
def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
  df = stocks
  df = df.apply(buysell, axis=1).reset_index()
  df = df.groupby('stock_name')['price'].sum().reset_index()
  return df.rename(columns={'price': 'capital_gain_loss'})
