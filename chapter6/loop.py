from random import randrange


#for x = 0; x < 5; x += 1
for x in range(0, 16):
    print("hello %d" % (x + 1));

print(list(range(20, 0, -3)));

koncatiny:list = ["hlava","ramena","kolena","palce","kolena","palce","kolena","palce","hlava","ramena","kolena","palce","oci","usi","usta","nos"]
for koncatina in koncatiny:
    print("the song goes:{}".format(koncatina))

table = [[None for x in range(4)] for y in range(4)];
for row in range(0,4):
    for col in range(0,4):
        # table[row][col] = row * 4 + col;
        table[row][col] = randrange(0,256);

print("-------------")
for row in range(0,4):
    print('|', end='')
    for col in range(0,4):
        print("%2x" % table[row][col], end='')
        if col < 3:
            print(',', end='')
    print('|', end='\n')
print("-------------")

a = 50
b = 100
while a < b:
    print(a)
    a+=1