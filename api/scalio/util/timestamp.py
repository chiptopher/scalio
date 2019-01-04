import datetime

from pytz import timezone


def convert_date_to_timestamp(date: str):
    return round(datetime.datetime.strptime(date, "%Y-%m-%d")
                 .replace(tzinfo=timezone('UTC'))
                 .timestamp()*1000)


def time_in_millis(time_to_convert: datetime.datetime = datetime.datetime.utcnow(),
                   delta: datetime.timedelta = datetime.timedelta(days=0)):
    return round((time_to_convert - delta).timestamp() * 1000)


def convert_date_to_different_day(date: str, days: int):
    return ''
