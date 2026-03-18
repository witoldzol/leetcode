from datetime import datetime, timedelta


def how_many_years(bd: str) -> int:
    dt = datetime.strptime(bd, "%m-%d-%Y")
    year = dt.year
    month = dt.month
    day = dt.day
    target_day = dt.weekday()
    print("target day ", target_day)
    count = 1
    while True:
        try:
            next_year = datetime(year + count, month, day)
        except ValueError as e:
            print(e)
            count += 1
            continue
        new_day = next_year.weekday()
        if target_day == new_day:
            return count
        count += 1


print(how_many_years("2-29-2008"))
