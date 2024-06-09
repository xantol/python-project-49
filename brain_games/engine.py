import prompt


GAME_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def play_engine(game_module):
    user = welcome_user()
    print(game_module.question)
    for _ in range(GAME_ROUNDS):
        answer_list = game_module.play_game()
        print(answer_list[0])
        correct_answer = answer_list[1]
        answer = get_answer()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {user}!"
            )
            return
    print(f'Congratulations, {user}!')
