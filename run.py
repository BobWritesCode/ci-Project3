# Write your code to expect a terminal of 80 characters wide and 24 rows high
GAMETITLE = 'Hotdog Tycoon' #Name change pending
print(f'Preparing to start {GAMETITLE}...\n')

import gspread
from google.oauth2.service_account import Credentials
import os
import string
import random
import constants
import utils

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize (SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hotdog_Tycoon_Data')


def show_leaderboard_data():
    '''
    Gets leaderbaord data from Google sheet and displays in terminal
    '''
    clear_terminal()
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    print('************************************')
    print('Top 10 highscores for classic mode')
    print('************************************\n')
    print(f"{data[0][0]:<30}{data[0][1]:<40}")
    print('------------------------------------')
    for x in data[1:10]:
        print(f"{x[0]:<30}{x[1]:<40}")
    input("\nPress Enter to return to main menu...")
    main_menu()


def main_menu():
    '''
    Display main menu and options
    '''
    clear_terminal()
    print(utils.main_menu_header(255, 0, 0,'Welcome to Hotdog Tycoon'))
    user_choice = 0

    while True:
        print(constants.MAIN_MENU_OPTIONS)
        user_choice = input("\nInput choice: ")
        if validate_input(user_choice):
            break

    print(user_choice)
    if user_choice == '1':
        new_game()
    elif user_choice == '2':
        error_message("Coming soon")
        input("Press Enter to return to main menu...")
        main_menu()
    elif user_choice == '3':
        show_leaderboard_data()
    elif user_choice == '4':
        show_credits()


def new_game():
    '''
    Create new user and set up for a new game
    '''
    clear_terminal()
    print(f'Welcome to your new game. The first thing we need to do is set you up with a')
    print(f'new account.\n')
    user_name = create_user_name()
    user_id = create_user_id(user_name)
    background_story()


def background_story():
    '''
    Tell the user the background story
    '''
    clear_terminal()
    print(constants.BACKGROUND_STORY)
    input('\nPress Enter to continue...')
    set_up_new_character()


def set_up_new_character():
    stats = {
        "cash" : float(constants.STARTING_CASH),
        "reputation" : float(0),
        "hotdogs" : int(0),
        "buns" : int(0),
        "onions" : int(0),
        "secret_sauce" : int(0),
        "location" : {
            "1" : {
                "cart_lvl" : int(0),
                "staff_lvl" : int(0),
            },
            "2" : {
                "cart_lvl" : int(0),
                "staff_lvl" : int(0),
            },
            "3" : {
                "cart_lvl" : int(0),
                "staff_lvl" : int(0),
            },
            "4" : {
                "cart_lvl" : int(0),
                "staff_lvl" : int(0),
            },
            "5" : {
                "cart_lvl" : int(0),
                "staff_lvl" : int(0),
            },
        },
    }
    print(stats)

def create_user_name():
    '''
    Allow user to create their own name for the game
    '''
    while True:
        user_name = input(f'What name would you like to use?\n')
        print('')
        if user_name:
            while True:
                print(f'Hello {user_name}\n')
                yes_no = input('Would you like to change your name? (yes / no) \n')
                print('')
                if validate_yes_no(yes_no):
                    if yes_no.lower() in ['n','no']:
                        return user_name
                    else:
                        break


def create_user_id(user_name):
    '''
    Creates user ID and checks to make sure not already in user
    before showing user.
    '''
    user_id = ''
    print(f'Please wait why your new user ID is created...')
    while True:
        user_id = "".join(string.ascii_uppercase[random.randrange(0,25)] for x in range(6))
        user_data = SHEET.worksheet('user_data')
        cell_list = user_data.findall(user_id)
        if len(cell_list) == 0:
            break
    clear_terminal()
    print(f'Welcome to your new game. The first thing we need to do is set you up with a new')
    print(f'new account.\n')
    print('------------------------------------')
    print('USER ID CREATED')
    print('------------------------------------')
    print(f'\n{user_name}, your new user ID is: {utils.colored(0, 207, 0, user_id)}\n')
    print(f'Please keep this safe as this is how you can retrieve your progress')
    input('\nPress Enter to continue...')
    return user_id


def show_credits():
    '''
    Display credits on screen
    '''
    clear_terminal()
    print(constants.CREDITS)
    input("\nPress Enter to return to main menu...")
    main_menu()


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
            clear_terminal()
            error_message("invalid input")
            return False
        if int_value >= 1 and int_value <= 4:
          return True
        else:
            raise ValueError()
    except ValueError as e:
        clear_terminal()
        error_message("invalid input")
        return False

    return True


def validate_yes_no(value):
    '''
    Checks to make sure user typed expected response
    '''
    return value.lower() in ['y','ye','yes','n','no']


def error_message(data):
    '''
    Function to provide appropriate error message
    '''
    if data == "invalid input":
        print(f'\nInvalid input: please try again.\n')
    elif data == "Coming soon":
        print(f'\nThis feature is not implemented yet and will be coming soon.\n')
    else:
        print('Error')


def clear_terminal():
    '''
    Clears terminal for better user experience
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    '''
    Main functions to run once code has loaded
    '''
    #Setting default text color
    print(utils.colored(0, 0, 0, 'text'))
    main_menu()

set_up_new_character()
#main()