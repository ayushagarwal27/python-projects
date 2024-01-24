from random import randint

lower_num, higher_num = 1, 10
random_number:int = randint(lower_num,higher_num)
print(f"Guess the number in the range from {lower_num} to {higher_num}.")

num_of_guess_allowed = 3
while True:
    try:
        if num_of_guess_allowed <= 0:
            print('You ran out of permitted guesses!')
            break
        user_guess : int = int(input(f"Guess: "))
        if user_guess == random_number:
            print("You Won!")
            break
        if user_guess > random_number:
            print('The number is lower')
        elif user_guess < random_number:
            print('The number is higher')
        num_of_guess_allowed -= 1
    except ValueError as e:
        print('Please enter a valid number')