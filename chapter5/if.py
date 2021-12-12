age = 25
if age > 20:
    print("you are too old!")
    print("Why are we here?")
    print("why do we live?")

# condicions
age = 10
if age >= 10:
    print("What`s brown and sticky? A stick!")

# else
print("Want to hear a dirty joke?")
age = 8
if age == 12:
    print("A pig fell in the mud!")
else:
    print("Shhh..it's a secret.")

# elif
age = 15
if age == 10:
    print("haha")
elif age == 11:
    print("hahaha")
elif age == 12:
    print("hehe")
elif age == 13:
    print("hehehe")
else:
    print("huh")

# moznosti
age = 19
if age == 10 or age == 11 or age == 12 or age ==13:
    print("What is 12 + 134 + 421 + 54? A headache!")
else:
    print("Huh?")


if age >= 10 and age <= 13:
    print("What is 12 + 134 + 421 + 54? A headache!")
else:
    print("Huuh?")


# none
myval = None
if myval == None:
    print("myval has no value.")


age = int(input())
# if age >= 18:
    # print("access granted")
# else:
    # print("this is 18+ only")
print("access granted") if age >= 18 else print("this is 18+ only")
print("you are over 18" if age >= 18 else "you must be an adult")