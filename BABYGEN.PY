import random
vowels = ["a", "e", "i", "o", "u"]
c =[0,0,0]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]

for i in range(3):
    a = cons[random.randint(0,19)]
    b = vowels[random.randint(0,4)]
    c[i] = a+b

print(c[0]+c[1]+c[2])

