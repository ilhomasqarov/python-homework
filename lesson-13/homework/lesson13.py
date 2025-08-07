from datetime import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (birthdate.replace(year=today.year, month=today.month) - birthdate.replace(year=today.year, month=today.month-1)).days
if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months, and {days} days old.")

from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

# Next birthday year
next_birthday_year = today.year if (today.month, today.day) < (birthdate.month, birthdate.day) else today.year + 1
next_birthday = birthdate.replace(year=next_birthday_year)

days_until = (next_birthday - today).days
print(f"Days until your next birthday: {days_until}")

from datetime import datetime, timedelta

current_dt_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")

duration_hours = int(input("Enter meeting duration hours: "))
duration_minutes = int(input("Enter meeting duration minutes: "))

end_time = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

from datetime import datetime
import pytz

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
src_tz_str = input("Enter your current timezone (e.g., US/Eastern): ")
target_tz_str = input("Enter target timezone (e.g., Europe/London): ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
src_tz = pytz.timezone(src_tz_str)
target_tz = pytz.timezone(target_tz_str)

dt_src = src_tz.localize(dt)
dt_target = dt_src.astimezone(target_tz)

print("Converted time:", dt_target.strftime("%Y-%m-%d %H:%M %Z"))


import time
from datetime import datetime

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future - now
    if remaining.total_seconds() <= 0:
        print("Countdown finished!")
        break
    days, seconds = remaining.days, remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print(f"Time remaining: {days}d {hours}h {minutes}m {seconds}s", end='\r')
    time.sleep(1)


import re

email = input("Enter an email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")


phone = input("Enter 10-digit phone number (digits only): ").strip()

if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number input.")


import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password)):
    print("Strong password!")
else:
    print("Weak password. Must be at least 8 chars, include uppercase, lowercase, and digits.")

