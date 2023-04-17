#!/usr/bin/python
# coding=utf-8

import os
import csv
import smtplib
from subprocess import call

user = 'darsenlu@gmail.com'
app_password = 'aqvi zjzw kqae cdwg'

# Log into Gmail
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user, app_password)

# Open account list
csvfile = open('2023_scmodeling_account_v2.csv', 'r') 
# csvfile = open('accounts_test.csv', 'r')
    
myreader = csv.reader(csvfile)

# Loop over accounts

for row in myreader:
    name = row[0]
    username = row[1]
    recipient = row[2]
    passwd = row[3]
    
    # Create new user
    print("Creating user '%s'..."%username)
    os.system("sudo useradd -m -s /bin/csh %s"%username)
    os.system("sudo cp cshrc_file /home/%s/.cshrc"%username)
    os.system("sudo chown %s.%s /home/%s/.cshrc"%(username,username,username))

    # Set password
    print("Setting password for %s ..."%username)
    os.system("echo '%s:%s' | sudo chpasswd" % (username,passwd))
    msg = """\
From: %s
To: %s<%s>
Subject: %s

Dear %s:

The following information is for your Semiconductor Memory Devices and Circuits (半導體記憶體元件與設計實務) course account.

Your username is: %s
Your password is: %s

Please connect to devmodel.ee.ncku.edu.tw using MobaXterm or other SSH connection software.

You will need this to complete your homework assignments.

Best Regards,
Darsen Lu
 

"""%("Darsen Lu<darsenlu@gmail.com>", name, recipient, "Password Notification for N258300", name, username, passwd)
    
    '''sent the mail'''
    try:
        smtpObj.sendmail("darsenlu@gmail.com", recipient, msg)
        print ("Mail sent to %s" % recipient)
    except Exception as e:
        print("Error sending mail. Error msg: %s" % str(e))
    

csvfile.close()

smtpObj.quit()

