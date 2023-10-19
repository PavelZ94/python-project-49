import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def calculate(number):
    if number > 1:
        results = []
        for i in range(2, number):
            result = number % i
            results.append(result)
            if 0 in results:
                right_answer = 'no'
            else:
                right_answer = 'yes'
        return right_answer

def current_game():
    number = random.randint(1, 100)
    question = f'{number}'
    right_answer = calculate(number)
    return (question, right_answer)
