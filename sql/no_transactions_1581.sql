-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
select v.customer_id, count(v.customer_id) as count_no_trans from Visits v
left join Transactions t on t.visit_id = v.visit_id
where t.transaction_id is NULL
group by v.customer_id


-- pandas
def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, how='left', on='visit_id')
    df = df[df['transaction_id'].isna()]
    df = df.groupby(['customer_id'])['visit_id'].count().reset_index()
    return df.rename({'visit_id':'count_no_trans'}, axis=1)
