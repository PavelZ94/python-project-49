import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number > 1:
        results = []
        for i in range(2, number):
            result = number % i
            results.append(result)
            if 0 in results:
                right_answer = False
            else:
                right_answer = True
        return right_answer


def current_game():
    number = random.randint(1, 100)
    question = f'{number}'
    right_answer = 'yes' if is_prime(number) else 'no'
    return (question, right_answer)
