#!/usr/bin/env python
import datetime


with open('scr.txt','r+') as f:
	f.readline()
	f.seek(0)
	f.truncate()



with open("scr.txt", mode='a') as file:
    file.write('%s \n' % (datetime.datetime.now()))
#with open("scr.txt", mode='a') as file:
#    file.write('%s \n' % (datetime.datetime.now()))
