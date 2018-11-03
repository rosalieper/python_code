#!/usr/bin/python
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)

t = time.mktime(t)

print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))