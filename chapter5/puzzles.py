income = float(input())
if income >= 1000:
    print("you need topay rich tax")
else:
    print("you are not rich enough yet")
    print("but you might be in the future...")


twinkies = int(input())
if twinkies < 100 or twinkies > 500:
    print("you have too few or too many twinkies")


money = float(input())
if (money > 100 and money < 500) or (money > 1000 and money < 5000):
    print("correct amount")


ninjas = int(input())
if ninjas < 10:
    print("Bring 'em on!")
elif ninjas < 30:
    print("it will be a struggle, but I can fight them.")
elif ninjas < 50:
    print("that's too many")