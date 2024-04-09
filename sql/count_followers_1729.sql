-- https://leetcode.com/problems/find-followers-count/description/
select user_id, count(follower_id) as followers_count 
from Followers
group by user_id
order by user_id asc


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby('user_id')['follower_id'].count().reset_index()
    df.rename(columns={'follower_id': 'followers_count'}, inplace=True)
    df.sort_values(by='user_id', ascending=True)
    return df
    
