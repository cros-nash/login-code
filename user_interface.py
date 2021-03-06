import csv # Imports CSV module, to be able to make tables
import smtplib # Imports module to be able to send emails
import re
# __init__.py file needs to be made to link python files
import emailsender # Imports emailsender.py
import settings # Imports settings file with global variables
import forget

# Sets all variables needed later to False

confirm = False
mame = False
done = False
done3 = False
name = False
email = False
passd = False

# Main starts all functions, and runs settings.py first

def code():
    pinc = input("Enter confirmation code, or press R to resend: ").title()
    actualpin = str(settings.pin)
    if pinc == actualpin:
        global confirm
        confirm == True
        global done
        done = True
        global username
        print("Correct code.")
        username = settings.new
        accounts = [settings.new,settings.pas,settings.ema]
        with open('accountlist.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(accounts) # Writes a row with name, password and email
        after()
        
    elif pinc == "R":
        settings.random()
        emailsender.confirms()
        code()
        
    elif pinc != actualpin:
        print("Wrong code, try again")
        code()
        
    else:
        print("Something went wrong...")
        main()

def valid():
    with open('accountlist.csv','r') as f: # Opens csv file and enables reader mode
        reader = csv.reader(f, delimiter=',') # Delimiter = space between each cell
        for row in reader:
            if settings.imame == row[0] or settings.imame == row[2]: # Checks if name or email is already made
                global mame # Global turns local variable to global vairable
                mame = True
                global username
                username = row[0]
                if settings.ipass == row[1]: # Compares name with password in same row
                    global passd
                    passd = True
                        
    if mame == False: # If username hasn't already been made
        confirm = input("Create new account? (Y/N), Forgot password? (F): ").title() # Asks to create new account, sets answer to capital
        
        if confirm == "Y":
            settings.newusername()
            print("Your confirmation code will be sent shortly")
            emailsender.confirms()
            code()
    
        elif confirm == "N":
            main()  # Re-does login process

        elif confirm == "F":
            forget.main()
        
        else:
            print("That is not a valid option")
            valid() # If wrong key pressed, re-does confirmation

    elif mame == True:
        with open('accountlist.csv','r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if settings.imame == row[0] or settings.imame == row[2]:
                    settings.done1 = True
                    if settings.ipass == row[1]:
                        settings.done2 = True
                        print("\nLogging in...")
                        after()
                        break              

        if settings.done1 == False or settings.done2 == False:
            print('\nIncorrect credentials, Please try again...\n')
            main()
 


                      
def after():
    if mame == True and passd == True:
        print("\nWelcome {}!\nYour login info has been emailed to you.".format(username))
        emailsender.lastemail()
        print("work")
    elif done == True:
        print("\nWelcome {}!\nYour login info has been emailed to you.".format(username))
        #emailsender.lastemail2()
        print("works")
    
def main():
    settings.init()
    valid()
    
main()

# Make login code: /
    # Make table /
    # Add to table = Make new users /
    # Read table /
    # Reset table /
    # Redo credentials if incorrect /
# Link python files: /
    # Make global variables between python files /
# Use Username or Email as iname: /
    # Make new user with username and email /
    # Welcome message has to say,"Welcome {username}" /
    # mame has to be letters or numbers, no symbols except ( _ or . ) /
    # mame has to be 4+ letters long /
    # email has to end with @gmail.com /
    # password has to be longer than 6 letters /
        # Password contains:
            # 1 capital letter
            # 2 numbers
    # password cannot be the same as username /
    # Retype: /
        # compare passwords /
        # compare email /
# Send emails from python: /
    # Send email address to user's email address /
    # Send email with credentials /
# Confirm email address - using random generated pin /
    # Make random 6 digit pin /
    # Save pin with details /
    # Send pin number to user /
    # Ask user to confirm pin number /
    # Send account info after pin confirmation /
    # If resend, replace original pin with new pin /
# If forget credentials:
    # Use email to send random code 
    # Ask to enter new password twice
    # Edit account credentials on csv
# Once login:
    # Display information
    # Allow to edit information:
        # Ask to login again
        # Ask what to edit, or if done
        # Replace table credentials with new data
# Encrypt database using cryptography module
    # Username encryption is different to password encryption
    # Decryption tool is saved but not shown
# Implement this code into HTML:
    # Make a login webpage
    # Make a "captive portal" popup
# Make a database server using rasberry pi:
    # Install Node.js
    # Create / read csv files
    # Link node.js file with webpage
# Portforward:
    # Allow the website to be hosted with a domain
