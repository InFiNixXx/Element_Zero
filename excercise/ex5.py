#!/usr/bin/python
name = 'Sauronil Das'
age = 22 
height = 167 #in centimeters
weight = 65 #in Kilograms
eyes = 'Back'
teeth = 'White'
hair = 'Black'


print "Let's Talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d Kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)

print (age * weight)

