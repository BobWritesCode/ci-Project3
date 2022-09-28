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

    while True:
        print(utils.main_menu_header(255, 0, 0,'Welcome to Hotdog Tycoon'))
        user_choice = 0
        print(constants.MAIN_MENU_OPTIONS)
        user_choice = input("\nInput choice: ")
        if validate_input(user_choice, 4):
            break

    if user_choice == '1':
        new_game()
    elif user_choice == '2':
        error_message("Coming soon")
        main_menu()
    elif user_choice == '3':
        show_leaderboard_data()
    elif user_choice == '4':
        show_credits()
    elif user_choice == '0':
        main_menu()


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
    '''
    Function sets all new character stats to default values
    '''
    stats = {
        "day" : 0,
        "cash" : float(constants.STARTING_CASH),
        "reputation" : float(0),
        "hotdogs" : int(0),
        "buns" : int(0),
        "onions" : int(0),
        "secret_sauce" : int(0),
        "location" : {
            "1" : {
                "purchased" : False,
                "cart_lvl" : int(0),
                "staff_lvl" : int(0)
            },
            "2" : {
                "purchased" : False,
                "cart_lvl" : int(0),
                "staff_lvl" : int(0)
            },
            "3" : {
                "purchased" : False,
                "cart_lvl" : int(0),
                "staff_lvl" : int(0)
            },
            "4" : {
                "purchased" : False,
                "cart_lvl" : int(0),
                "staff_lvl" : int(0)
            },
            "5" : {
                "purchased" : False,
                "cart_lvl" : int(0),
                "staff_lvl" : int(0)
            }
        }
    }
    daily_menu(stats)


def daily_menu(stats):
    '''
    Daily player menu to purchase upgrades and make changes to recipes
    '''
    clear_terminal()
    while True:
        print(constants.DAILY_MENU_OPTIONS)
        user_choice = input("\nInput choice: ")

        if validate_input(user_choice, 6):
            break
    
    if user_choice == '1':
        purchase_location(stats)
    elif user_choice == '2':
        purchase_cart_menu(stats)
    elif user_choice == '3':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '4':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '5':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '6':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '0':
        daily_menu(stats)


def purchase_location(stats):
    '''
    Purchase location menu for player
    '''
    LOC_NAME = constants.LOCATION_NAMES
    LOC_COST = constants.LOCATION_COSTS
    while True:
        clear_terminal()
        print('Purchase hotdog pitch locations')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}')
        print('------------------------------------')
        for x, y in enumerate(LOC_NAME, start=1):
            str_part_1 = f'{x}. {y}'

            if stats['location'][str(x)]['purchased'] == False:
                str_part_2 = utils.colored(50, 205, 50, "Avaliable")
                text = f'PURCHASE for £{LOC_COST[x-1]}'
                str_part_3 = utils.colored(0, 255, 255, text)
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}' + ' - ' f'{str_part_3:<30}')
            else:
                str_part_2 = utils.colored(255, 165, 0, "Already Purchased")
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<52}' + '- ')

        print('')
        print('0. Go back.')
        print('')

        user_choice = input("\nInput choice: ")
        if validate_input(user_choice, 5):
            if int(user_choice) > 0:
                if stats['location'][str(user_choice)]['purchased'] == False:
                    # Check if remaining cash will above 0 after purchase, if so continue, else loop
                    remaining_cash = stats["cash"] - LOC_COST[int(user_choice)-1]

                    if remaining_cash >= 0:
                        stats['location'][str(user_choice)]['purchased'] = True
                        text = f'Your purchased {LOC_NAME[int(user_choice)-1]} for £{LOC_COST[int(user_choice)-1]}'
                        print(utils.colored(50, 205, 50, text))
                        stats["cash"] = remaining_cash
                        text = f'Remaining cash £{remaining_cash}'
                        print(utils.colored(0, 255, 255, text))
                        input("Press Enter to continue...")
                    else:
                        error_message("Not enough funds")
                else:
                    error_message('Already Purchase')
            else:
                break

    daily_menu(stats)


