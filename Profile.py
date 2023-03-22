import pandas as pd


class ProfileUser:
    def __init__(self, name, surname, age, passport, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.passport = passport
        self.address = address


class CreateProfile:
    def __init__(self):
        pass

    def create_profile(self, name, surname, age, passport, address):
        """A form to create the user profile """
        user = ProfileUser(name, surname, age, passport, address)  # create a user
        user_info_df = pd.read_csv('User_info-1.csv')
        last_index = int(user_info_df.iloc[-1]['ID'])  # get the last index of the dataframe for autoincrement
        new_user_df = pd.DataFrame(
            {'ID': [last_index + 1],
             'Name': [user.name], 'Surname': [user.surname], 'age': [user.age], 'passport': [user.passport],
             'address': [user.address]})  # create a new dataframe by getting user credentials
        user_created_df = user_info_df.append(new_user_df,
                                              ignore_index=True)  # add the new user profile dataframe to the existing

        user_created_df.to_csv('User_info-1.csv', index=False)
        print('Profile created successfully!')


class Profile:
    def display_profile(self, ID):
        df = pd.read_csv('User_info-1.csv')
        record = df.loc[df['ID'] == ID]
        print(record)

    def change_password(self, username, answer, new_password, new_password_confirm):
        df = pd.read_csv('User-1.csv')
        passwordConfirmed = False
        for index, row in df.iterrows():
            if row['Username'] == username and row['Answer'] == answer:
                if new_password == new_password_confirm:
                    passwordConfirmed = True

        if passwordConfirmed:
            df.loc[(df['Username'] == username) & (df['Answer'] == answer), 'PSW'] = new_password
            df.to_csv('User-1.csv', index=False)
            print('Password changed successfully!')
        else:
            print('Process failed!')

    def reset_password(self, username, answer, new_password, new_password_confirmed):
        self.change_password(username, answer, new_password, new_password_confirmed)
