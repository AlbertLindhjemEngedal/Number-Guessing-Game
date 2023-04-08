import random

def hent_input(text):
    value = input(text)
    while not value.isnumeric():
        print("You have to write a positive number. ")
        value = input(text)
    return int(value)


print("Welcome to The Number Guessing Game! ")
print("ㅤ")
print("You have to choose a range of numbers to guess from.")
min_number = hent_input("What should the minimum number be? ")
max_number = hent_input("What should the maximum number be? ")

while max_number <= min_number:
    print("The maximum number has to be grater than the minimum number")
    min_number = hent_input("What should the minimum number be? ")
    max_number = hent_input("What should the maximum number be? ")


random_number = random.randint(min_number, max_number)
number_guessed = hent_input("Guess the number! ")


guesses = 0


while True:
    guesses += 1

    if number_guessed > max_number:
        print(f"Your guess has to be lower than {max_number}")
        number_guessed = hent_input(f"Your guess has to be under {max_number}")
        continue

    if number_guessed < min_number:
        print(f"Your guess has to be greater than {min_number}")
        number_guessed = hent_input("Make another guess: ")
        continue

    if number_guessed > random_number:
        print("You are over the number.")
        number_guessed = hent_input("Guess again: ")
        continue

    if number_guessed < random_number:
        print("You are under the number.")
        number_guessed = hent_input("Guess again: ")
        continue
    break


print("ㅤ")
print(f"You got it! The number was: {random_number}")
print(f"You guessed {guesses} times before you got it.")
print("ㅤ")

quit_status = input("Press a key to quit: ")