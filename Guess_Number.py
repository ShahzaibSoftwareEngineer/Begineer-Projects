import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

# Call the function with a range (for example, 10)
guess(10)
