import smtplib, os, datetime as dt, pandas as pd, random
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today = (now.month, now.day)
current_time_tuple = (now.hour, now.minute, now.second)

birthday_dataframe = pd.read_csv("birthdays.csv")
birthdays = birthday_dataframe.to_dict(orient="records")
for birthday in birthdays:
    if (birthday["month"], birthday["day"]) == today:
        letter_index = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_index}.txt", "r") as file:
            letter_template = file.read()
            letter = letter_template.replace("[NAME]", birthday["name"].title())

        with smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=20) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs=birthday["email"], from_addr=MY_EMAIL, msg=f"Subject:Happy birthday!\n\n{letter}")
            connection.close()
