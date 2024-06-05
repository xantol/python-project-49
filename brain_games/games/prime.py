from random import randint


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    num = randint(2, 100)
    print(f'Question: {num}')
    if num == 2:
	return 'yes'
    for divider in range(2, num):
        if num % divider == 0:
            return 'no'
    return 'yes'
