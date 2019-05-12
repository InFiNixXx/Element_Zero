#!/usr/bin/python

from sys import exit

import random
response = ["yes" , "no" ]
random.choice(response)

def begin_friendship():
    print "You Now Have A Friend"
    exit(0)

def recreation():
    print "Ask For Rectreational Activity"
    if random.choice(response) == "yes":
        begin_friendship()
    else:
        print "Sorry, The Person is Not Interested"
        exit(0)




def beverage_offers():
    print "Ask Them: "
    print "1. Coffee"
    print "2. Tea "
    print "3. Cocoa "

    next = raw_input("> ")
    if next == "1." or next == "Coffee":
        random.choice(response) == "yes"
        begin_friendship()

    elif next == "2" or next == "Tea":
        random.choice(response) == "yes"
        begin_friendship()



    elif next == "3" or next == "Cocoa":
        random.choice(response) == "yes"
        begin_friendship()

    else:
        print "Sorry, The Person Clearly Does not want to be friends with you"
        exit(0)





def beverage():
    print "Sorry! The Person does not want to have a meal?"
    print "Lets ask  Him/Her for beverage!"
    if random.choice(response) == "yes":
        beverage_offers()
        
    else:
        recreation()


def meal():
    print "Would Lke To Have A Meal Together?"
    if random.choice(response) == "yes":
        print "You Had a Lovely Meal at the Cheese Cake Factory"
        begin_friendship()
    else:
        beverage()

def home_prompt():
    print "You made your call"
    print "Lets See If the person Is at Home or Not?"
    home()

def home():
    if random.choice(response) == "yes":
        meal()
    else:
        print "Would You Like to call someone else?"
        print "1. Yes \t 2. No"

        next = raw_input("> ")

        if next == "1" or next == "Yes":
             place_call()
        else:
             exit()


def place_call():
    print "Whom Do You Want To Call?"
    print "1. Chris Pratt"
    print "2. Karlie Kloss"
    print "3. Dave Mustaine"

    next = raw_input("> ")

    if next == "1" or next == "Chris Pratt":
        home_prompt()

    if next == "2" or next == "Karlie Kloss":
        home_prompt()

    if next == "3" or next =="Dave Mustaine":
        home_prompt()

place_call()
    


