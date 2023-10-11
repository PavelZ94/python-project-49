import random

INTRO = 'What is the result of the expression?'


def current_game():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = ['+', '-', '*']
    op = random.choice(operator)
    question = f'{number1} {op} {number2}'
    if '+' == op:
        right_answer = str(number1 + number2)
    if '-' == op:
        right_answer = str(number1 - number2)
    if "*" == op:
        right_answer = str(number1 * number2)
    return (question, right_answer)
