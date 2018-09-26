import datetime
import time

s = '1526228086'

def ms_to_datetime(t):
    return datetime.datetime.fromtimestamp(int(t)/1000.0)


print(ms_to_datetime(s))



def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

