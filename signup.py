import pandas as pd


class User:
    def __init__(self, username, password, confirm_password, question, answer):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.question = question
        self.answer = answer


class Register:
    def __init__(self):
        pass

    def register(self, username, password, confirm_password, question, answer):
        df = pd.read_csv("User-1.csv")
        user = User(username, password, confirm_password, question, answer)
        lastIndex = int(df.iloc[-1]['ID'])

        new_user_df = pd.DataFrame(
            {'ID': [lastIndex + 1], 'Username': [user.username],
             "PSW": [user.password], 'Question': [user.question], 'Answer': [user.answer]}
        )

        for index, row in df.iterrows():
            if row['Username'] == user.username:
                print("Username exists!")

        if confirm_password == password:
            new_user_df_added = df.append(new_user_df, ignore_index=True)
            new_user_df_added.to_csv('User-1.csv', index=False)
            print('Registered Successfully\nNow, we it\'s time to create your profile ')

        else:
            print('Registration failed. Passwords do not match!')
