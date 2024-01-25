from random import randint


def roll_dice(dice_count):
    sum = 0
    while dice_count > 0:
        number = randint(1, 6)
        sum += number
        print(f'Dice number {number}', end=", ")
        print(f'Total Sum: {sum}', end="")
        print("")
        dice_count -= 1

while True:
    try:
        entered_input: str = input('How many dice would you like to roll ? ')
        if entered_input.lower() == 'exit':
            print('Thanks for playing!')
            break
        elif int(entered_input) <= 0:
            raise ValueError
        else:
            dice_count = int(entered_input)
            roll_dice(dice_count)
            break
    except ValueError as v:
        print('Please enter a valid number')
