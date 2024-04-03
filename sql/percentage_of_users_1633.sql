-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/
select r.contest_id, 
round(
  count(r.user_id)/( (select count(*) from Users ) * 1.0 ),
  4
) * 100 as percentage from Register r
group by r.contest_id
order by percentage desc, r.contest_id asc


-- pandas
def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    user_count = len(users) * 1.0
    df = register.groupby('contest_id')['user_id'].count().reset_index()
    df['percentage'] = round((df['user_id']/user_count) * 100, 2)
    df = df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    return df[['contest_id','percentage']]
