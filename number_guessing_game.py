# number_guessing_game.py

import random
def main():
    print(" 🎯 Number Guessing Game ")
    print("I am thinking of a number between 1 and 150.")

    secret_number = random.randint(1,150) #we will remove this line later.
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1 
        if guess == secret_number:
            print(f"Congratulations!! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print(" Too low! Try a higher number. ")
        else:
            print("Too high! Try a lower number.")

if __name__ == "__main__":
    main()


