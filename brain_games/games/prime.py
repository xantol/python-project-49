from random import randint


main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 2:
        return True
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True


def play_game():
    num = randint(2, 100)
    question = f'Question: {num}'
    if is_prime(num):
        return [question, 'yes']
    return [question, 'no']
