-- https://leetcode.com/problems/invalid-tweets/description/
select tweet_id from Tweets
where length(content) > 15

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    fil = tweets[tweets['content'].str.len() > 15]
    return fil['tweet_id'].to_frame()
    
