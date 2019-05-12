#!/usr/bin/python

#We can also build lists, first start with an empty one.

elements = []

#then we use the range function to do 0 to 5 counts

for i in range (0,6):

    print "Adding %d to the list" %i
    elements.append(i)

    #append is a function that list can understand

#Now we can can print them out

for i in elements:
    print"Element added was: %d" %i


    
