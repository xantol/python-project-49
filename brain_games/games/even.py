from random import randint


question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play_game():
    number = randint(1, 500)
    game_question = f'Question: {number}'
    if is_even(number):
        return [game_question, 'yes']
    return [game_question, 'no']
