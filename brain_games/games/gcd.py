from random import randint


question = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def play_game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print(f'Question: {num1} {num2}')
    return str(calculate_gcd(num1, num2))
