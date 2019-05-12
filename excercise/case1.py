#!/usr/bin/python

class Rectangle(object):
    def __init__(self, length, breadth, unit_cost = 0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_perimeter(self):
        return 2 *(self.length + self.breadth)
    def get_area(self):
        return self.length * self.breadth
    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

print "Insert Length"
length1 = raw_input("> ")
print "Insert Breadth"
breadth1 = raw_input("> ")
print "Insert Unit Cost"
unit_cost1 = raw_input("> ")


r = Rectangle(int(length1), int(breadth1), int(unit_cost1))

print "Area of Rectangle : %s cm^2" % (r.get_area())
print "Cost of Rectangle field : Rs %r " % (r.calculate_cost())
