#!/usr/bin/python
# coding=utf-8

import re
import random
import string

prefix="scmodeling"

with open('scmodeling_students_2020.txt', 'r', encoding = 'utf-8') as moodleFile:
    text = moodleFile.read()
    #old way (before 2021)
    list = re.findall(r"(\S+)\s\(1082_N258300\)\n\S+\n\n電子郵件信箱\n\s+(\S+)", text, re.MULTILINE)
    
#list = re.findall(r"(\S+)\s(1072_N258300)\n(\S+)\n電子郵件信箱(\S+)", text, re.MULTILINE)
    
    print("%d members found",  len(list))
    i = 0
    for member in list:
        i = i + 1
        #print (member)
        # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
        passwd = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

        print( "%s,%s%d,%s,%s" % (member[0], prefix, i, member[1], passwd))

    moodleFile.close()

