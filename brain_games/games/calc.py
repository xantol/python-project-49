from random import randint, choice


main_question = 'What is the result of the expression'


def calculate(num1, num2, operator):
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return correct_answer


def play_game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    question = f'Question: {num1} {operator} {num2}'
    return [question, str(calculate(num1, num2, operator))]
