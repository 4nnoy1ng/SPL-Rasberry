import random

RandomNumber = 0
sum = 0

while (RandomNumber != 15 and RandomNumber != 25):
    RandomNumber = random.randint(10, 30)
    sum += RandomNumber
    print(RandomNumber)

    print(sum)
