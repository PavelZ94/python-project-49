import prompt


def welcome_user(game_intro=''):
    print('Welcome to the Brain Games!')
    if game_intro:
        print(f'{game_intro}')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer


def engine(game):
    player_name = welcome_user(game.INTRO)
    count_of_rounds = 0

    while count_of_rounds != 3:

        question, right_answer = game.current_game()

        player_answer = get_answer(question)

        if player_answer != right_answer:
            print(f'''{player_answer} is wrong answer ;(.
Correct answer was {right_answer}.
Let's try again, {player_name}!''')
            return
        elif player_answer == right_answer:
            print('Correct!')
            count_of_rounds += 1
    return (print(f"Congratulations, {player_name}!"))
