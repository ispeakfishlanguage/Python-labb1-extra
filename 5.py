import random

digits = list(range(10))
number = random.sample(digits, 3)

def check_guess(guess, number):
    guess_list = [int(digit) for digit in guess]

    if guess_list == number:
        return "CORRECT", True

    for i in range(3):
            if guess_list[i] == number[i]:
                return "Match: You've guessed a correct number in the correct position", False
            elif guess[i] in number:
                return "Close: You've guessed a correct number but in the wrong position", False
    return "Nope: You haven't guess any of the numbers correctly", False

while True:
    guess = input("Enter a 3 digit number to guess: ")
    message, correct = check_guess(guess, number) 
    print(message)
    if correct:
        break 