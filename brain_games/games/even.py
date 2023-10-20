import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer


def current_game():
    question = random.randint(1, 100)
    right_answer = is_even(question)
    return (question, right_answer)
