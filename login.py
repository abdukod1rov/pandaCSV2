import hashlib
import pandas as pd


class User:
    def __init__(self, username, password, question, answer):
        self.username = username
        self.password = password
        self.question = question
        self.answer = answer


class Login:
    def __init__(self):
        pass

    def register(self, username, password, question, answer):
        df = pd.read_csv("User-1.csv")
        user = User(username, password, question, answer)

        lastIndex = df.iloc[-1]['ID']

        new_user_df = pd.DataFrame(
            {'ID': [lastIndex + 1], 'Username': [user.username],
             "PSW": [user.password], 'Question': [user.question], 'Answer': [user.answer]}
        )
        new_user_df_added = df.append(new_user_df, ignore_index=True)
        new_user_df_added.to_csv('User-1.csv')
