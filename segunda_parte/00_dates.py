### Dates ###

from datetime import datetime, time, date, timedelta

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date)

now = datetime.now()
print_date(now)

timestamp = now.timestamp() # timestamp es un float que representa la cantidad de segundos desde el 1 de enero de 1970
print(timestamp)

year_2025 = datetime(2025, 1, 1, 0, 0, 0)
print_date(year_2025)

current_time = time()
print(current_time)

current_date = date.today()
print(current_time)

time_delta = timedelta(days=1, hours=2, minutes=3, seconds=4)