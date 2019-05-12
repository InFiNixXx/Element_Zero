#!/usr/bin/python

from sys import exit

def mass_murder(string):
    print string, "Congratulations You Killed Millions of poeple"
    exit(0)

def che_guevera():
    mass_murder("Wrong Option")

def joseph_stalin():
    mass_murder("Wrong Option")

def hitler():
    mass_murder("Wrong Option")

    


def start():
    print "War Games"
    print "You get to be a Leader of 3 great Nations and Political Agendas"
    print "Choose Your General"
    print "1. Che Guevera \t\t\t 2. Joseph Stalin \t\t\t 3. Adolf Hitler"

    next = raw_input("> ")

    if next == "1" or next == "Che Guevera":
        che_guevera()
    elif next == "2" or next == "Joseph Stalin":
        joseph_stalin()
    elif next == "3" or next == "Adolf Hitler":
        hitler()
    else:
        print "Error, You Can't escape the WAR GAMES"
        start()


start()

