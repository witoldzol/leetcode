-- https://leetcode.com/problems/employees-with-missing-information/description/
select t.employee_id from 
(
    select * from Employees e
    full join Salaries s using(employee_id)
) t
where t.name is null or t.salary is null
order by t.employee_id asc

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df = df.merge(salaries, on='employee_id', how='outer')
    filtered = df[df['name'].isnull() | df['salary'].isnull()]
    ids = filtered['employee_id'].to_frame()
    sorted = ids.sort_values(by='employee_id', ascending=True)
    return sorted
