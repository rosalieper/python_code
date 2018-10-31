#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print "dict['Name']: ", dict['Name'];

#this will yield an error
dict = {['Name']: 'Zara', 'Age': 7};
print "dict['Name']: ", dict['Name'];