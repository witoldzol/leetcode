-- https://leetcode.com/problems/daily-leads-and-partners/submissions/1226415157/
select date_id,
make_name,
count(distinct lead_id) as unique_leads,
count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales \
        .groupby(['date_id', 'make_name'])[['lead_id', 'partner_id']] \
        .nunique() \
        .reset_index()
    return df.rename(columns={'lead_id':'unique_leads', 'partner_id': 'unique_partners'})

