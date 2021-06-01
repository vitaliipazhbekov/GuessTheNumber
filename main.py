import random

random.randrange(0, 100)
number = random.randrange(0, 100)
Running = True

while Running:
    guess = int(input('Insert your number.'))

    if guess == number:
        print('Gotcha!')
        Running = False

    elif number > guess:
        print('Guessed number is more than you have written.')
    else:
        print('Guessed number is less than you have written.')


print('Game Over. Want to play one more time?')