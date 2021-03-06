import os
from datetime import date, datetime

from app import app

BASEDIR = os.getcwd().split("\\")[-1]
ERROR_MSG = "Invalid {0} <{1}>"


def _raise_error(time, value):
    raise ValueError(ERROR_MSG.format(time, value))


def validate(value, time="year"):
    if time not in ["year", "month", "day"]:
        raise ValueError(f"Invalid <{time}> choose 'year', 'month', 'day'")
    if time == "year":
        if value not in range(1900, datetime.now().year + 1):
            _raise_error(time, value)
    elif time == "month":
        if value not in range(1, 13):
            _raise_error(time, value)
    elif time == "day":
        if value not in range(1, 32):
            _raise_error(time, value)
    return value


def get_year():
    year = int(input("Enter Year"))
    return validate(value=year, time="year")


def get_month():
    month = int(input("Enter Month"))
    return validate(value=month, time="month")


def get_day():
    day = int(input("Enter day"))
    return validate(value=day, time="day")


def get_birthday():
    year = get_year()
    month = get_month()
    day = get_day()
    print(f"It is looks like you born in {day}/{month}/{year}")
    return date(year=year, month=month, day=day)


def days_in_between(start_date, end_date):
    # you can get the seconds , then convert from seconds to days
    delta = start_date - end_date
    days = delta.days
    # in case of Programmer swap the dob with today (it is ok to show days in positive values)
    if days < 0:
        days = -days  # the same of -1 * days (pure python)
    return days


def main():
    today = date.today()
    dob = get_birthday()
    print(f"Your age in days is {days_in_between(today, dob)} Days")


if __name__ == "__main__":
    app(BASEDIR)
    main()
