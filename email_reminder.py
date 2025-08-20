import smtplib
from email.mime.text import MIMEText
from datetime import datetime




reminders = {
    "08-19": "Meeting at 3PM"

}


today = datetime.now().strftime("%m-%d")
print(today)


if today in reminders:
    message = reminders[today]


    email_sender = "khadija.codencoit@gmail.com"
    Email_reciver = "khadija.khatun@codencoit.com"
    password = "erws ccfb gzwh nhip"


    msg = MIMEText(message)
    msg["Subject"] = "Reminder Notification"
    msg["From"] = "Khadija Khatun"
    msg["To"] = Email_reciver


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_sender, password)
        server.sendmail(email_sender, Email_reciver, msg.as_string())
    print("eminder sent successfully!")
else:
    print("No reminders for this time.")

   