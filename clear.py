#!/usr/bin/env python


with open('scr.txt','r+') as f:
	f.readline()
	f.seek(0)
	f.truncate()
