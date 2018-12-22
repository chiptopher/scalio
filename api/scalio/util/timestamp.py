import datetime

from pytz import timezone


def convert_date_to_timestamp(date: str):
    return round(datetime.datetime.strptime(date, "%Y-%m-%d")
                 .replace(tzinfo=timezone('UTC'))
                 .timestamp()*1000)


def time_in_millis(time_to_convert: datetime.datetime = datetime.datetime.utcnow(),
                   delta: datetime.timedelta = datetime.timedelta(days=0)):
    time_minus_delta = (time_to_convert - delta)
    timestamp = time_minus_delta.timestamp()
    return round(timestamp * 1000)
