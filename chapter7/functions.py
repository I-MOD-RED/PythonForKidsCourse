

def testfunc(fname, lname):
    print("Hello %s %s" % (fname, lname))

testfunc("Iva","Modrovic")

firstname = 'Ivana'
lastname = 'Modrovicova'
testfunc(firstname, lastname)

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending

print(savings(500, 50, 250))

another_variable = 36
def variable_test2():
    first_variable = 25
    second_variable = 34
    return first_variable * second_variable - another_variable

print(variable_test2())

def spaceship_building(cans):
    total_cans = 0
    for day in range(1, 8):
        total_cans = total_cans + cans
        print("day %s = %s cans" % (day, total_cans))

print(spaceship_building(8))

import time
print(time.asctime())

import sys

def silly_age_joke():
    print("How old are you?")
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 15:
        print("what is 456 + 789 - 123? A headache!")
    else:
        print("huh?")

silly_age_joke()
