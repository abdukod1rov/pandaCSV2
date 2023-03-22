import hashlib
import pandas as pd


class User:
    def __init__(self, username, password, answer):
        self.username = username
        self.password = password
        self.answer = answer


class Login:

    def login(self, username, password, answer):

        user = User(username, password, answer)
        users_df = pd.read_csv('User-1.csv')
        loginStatus = False
        validUsername = False
        validPassword = False
        validAnswer = False
        user_id = ''
        for index, row in users_df.iterrows():
            if row['Username'] == user.username and row['PSW'] \
                    == user.password and row['Answer'] == user.answer:
                validUsername = True
                validPassword = True
                validAnswer = True
                loginStatus = True
                user_id = row['ID']

            if row['Username'] != user.username or row['PSW'] != user.password and row['Answer'] == user.answer:
                validUsername = False
                validPassword = False
                validAnswer = True

            if row['Answer'] != user.answer and row['Username'] \
                    != user.username and row['PSW'] != user.password:
                validAnswer = False
                validUsername = True
                validPassword = True

        if not validUsername and not validPassword:
            print('Invalid Username or Password')
        if not validAnswer:
            print('Could not pass from security question. Invalid Answer')
        if loginStatus:
            print('Logged In Successfully!')
        return int(user_id)
