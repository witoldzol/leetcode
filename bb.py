import datetime


def count_years(birthday: str) -> int:
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    birthday_day_of_a_week = birthday_dt.weekday()
    i = 1
    while True:
        year = birthday_dt.year + i
        try:
            next_year = datetime.datetime(year, birthday_dt.month, birthday_dt.day)
        except Exception:
            i += 1
            continue
        if next_year.weekday() == birthday_day_of_a_week:
            print(next_year)
            return i
        i += 1


print("years: ", count_years("1982-05-22"))
