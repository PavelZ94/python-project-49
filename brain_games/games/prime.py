import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def current_game():
    number = random.randint(1, 100)
    question = f'{number}'
    right_answer = 'yes' if is_prime(number) else 'no'
    return (question, right_answer)
