-- https://leetcode.com/problems/primary-department-for-each-employee/description/
select employee_id, department_id
from Employee
where primary_flag='Y' 
or employee_id in
(   select employee_id from Employee 
    group by employee_id 
    having count(department_id) = 1 
)


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    df['dc'] = df.groupby('employee_id')['department_id'].transform('nunique')
    filtered = df[
        (df['primary_flag']=='Y') | 
        (df['dc'] == 1)
    ]
    return filtered[['employee_id', 'department_id']]
