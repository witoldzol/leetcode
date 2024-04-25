-- https://leetcode.com/problems/the-latest-login-in-2020/description/
with
extracted as (
    select
        user_id,
        time_stamp,
        extract(year from time_stamp) as year
    from Logins
),
extracted_year as (
    select
        user_id,
        time_stamp
    from extracted
    where year = 2020
),
final as (
    select
        user_id,
        max(time_stamp) as last_stamp
    from extracted_year
    group by user_id
)
select * from final

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
   filtered = logins[logins['time_stamp'].dt.year == 2020]
   df = filtered.groupby('user_id')['time_stamp'].max().rename('last_stamp').reset_index()
   return df
