-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/
select activity_date as day, count(distinct user_id) as active_users from Activity
where activity_date between TO_DATE('2019-07-27', 'YYYY-MM-DD') - INTERVAL '30 days' and '2019-07-27'
group by activity_date


import pandas as pd
def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby('reports_to', as_index=False).agg(reports_count=('name', 'count'), average_age=('age', 'mean'))
    df = df.merge(employees, how='left', left_on='reports_to', right_on='employee_id')
    df = df[['reports_to_x', 'name', 'reports_count', 'average_age']]
    df = df.rename(columns={'reports_to_x': 'employee_id'})
    df['average_age'] = round(df['average_age'] + 0.1)
    return df
    