def purchase_cart_menu(stats):
    '''
    Purchase cart menu for player
    '''
    LOC_NAME = constants.LOCATION_NAMES
    CART_PRICE = constants.CART_COSTS
    
    while True:
        clear_terminal()
        print('Purchase or upgrade carts at your hotdog pitch locations')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}')
        print('------------------------------------')
        for x, y in enumerate(LOC_NAME, start=1):
            cart_level = stats['location'][str(x)]['cart_lvl']

            str_part_1 = f'{x}. {y}'

            if cart_level == 0 :
                text = 'Not currently owned'
                str_part_2 = utils.colored(255, 0, 0, text)
            else:
                text = f'Current level is {cart_level}'
                str_part_2 = utils.colored(0, 255, 255, text)

            if stats['location'][str(x)]['purchased'] == False:
                text = f'Purchase location first'
                str_part_3 = utils.colored(255, 0, 0, text)
            elif cart_level == 0:
                text = f'PURCHASE for £ {CART_PRICE[cart_level]}'
                str_part_3 = utils.colored(50, 205, 50, text)
            elif cart_level == '5':
                text = 'No further upgrades'
                str_part_3 = utils.colored(255, 165, 0, text)
            else:
                text = f'UPGRADE for £{CART_PRICE[cart_level]}'
                str_part_3 = utils.colored(50, 205, 50, text)

            print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<23}' + ' - ' f'{str_part_3:<18}')

        print('')
        print('0. Go back.')
        print('')
        user_choice = input("\nInput choice: ")

        if validate_input(user_choice, 5):
            if int(user_choice) > 0:
                # Make sure location has been purchased first
                if stats['location'][str(user_choice)]['purchased'] == True:
                    # Check if remaining cash will above 0 after purchase, if so continue, else loop
                    cart_level = stats['location'][str(user_choice)]['cart_lvl']
                    remaining_cash = stats["cash"] - CART_PRICE[cart_level]

                    if remaining_cash >= 0:
                        new_cart_lvl = cart_level + 1
                        stats['location'][str(user_choice)]['cart_lvl'] = new_cart_lvl
                        stats["cash"] = remaining_cash
                        loc = int(user_choice) - 1
                        text = f'Cart level {new_cart_lvl} purchased for {LOC_NAME[loc]} for £{CART_PRICE[cart_level]}.'
                        print(utils.colored(50, 205, 50, text))
                        text = f'Remaining cash £{remaining_cash}'
                        print(utils.colored(0, 255, 255, text))
                        input("Press Enter to continue...")
                    else:
                        error_message("Not enough funds")
                else:
                    error_message("Purchase Land")
            else:
                break
            
    daily_menu(stats)


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


def validate_input(value, max_value):
    '''
    Inside the try, converts input string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if outside the expected range.
    '''
    try:
        try:
            int_value = int(value)
        except:
            error_message("invalid input")
            return False
        if int_value >= 0 and int_value <= int(max_value):
          return True
        else:
            raise ValueError()
    except ValueError as e:        
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
        text = utils.colored(255, 0, 0, 'Invalid input: please try again.')
        print(f'{text}')
    elif data == "Coming soon":
        text = utils.colored(255, 165, 0, 'This feature is not implemented yet and will be coming soon.')
        print(f'{text}')
    elif data == "Not enough funds":
        text = utils.colored(255, 165, 0, 'You do not have enough funds to do this.')
        print(f'{text}')
    elif data == "Purchase Land":
        text = utils.colored(255, 165, 0, 'You need to purchase this location first.')
        print(f'{text}')
    elif data == "Already purchase":
        text = utils.colored(255, 165, 0, 'You already have this, make another selection.')
        print(f'{text}')
    else:
        text = utils.colored(255, 0, 0, 'Error.')
        print(f'{text}')
    input("Press Enter to retry...")
    clear_terminal()


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