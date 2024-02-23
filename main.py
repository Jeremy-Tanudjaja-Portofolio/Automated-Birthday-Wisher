import smtplib
import random
import datetime as dt
import pandas

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birthday_data_frame = pandas.read_csv("birthdays.csv")
birthday_list = birthday_data_frame.iterrows()

# 2. Check if today matches a birthday in the birthdays.csv
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day
for data in birthday_list:
    for data_row in range(1, len(data)):
        if (data[data_row]["month"] == current_month) and (data[data_row]["day"] == current_day):
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
            # person's actual name from birthdays.csv

            letter_choice = f"letter_{random.randint(1, 3)}.txt"
            with open(f"letter_templates/{letter_choice}", "r") as letter_template:
                letter = letter_template.read().replace("[NAME]", f"{data[data_row]['name']}")

            # 4. Send the letter generated in step 3 to that person's email address.

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="user@gmail.com", password="password")
                connection.sendmail(from_addr="user@gmail.com",
                                    to_addrs=f"{data[data_row]['email']}",
                                    msg=f"Subject: Happy Birthday {data[data_row]['email']}\n\n{letter}")
