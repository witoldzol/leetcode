-- https://leetcode.com/problems/calculate-special-bonus/
select employee_id, 
case 
    when employee_id % 2 != 0 and left(name,1) != 'M' then salary
    else 0
end as bonus
from Employees
order by employee_id


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def is_bonus(id: str, name: str):
        return int(id) % 2 != 0 and name[0] != 'M'
    df = employees
    df = df.assign(
        bonus=df.apply(lambda x: x['salary'] 
            if is_bonus( x['employee_id'], x['name']) 
            else 0,
        axis=1)
    )
    sorted = df.sort_values(by='employee_id') 
    return sorted[['employee_id', 'bonus']]
