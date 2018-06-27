import settings
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def confirms():
    settings.search()
    me = "crosnash@gmail.com"
    my_password = r"Mondadori3"
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
    me = "crosnash@gmail.com"
    my_password = r"Mondadori3"
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
    me = "crosnash@gmail.com"
    my_password = r"Mondadori3"
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

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    print("Sent!")
