import random

INTRO = 'What is the result of the expression?'

def calculate(number1, number2, get_operator):
    if '+' == get_operator:
        right_answer = str(number1 + number2)
    if '-' == get_operator:
        right_answer = str(number1 - number2)
    if "*" == get_operator:
        right_answer = str(number1 * number2)
    return right_answer


def current_game():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = ['+', '-', '*']
    get_operator = random.choice(operator)
    question = f'{number1} {get_operator} {number2}'
    right_answer = calculate(number1, number2, get_operator)
    return (question, right_answer)
