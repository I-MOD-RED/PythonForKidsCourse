for x in range(0, 20):
    print("hello %s" % x)
    if x <= 9:
        continue
    print("x is bigger than")

from operator import mod


age = int(input())
for i in range(1, age + 1):
    # i % 2 -> remainder (zvysok) after division by two
    # mod(i, 2) does exactly the same thing
    if (mod(age, 2) == 0) and (i % 2 == 0):
        print(i)
    # & is a boolean concatenation (statements on both sides have to be true for it to be true)
    # 'and' does exactly the same
    # Boolean logic for AND operation:
    # statement A | statement B | result
    #    false    |    false    | false
    #    false    |    true     | false
    #    true     |    false    | false
    #    true     |    true     | true
    if (age % 2 == 1) & (mod(i, 2) == 1):
        print(i)

# Boolean logic for OR operation:
# statement A | statement B | result
#    false    |    false    | false
#    false    |    true     | true
#    true     |    false    | true
#    true     |    true     | true

# Boolean logic for XOR (eXclusive OR) operation:
# statement A | statement B | result
#    false    |    false    | false
#    false    |    true     | true
#    true     |    false    | true
#    true     |    true     | false


ingredients = ["snails", "leeches", "gorilla butt", "giraffe legs", "centipedes gut", "kokot", "pica", "kurva vyjebany python skurveny dopice pridem si o nervy"]

for i, j in zip(range(1,len(ingredients)+1), ingredients):
    print("%d %s" % (i,j))


weight = 50
moonweight: float
for year in range(1, 16):
    moonweight = weight * 0.165
    print("year %s = %f" % (year,moonweight))
    weight += 1
