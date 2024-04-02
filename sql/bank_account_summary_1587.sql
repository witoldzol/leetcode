-- https://leetcode.com/problems/bank-account-summary-ii/description/
select u.name as NAME, sum(t.amount) as BALANCE from Transactions t
join Users u on t.account = u.account
group by u.name, t.account
having sum(amount) > 10000


-- pandas
def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
   AMOUNT = 10_000 
   df = transactions.groupby(['account'])['amount'].sum().reset_index()
   filtered = df[df['amount'] > AMOUNT]
   df = filtered.merge(users, on='account')
   df = df[['name', 'amount']]
   return df.rename(columns={'name': 'NAME', 'amount': 'BALANCE'})
