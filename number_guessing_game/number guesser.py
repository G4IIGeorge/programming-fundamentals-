import random

def number_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("I am thinking of a number between 1 and 20.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
