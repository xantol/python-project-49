from random import randint, choice


question = 'What is the result of the expression'

def play_game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    print(f'{num1} {operator} {num2}')
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return str(correct_answer)
