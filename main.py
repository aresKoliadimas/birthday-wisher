import smtplib
import datetime
import random

now = datetime.datetime.now()

with open("quotes.txt") as quotes:
    q_list = quotes.readlines()
    msg = random.choice(q_list)

if now.weekday == 0:
    my_email = "ariskoliadimas@gmail.com"
    password = "abcd1234()"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="blaubla@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{msg}"
        )
