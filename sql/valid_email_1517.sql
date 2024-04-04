-- https://leetcode.com/problems/find-users-with-valid-e-mails/description/
select * from Users
where mail ~ '^[[:alpha:]]+[A-Za-z0-9\-\.\_]*@leetcode\.com$'

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z]+[a-zA-Z0-9\.\-_]*@leetcode\.com$'
    filtered = users[users['mail'].str.match(pattern)]
    return filtered
