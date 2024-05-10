select s1.score, 
count(distinct s2.score)as rank
from scores s1
inner join scores s2 on s1.score <= s2.score
group by s1.id, s1.score
order by rank asc

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores
    # rank the scores
    df['rank'] = df['score'].rank(method='dense', ascending=False)
    return df.sort_values(by='score', ascending=False)[['score','rank']]
