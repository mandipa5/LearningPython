import datetime

birth_date = datetime.date(2000,9,25)
current_date = datetime.date.today()

age = current_date - birth_date

print(age)