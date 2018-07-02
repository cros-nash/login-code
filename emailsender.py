import settings
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def confirms():
    settings.search()
    me = "automation_email"
    my_password = r"automation_password"
    you = (settings.ema)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirmation number"
    msg['From'] = me
    msg['To'] = you


    html = """\
    <html>
    <body>
     <p>Hello {userna},
     </p>
     <p>Your confirmation code is: {pin}
     </p>
    </body>
    </html>""".format(pin=settings.pin,userna=settings.new)
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    print("Sent!")

def lastemail2():
    settings.search()
    me = "automation_email"
    my_password = r"automation_password"
    you = (settings.ema)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Account credentials"
    msg['From'] = me
    msg['To'] = you

    html = """\
   <html>
    <body>
     <p>Your account credentials are:
     </p>
     <p>USERNAME: {user}
     </p>
     <p>PASSWORD: {passd}
     </p>
     <p>EMAIL: {email}
     </p>
    </body>
    </html>""".format(user=settings.us,passd=settings.pa,email=you)
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    print("Sent!")

def lastemail():
    settings.search()
    me = "automation_email"
    my_password = r"automation_password"
    you = (settings.userem)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Account credentials"
    msg['From'] = me
    msg['To'] = you

    html = """\
   <html>
    <body>
     <p>Your account credentials are:
     </p>
     <p>USERNAME: {user}
     </p>
     <p>PASSWORD: {passd}
     </p>
     <p>EMAIL: {email}
     </p>
    </body>
    </html>""".format(user=settings.userna,passd=settings.userpa,email=you)
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')

    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    print("Sent!")

def forgetemail():
    settings.search()
    me = "automation_email"
    my_password = r"automation_password"
    you = (settings.CEmail)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirmation number"
    msg['From'] = me
    msg['To'] = you


    html = """\
    <html>
    <body>
     <p>Hello {userna},
     </p>
     <p>Your confirmation code is: {pin}
     </p>
    </body>
    </html>""".format(pin=settings.pin,userna=settings.CName)
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    print("Sent!")
