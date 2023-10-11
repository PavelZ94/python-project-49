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
