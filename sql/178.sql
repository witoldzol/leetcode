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

-- my pandas solution
import pandas as pd
rank: int = 1
current_score = None

def rank_rows(row):
    global rank
    global current_score
    if current_score is None:
        current_score = row['score']
    if row['score'] == current_score:
        return rank
    else:
        current_score = row['score']
        rank = rank + 1
        return rank

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores
    df = df.sort_values(by='score', ascending=False)
    df['rank'] = df.apply(rank_rows, axis=1)
    return df[['score', 'rank']]
