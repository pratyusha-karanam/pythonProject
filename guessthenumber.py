import random

number = random.randint(0, 10)
player = input("Enter your name:")
number_of_guesses = 0
print("Hi " + player + " I'm robo and find the number I guessed between 1 to 10")

while number_of_guesses < 6:
    guess = int(input("Enter the number that you've guessed:"))
    number_of_guesses += 1
    if number < guess:
        print("Oops! your number is too high")
    if number > guess:
        print("Oops! your number is too low")
    if number == guess:
        break
if number == guess:
    print("yes, you're right. You've guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("Sorry!" + player + "you failed to guess the right answer :(")



