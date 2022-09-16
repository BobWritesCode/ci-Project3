# Write your code to expect a terminal of 80 characters wide and 24 rows high
GAMETITLE = 'Hotdog Tycoon' #Name change pending
print(f'Preparing to start {GAMETITLE}...\n')

import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize (SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hotdog_Tycoon_Data')


def get_leaderboard_data():
    '''
    Gets leaderbaord data from Google sheet and displays in terminal
    '''
    clear_terminal()
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    print('\n************************************')
    print('Top 10 Highscores for classic mode')
    print('************************************\n')
    print(f"{data[0][0]:<30}{data[0][1]:<40}")
    print('------------------------------------')
    for x in data[1:10]:
        print(f"{x[0]:<30}{x[1]:<40}")


def main_menu():
    '''
    Display main menu and options
    '''
    clear_terminal()
    print('************************************')
    print(f'Welcome to {GAMETITLE}!')
    print('************************************\n')
    print(f'Can you prove that you are able to take a small hotdog stand and turn it into')
    print(f'a great hotdog empire?!')
    print(f'')
    print(f'Choose from the following options:')
    print('------------------------------------')
    print(f'1. New Game')
    print(f'2. Retrieve a previous game')
    print(f'3. View leaderboard')
    print(f'4. Credits')
    print('------------------------------------')


    while True:
        user_choice = input("\nInput choice: ")
        if validate_input(user_choice):
            print('Choice is valid!')
            break


def validate_input(value):
    '''
    Inside the try, converts input string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if outside the expected range.
    '''
    try:
        try:
            int_value = int(value)
        except:
            print(f'Invalid input: please try again.\n')
            return False
        if int_value >= 1 and int_value <= 4:
          return True
        else:
            raise ValueError()
    except ValueError as e:
        print(f'Invalid input: please try again.\n')
        return False

    return True


def clear_terminal():
    '''
    Clears terminal for better user experience
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    '''
    Main functions to run once code has loaded
    '''
    main_menu()

main()