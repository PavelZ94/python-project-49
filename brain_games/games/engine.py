from brain_games.cli import welcome_user, get_answer


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
            if count_of_rounds == 3:
                return (print(f"Congratulations, {player_name}!"))
