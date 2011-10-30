#!/usr/bin/env python


from datetime import datetime


def get_timestamp_from_year_to_second(separator=False):
    """A compact timestamp.
    
    Example: 20110523_234401 ."""
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
    
#############################################################################
    
if __name__ == "__main__":
    print get_timestamp_from_year_to_second(separator=True)
    print get_date_from_year_to_day()