# нагуглил метод join)
from random import randint


question = 'What number is missing in the progression?'


def play_game():
    progression_list = [randint(0, 50)]
    step = randint(2, 30)
    for i in range(0, randint(4, 10)):
        progression_list.append(progression_list[i] + step)
    index = randint(0, len(progression_list) - 1)
    correct_answer = progression_list[index]
    progression_list[index] = '..'
    progression_stroke = ' '.join(str(elem) for elem in progression_list)
    print(f'Question: {progression_stroke}')
    return str(correct_answer)
