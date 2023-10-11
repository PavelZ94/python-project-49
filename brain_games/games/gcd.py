import math
import random

INTRO = 'Find the greatest common divisor of given numbers.'


def current_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    right_answer = str(math.gcd(number1, number2))
    return (question, right_answer)
