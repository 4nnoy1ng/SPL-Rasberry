# 1 FUnktion mit 2 Zahlen

def add(a, b):
    return a + b

sum = add(3,4)
print(sum)

# 2 Funktion mit Random Nummer
import random

# Funktion darf nicht Random heisen

def generate_random_number():
    return random.randint(100, 200)

Random_Number = generate_random_number()
print("Zufällige Zahl: ", Random_Number)

# 3 Funktion Random Name
def Names():
    MyList = ["Daniel", "Siegfried", "Herbert", "Tuertscher"]
    return random.choice(MyList)

Name = Names()
print(Name)



