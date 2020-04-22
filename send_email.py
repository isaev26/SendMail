import smtplib
import ssl
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(mail):
    serv = smtplib.SMTP_SSL('smtp.yandex.ru', '465')
    serv.login("salatik3392@yandex.ru", "Atos2018*")
    serv.set_debuglevel(1)
    email = "salatik3392@yandex.ru"
    msg = MIMEMultipart('alternative')

    for name, mail in mail.items():
        text = "Hi! " + name + "\nHow do you do?\n"
        html = """\
        <html>
        <head></head>
        <body>
            <h2>Hi! """ + name + """</h2> <br>
            <p>How do you do?<br></p>
        </body>
        </html>
        """
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        msg['Subject'] = "Python message for " + name
        msg['From'] = email
        msg['To'] = mail
        serv.sendmail(email, mail, msg.as_string())
    serv.quit()


def emails():
    email = {}
    f = open('emails.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    for name, mail in reader:
        email.update({name: mail})
    return email


if __name__ == "__main__":

    mail = emails()
    send(mail)
