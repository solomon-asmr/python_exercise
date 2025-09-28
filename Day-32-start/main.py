from datetime import datetime
import pandas as pd
import random
import smtplib
my_email = "myemail@gmail.com"
password = "app password you got from gmail account"
today = datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(int(data_row["month"]), int(data_row["day"])): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")
        

'''
to run the python code in the cloud
---------------------------------------------------
go to pythonAnywhere and signup with free tier
click the files tab
    upload your files one by one like
    -main.py
    -birthdays.csv
    then create directory name "letter_templates" and upload
        -letter_1.txt
        -letter_2.txt
        -letter_3.txt
go to consoles and click Bash 
    then on the console write python main.py
    --you may see smtplib authentication error
    just copy https://support.google.com/mail/answer/78754
    then click th the https://www.google.com/accounts/displayUnlockCaptcha
    click continue
    then go back to console and write python3 main.py

    to schedule a task go to Tasks and clik on it
    write the same command  python3 main.py and schedule at a particular time as you want

'''
