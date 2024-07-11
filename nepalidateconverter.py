import datetime
import datetime_nepali
year = int(input("Enter Nepali year: "))
month = int(input("Enter Nepali month: "))
day = int(input("Enter Nepali day: "))
date = datetime_nepali.date(year, month, day).to_datetime_date()
print(f"English date is: {date}")