import pandas as pd
from signup import Register
from login import Login
from art import home_page
from Profile import CreateProfile, Profile

signup = Register()
login = Login()
create = CreateProfile()
profile = Profile()


def main():
    global question
    while True:
        choice = input('Choose 1 to register  2 to login 3 to reset your password: ')
        if choice == '0':
            break
        if choice == '1':
            username = input('Enter username: ').lower()
            password = input('Enter password: ')
            confirm_password = input('Confirm password: ')
            question = input('Enter security question: ')
            answer = input('Submit answer for the previous question: ').lower()
            signup.register(username, password, confirm_password, question, answer)
            # create the user profile
            name = input('Name: ')
            surname = input('Surname: ')
            age = input('Age: ')
            passport = input('Passport series number: Make sure to enter in the XX00000: ')
            address = input('Address: ')
            create.create_profile(name, surname, age, passport, address)

        if choice == '2':
            df = pd.read_csv('User-1.csv')
            question = ''
            questionValid = False
            username = input('Enter username: ').lower()
            password = input('Enter password: ')
            for index, row in df.iterrows():
                if row['Username'] == username and row['PSW'] == password:
                    questionValid = True
                    question = row['Question']
            if questionValid:
                answer = input(f'Answer the following security question\n{question}: ').lower()
                ID = login.login(username, password, answer)
                print(home_page)
                # Prompt the user to do something
                toDo = input('What would you like to do?: ')
                if toDo == '1':
                    profile.display_profile(ID)
                if toDo == '2':
                    userName = input('Enter username: ')
                    print(f'Please, answer the following security question!')
                    answer = input(f'{question}: ')
                    userExists = False
                    for index, row in df.iterrows():
                        if row['Username'] == username and row['Answer'] == answer:
                            userExists = True
                            break

                    if userExists:
                        new_password = input('Enter new password: ')
                        new_password_confirm = input('Confirm new password: ')
                        profile.change_password(userName, answer, new_password, new_password_confirm)
                    else:
                        print('Username or answer incorrect!')
            else:
                print('Security question not found')

        if choice == '3':
            username = input('Enter username: ')
            print('Answer the following security question')
            answer = input(f'{question}')
            new_password = input('Enter a new password: ')
            new_password_confirm = input('Confirm the password: ')
            profile.reset_password(username, answer, new_password, new_password_confirm)


if __name__ == '__main__':
    main()
