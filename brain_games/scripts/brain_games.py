#!/usr/bin/env python3
import brain_games.cli as cli


def greet(message):
    print(message)


def main():
    greet('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
