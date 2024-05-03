-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher
    df = df.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df = df.rename(columns={'subject_id': 'cnt'})
    return df
    
