import prompt
from brain_games.games.greet import welcome_user
from random import randint, choice


def brain_calc():
    user = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        first_num = randint(1, 20)
        second_num = randint(1, 50)
        function = choice(['*', '+', '-'])
        print(f'Question: {first_num} {function} {second_num}')
        answer = prompt.string('Your answer: ')
        if function == '+':
            correct_answer = first_num + second_num
        elif function == '-':
            correct_answer = first_num - second_num
        else:
            correct_answer = first_num * second_num
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {user}!"
            )
            return
    print(f'Congratulations, {user}!')
