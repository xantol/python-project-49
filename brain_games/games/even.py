from random import randint


question = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():  
        number = randint(1, 500)
        print(f'Question: {number}')
        if number % 2 == 0:
            return 'yes'
        else:
            return 'no'
