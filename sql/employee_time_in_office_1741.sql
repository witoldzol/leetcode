-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/
select event_day as day,
emp_id,
sum(out_time - in_time) as total_time
from Employees
group by emp_id, event_day

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(['emp_id','event_day'])[['in_time','out_time']].sum().reset_index()
    df['total_time'] = df['out_time'] - df['in_time']
    df.rename(columns={'event_day': 'day'}, inplace=True)
    return df[['day','emp_id','total_time']]
