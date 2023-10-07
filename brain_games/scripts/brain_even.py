import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count_of_rounds = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_of_rounds != 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        player_answer = input('Your answer: ')
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if player_answer == right_answer:
            print('Correct!')
            count_of_rounds += 1
        else:
            print(f'''{player_answer} is wrong answer ;(. Correct answer was {right_answer}.
Let's try again, {name}!''')
            count_of_rounds = 0
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()