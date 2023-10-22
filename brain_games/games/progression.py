import random

INTRO = 'What number is missing in the progression?'


def make_question(chosen_number, progression):
    new_progression = [x if x != chosen_number else ".." for x in progression]
    question = (" ".join(map(str, new_progression)))
    return question


def current_game():
    number1 = random.randint(1, 5)
    number2 = random.randint(17, 20)
    period = random.randint(1, 3)
    progression = list(range(number1, number2, period))
    chosen_number = random.choice(progression)
    question = make_question(chosen_number, progression)
    right_answer = str(chosen_number)
    return (question, right_answer)
