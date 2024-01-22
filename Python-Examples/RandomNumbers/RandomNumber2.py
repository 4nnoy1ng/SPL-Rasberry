import random

RandomNumber1 = random.randint(0,100);
RandomNumber2 = random.randint(0,100);

print(RandomNumber1);
print(RandomNumber2);

if RandomNumber1 <= RandomNumber2 <= 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if RandomNumber1 == RandomNumber2 <= 30:
    print("Eine der beiden ist kleiner als 30")

if RandomNumber1 <= 50 and RandomNumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")