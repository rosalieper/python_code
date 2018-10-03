#!usr/bin/python

#Examples of usage of lists

mylist = ['abs', '123', 123, 344, 20.5]
tinylist = [12, 'John']

print mylist

print mylist[0]

print mylist[1:]

print mylist[2:3]

print mylist+tinylist

print tinylist *2

#Examples of usage of tuples

tuple = ('absd', 700, 2.8, 'marry', 2.2)

tinytupple = (231, 'jon')

print tuple

print tuple[0]

print tuple[1:3]

print tuple[:2]

print tinytupple * 2

print tuple + tinytupple


#Examples of usage of Dicitionary

dict = {}

dict['one'] = 'this is one'

dict[2] = 'this is two'

tinydict = {'name':'john', 'code': '2345', 'dept':'sales'}

print dict['one']

print dict[2]

print tinydict

print tinydict.keys()

print tinydict.values()