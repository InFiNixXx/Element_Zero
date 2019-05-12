#!/usr/bin/python

print "You Enter a Dark Room with TWO DOORS. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There is a Giant Bear eating a cheese cake. What do you do?"
    print "1. Take the Cake and Have it Yourself?"
    print "2. Scream at the Bear becuase you do that best!"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off."
    elif bear == "2":
        print "The bear eats your legs off."
    else:
        print "Well, doing %s is probably better. Bears runs away." % bear 

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina"
    print "1. Blueberries"
    print "2. Yellow Jacket Clothespins"
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. GOOD JOB"
    else:
        print "The insanity rots your eyes into a pool of muck. GOOD JOB"

else:

    print "You stumble upon and fall on knife edge and die. GOOD JOB"



