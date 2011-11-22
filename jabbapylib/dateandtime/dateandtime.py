#!/usr/bin/env python

# from jabbapylib.dateandtime.dateandtime import get_timestamp_from_year_to_second

from datetime import datetime
import time


def get_timestamp_from_year_to_second(separator=False, date=None):
    """A compact timestamp.
    
    Example: 20110523_234401 . date can be a datetime object.
    If date is not specified, the current date and time (now) will be used."""
    if date:
        now = date
    else:
        now = datetime.now()
    date = datetime.date(now)
    time = datetime.time(now)
    #return "%d-%02d-%02d @ %02dh%02d%02d" % (date.year, date.month, date.day, time.hour, time.minute, time.second)
    template = "{year}{month:02}{day:02}_{hour:02}{minute:02}{second:02}"
    if separator:
        template = "{year}_{month:02}_{day:02}_{hour:02}{minute:02}{second:02}"
    return template.format(year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute, second=time.second)
    
    
def get_date_from_year_to_day():
    """A simplified timestamp.
    
    Example: 2011_10_29 ."""
    now = datetime.now()
    date = datetime.date(now)
    return "{year}_{month:02}_{day:02}".format(year=date.year, month=date.month, day=date.day)


def datetime_to_unix_timestamp(date):
    """Convert a datetime to Unix timestamp.
    
    date is a datetime object, the return value is an int."""
    # http://stackoverflow.com/questions/2775864/python-datetime-to-unix-timestamp
    return int(time.mktime(date.timetuple()))


def unix_timestamp_to_datetime(timestamp):
    """Convert a Unix timestamp to datetime.
    
    The return value is a datetime object."""
    # http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python
    return datetime.fromtimestamp(timestamp)
    
#############################################################################
    
if __name__ == "__main__":
    print get_timestamp_from_year_to_second(separator=True)
    print get_date_from_year_to_day()
    now = datetime.now()
    print datetime_to_unix_timestamp(now)
    ts = 1111111111
    dt = unix_timestamp_to_datetime(ts)
    print dt
    print get_timestamp_from_year_to_second(date=dt)
