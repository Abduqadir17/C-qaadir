import random
number = random.randint(15,30)
for i in range(0,4):
    user = int(input("Guess the Number: "))
    if user == number:
        print("congrartulations!")
        print(f"{number} is the correct guess")
        break
if user!= number:
        print(f"your guess is incorrect , {number} is the correct guess")
