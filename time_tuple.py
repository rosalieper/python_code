#!/usr/bin/python

import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")

print ("returned tuple: %s " % struct_time)