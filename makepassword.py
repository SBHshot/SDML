#!/usr/bin/python

import csv
import random
import string

#prefix="scmodeling"
prefix="scmemory"
i = 0
csvfile=open('scmemory_students_2022.csv', 'r') 
myreader = csv.reader(csvfile)
for row in myreader:
    i=i+1
    name = row[0]
    email = row[1]
    #sid = row[2]
    passwd = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    print( "%s,%s%d,%s,%s" % (name, prefix, i, email, passwd))
    
