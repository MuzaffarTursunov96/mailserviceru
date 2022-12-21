import datetime


yesterday = datetime.date.today() - datetime.timedelta(days=1)
today_start=datetime.date.today()

print(yesterday,today_start)
