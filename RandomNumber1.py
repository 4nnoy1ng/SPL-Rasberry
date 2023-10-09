import random;

RandomNumber = random.randint(0,100)
print(RandomNumber);

if RandomNumber <= 20:
    print("Mini");

if 20 <= RandomNumber <= 50:
    print("Medium");

if RandomNumber >= 50:
    print("Large");