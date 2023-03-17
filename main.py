from login import Login
import pandas as pd

login = Login()


def main():
    while True:
        choice = input('Choose L to log in:').upper()
        if choice == 'L':
            username = input('Enter username: ')
            password = input('Enter password: ')
            question = input('Enter security question: ')
            answer = input('Submit answer for the previous question: ')
            login.register(username, password, question, answer)
            print('Registered successfully')


if __name__ == '__main__':
    main()
