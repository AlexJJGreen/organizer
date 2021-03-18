from calendar import Calendar
from datetime import date

TODAY = date.today()
CALENDAR = Calendar()

def get_month(current_month):
    month = list((day for day in CALENDAR.itermonthdays(current_month.year,current_month.month)))
    return month


