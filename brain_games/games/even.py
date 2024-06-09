from random import randint


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play_game():
    number = randint(1, 500)
    question = f'Question: {number}'
    if is_even(number):
        return [question, 'yes']
    return [question, 'no']
