import settings
import emailsender
import re
import csv

def main():
    cemail = input("Enter email address linked with account: ")
    r1 = re.compile("@gmail\.com")
    if r1.search(cemail):
        with open('accountlist.csv','r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if cemail == row[2]:
                    settings.confirmemailpin()
                    settings.CName = row[0]
                    settings.CEmail = row[2]
                    settings.random()
                    emailsender.forgetemail()
                    forgetpin()
                elif cemail != row[2]:
                    wrong = input("Invalid email. Please try again").title()
                    if wrong == "M":
                        main()
    elif bool(r1.search(cemail)) == False:
        print("Please retype email address")
        main()

def forgetpin():                    
        forgetpin = input("Enter confirmation number: ")
        actualpin = str(settings.pin)
        if forgetpin == actualpin:
            print("Success.")
            newpass = input("Enter new password: ")
            newpass = input("Verify new password: ")
        elif forgetpin != actualpin:
            print("Incorrect pin. Please try again. ")
            forgetpin()

