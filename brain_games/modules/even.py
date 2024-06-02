import prompt
from random import randint
from brain_games.modules.greet import welcome_user


def is_even():
    user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 500)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
            '{correct_answer}'.\nLet's try again, {user}!")
            break
