#очень пробная версия из того что помню о списках
from random import choice, randint


question = 'What number is missing in the progression?'


def play_game():
    l = [randint(0, 50)]
    step = randint(2, 30)
    for i in range(0, randint(5, 10)):
        l.append(l[i] + step)
    index = randint(0, len(l) - 1)
    correct_answer = l[index]
    l[index] = '..'
    print(f'Question: {l}')
    return str(correct_answer)
