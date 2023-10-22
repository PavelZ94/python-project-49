import random

INTRO = 'What number is missing in the progression?'


def make_question(number1, number2, period):
    progression = list(range(number1, number2, period))
    right_answer = random.choice(progression)
    new_progression = [x if x != right_answer else ".." for x in progression]
    question = (" ".join(map(str, new_progression)))
    return (question, right_answer)


def current_game():
    number1 = random.randint(1, 5)
    number2 = random.randint(17, 20)
    period = random.randint(1, 3)
    question, right_answer = make_question(number1, number2, period)
    return (question, str(right_answer))
