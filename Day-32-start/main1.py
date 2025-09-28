import random
import smtplib
import datetime as dt
import pandas as pd

now = dt.datetime.now()

day_of_week = now.weekday()
if day_of_week == 6:
    with open("quotes.txt", 'r') as data:
        all_quote = data.readlines()
        ready_quote = random.choice(all_quote)
        my_email = "your email"
        password = "app password you get from gmail"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="to_email@gmail.com",
                msg=f"Subject:Hello\n\n{ ready_quote }")

#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=1996, month=10, day=17)
# print(date_of_birth)
