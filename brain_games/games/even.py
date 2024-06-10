from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def play_game():
    num = randint(1, 500)
    question = f'Question: {num}'
    return (question, 'yes') if is_even(num) else (question, 'no')
