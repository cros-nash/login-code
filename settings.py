import random
from random import randint
import csv
import re

def init():
    global done1
    done1 = False
    global done2
    done2 = False
    global imame
    imame = input("Username or Email: ")
    global ipass
    ipass = input("Password: ")

def random():
    range_start = 10**(6-1)
    range_end = (10**6)-1
    global pin
    pin = randint(range_start, range_end)

def newusername():
    global new
    new = input("Username: ")
    if len(new) < 4:
        print("Username has to be longer than 4 characters")
        newusername()
    elif bool(re.match("^[A-Za-z0-9_.-]*$", new)) == False:
        print("Username can only have letters or numbers and '_' or '.'")
        newusername()
    elif re.match("^[A-Za-z0-9_.-]*$", new):
        newpassword()
        
def newpassword():
    global pas
    r1 = re.compile("[A-Z{1,}0-9{2,}]?")
    pas = input("Password: ")
    if pas == new:
        print("Password cannot be the same as username")
        newpassword()
    elif len(pas) < 6:
        print("Password has to be longer than six characters")
        newpassword()
    elif r1.search(pas):
        confirmpassword()
    elif bool(r1.search(pas)) == False:
        print("Password has to contain 1 Capital letter and 2 Numbers")
        newpassword()

def confirmpassword():
    confirmpas = input("Verify password: ")
    if confirmpas == pas:
        newemail()
    elif confirmpas != pas:
        print("Passwords do not match.")
        confirmpassword()
    else:
        print("Something went wrong")
            
def newemail():
    global ema
    ema = input("Email: ")
    r1 = re.compile("@gmail\.com")
    if r1.search(ema):
        confirmemail()
    elif bool(r1.search(ema)) == False:
        print("Please retype email address")
        newemail()

def confirmemail():
    confirmema = input("Verify email: ")
    if confirmema == ema:
        random()
    elif confirmema != ema:
        print("Emails do not match.")
        confirmemail()
    else:
        print("Something went wrong")

def search():
    with open('accountlist.csv','r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if imame == row[0] or imame == row[2]:
                global userna
                userna = row[0]
                global userpa
                userpa = row[1]
                global userem
                userem = row[2]
            if new == row[0] or ema == row[2]:
                global us
                us = row[0]
                global pa
                pa = row[1]
                global em
                em = row[2]
