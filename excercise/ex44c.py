#!/usr/bin/python

class Parent(object):
    def alt(self):
        print "PARENT altered()"

class Child(Parent):
    def alt(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).alt()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.alt()
son.alt()
