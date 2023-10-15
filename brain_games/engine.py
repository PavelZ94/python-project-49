import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    game_intro = game.INTRO
    print(f'{game_intro}')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')

    count_of_rounds = 0

    while count_of_rounds != 3:
        question, right_answer = game.current_game()
        print(f"Question: {question}")
        player_answer = prompt.string("Your answer: ")

        if player_answer != right_answer:
            print(f'''{player_answer} is wrong answer ;(.
Correct answer was {right_answer}.
Let's try again, {player_name}!''')
            return
        elif player_answer == right_answer:
            print('Correct!')
            count_of_rounds += 1
    return (print(f"Congratulations, {player_name}!"))
