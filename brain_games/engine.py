from brain_games.games import calc
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

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        return False

def play_engine(game_module):
    user = welcome_user()
    print(game_module.question)
    for _ in range(GAME_ROUNDS):
        correct_answer = game_module.play_game()
        answer = get_answer()
        if check_answer(answer, correct_answer):
            continue
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {user}!"
                )
            return
    print(f'Congratulations, {user}!')