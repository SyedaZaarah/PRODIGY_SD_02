import random
correct = False
random = random.randint(0,10)
counter = 1
while not correct:
    guess = input("Guess the Number 0-10: ")
    guess = int(guess)
    if guess == random:
        print(f"You have guessed the right number! You took {counter} guess")
        correct = True
    elif guess > random:
        print("Too high! Try again")
        counter = counter + 1
    elif guess < random:
        print("Too low! Try again")
        counter = counter + 1

