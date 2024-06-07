from random import randint


question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play_game():
    number = randint(1, 500)
    print(f'Question: {number}')
    if is_even(number):
        return 'yes'
    return 'no'
