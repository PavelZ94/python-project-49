import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 == 0:
        right_answer = True
    else:
        right_answer = False
    return right_answer


def current_game():
    question = random.randint(1, 100)
    right_answer = 'yes' if is_even(question) else 'no'
    return (question, right_answer)
