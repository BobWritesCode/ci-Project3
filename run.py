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
    # Get player input
    text = utils.colored(255, 165, 0, "Press Enter to return to main menu...")
    input(f'\n{text}')
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
        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')
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
    # Get player input
    text = utils.colored(255, 165, 0, "Press Enter to continue...")
    user_choice = input(f'\n{text}')
    set_up_new_character()


def set_up_new_character():
    '''
    Function sets all new character stats to default values
    '''

    stats = {
        "day" : 0,
        "cash" : float(constants.STARTING_CASH),
        "reputation" : float(0),
        "hotdog" : int(0),
        "bun" : int(0),
        "onion" : int(0),
        "sauce" : int(0),
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
        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'{text}')

        if validate_input(user_choice, 8):
            break
    
    if user_choice == '1':
        purchase_location(stats)
    elif user_choice == '2':
        purchase_cart_menu(stats)
    elif user_choice == '3':
        puchase_staff_menu(stats)
    elif user_choice == '4':
        purchase_stock_menu(stats)
    elif user_choice == '5':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '6':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '7':
        error_message("Coming soon")
        daily_menu(stats)
    elif user_choice == '8':
        print(stats)
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
        text = utils.colored(0, 255, 255, "Purchase hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}\n')

        for x, y in enumerate(LOC_NAME, start=1):
            str_part_1 = f'{x}. {y}'

            if stats['location'][str(x)]['purchased'] == False:
                str_part_2 = utils.colored(50, 205, 50, "Avaliable")
                text = f'PURCHASE for £{LOC_COST[x-1]}'
                str_part_3 = utils.colored(0, 255, 255, text)
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}' + ' - ' f'{str_part_3:<30}')
            else:
                str_part_2 = utils.colored(255, 165, 0, "Purchased")
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<52}' + '- ')

        print_go_back()

        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')

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
                        # Get player input
                        text = utils.colored(255, 165, 0, "Press Enter to continue...")
                        input(f'{text}')
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
        text = utils.colored(0, 255, 255, "Purchase or upgrade carts at your hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}\n')

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

        print_go_back()

        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')

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
                        # Get player input
                        text = utils.colored(255, 165, 0, "Press Enter to continue...")
                        input(f'{text}')

                    else:
                        error_message("Not enough funds")

                else:
                    error_message("Purchase Land")

            else:
                break
            
    daily_menu(stats)


def purchase_stock_menu(stats):
    '''
    Purchase stock menu
    '''
    while True:
        clear_terminal()
        text = utils.colored(0, 255, 255, "Purchase consumable stock to purchase")
        print(f'{text}')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}\n')

        text = utils.colored(0, 255, 255, "Your currently have this many portions of each item:")
        print(f'{text}')
        print('------------------------------------')
        print(f'{stats["bun"]} x Hotdog bun(s)')
        print(f'{stats["hotdog"]} x Hotdog sausage(s)')
        print(f'{stats["onion"]} x Onion(s)')
        print(f'{stats["sauce"]} x Special sauce(s)')

        # Show menu options
        print(constants.PURCHASE_STOCK_OPTIONS)

        print_go_back()

        # Get player input
        text = utils.colored(255, 165, 0, "Input choice: ")
        user_choice = input(f'\n{text} ')
        print('')

        if validate_input(user_choice, 4):

            if int(user_choice) == 0:
                break

            else:
                if user_choice == '1':
                    item = 'bun'
                elif user_choice == '2':
                    item = 'hotdog'
                elif user_choice == '3':
                    item = 'onion'
                elif user_choice == '4':
                    item = 'sauce'

                item_name = constants.STOCK_COSTS[item][0]
                item_qty = constants.STOCK_COSTS[item][1]
                item_cost = constants.STOCK_COSTS[item][2]

                text = utils.colored(50, 205, 50, f"{item_name} ({item_qty} portions)")

                print(f'You selected {text} for £{item_cost}.00')

                # Get player input
                text = utils.colored(255, 165, 0, "How many would you like to purchase?")
                user_choice_qty = input(f'\n{text}')
                print('')

                cost = int(item_cost) * int(user_choice_qty)
                new_qty = int(user_choice_qty) * int(item_qty)

                print('Checkout:')
                
                str1 = utils.colored(50, 205, 50, item_name)
                str2 = utils.colored(50, 205, 50, user_choice_qty)
                str3 = utils.colored(50, 205, 50, new_qty)
                str4 = utils.colored(50, 205, 50, f'£{cost}.00')

                print(f'{"Item:":<10}{str1:<10}')
                print(f'{"Qty:":<10}{str2:<10}')
                print(f'{"Portions:":<10}{str3:<10}')
                print(f'{"TOTAL:":<10}{str4:<10}')
                print('')

                # Get player input
                text = utils.colored(255, 165, 0, "Would you like to make this purchase? (type: yes) ")
                yes_no = input(f'{text}\n')

                print('')

                if validate_yes_no(yes_no):

                    if yes_no.lower() in ['y','yes']:
                        # Check if remaining cash will above 0 after purchase, if so continue, else loop
                        remaining_cash = stats["cash"] - cost

                        if remaining_cash >= 0:
                            # Update player stock with purchased items
                            stats[item] = int(stats[item]) + int(new_qty)
                            print(utils.colored(50, 205, 50, 'Purchase Succesful'))
                            # Update player cash
                            stats["cash"] = remaining_cash
                            text = f'Remaining cash £{remaining_cash}'
                            print(utils.colored(0, 255, 255, text))
                            # Get player input
                            text = utils.colored(255, 165, 0, "Press Enter to continue...")
                            input(f'{text}\n')

                        else:
                            error_message("Not enough funds")

    daily_menu(stats)


def puchase_staff_menu(stats):
    '''
    Hire and train staff menu
    '''
    LOC_NAME = constants.LOCATION_NAMES
    STAFF_PRICE = constants.STAFF_COSTS

    while True:
        clear_terminal()
        text = utils.colored(0, 255, 255, "Hire and train staff for your hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        print(f'Current Cash: £{stats["cash"]}\n')

        for x, y in enumerate(LOC_NAME, start=1):
            staff_level = stats['location'][str(x)]['staff_lvl']
            str_part_1 = f'{x}. {y}'

            if staff_level == 0 :
                text = 'Vacant position'
                str_part_2 = utils.colored(255, 0, 0, text)

            else:
                text = f'Current level is {staff_level}'
                str_part_2 = utils.colored(0, 255, 255, text)

            if stats['location'][str(x)]['purchased'] == False:
                text = f'Purchase location first'
                str_part_3 = utils.colored(255, 0, 0, text)

            elif staff_level == 0:
                text = f'PURCHASE for £ {STAFF_PRICE[staff_level]}'
                str_part_3 = utils.colored(50, 205, 50, text)

            elif staff_level == '5':
                text = 'No traning required'
                str_part_3 = utils.colored(255, 165, 0, text)

            else:
                text = f'TRAIN for £{STAFF_PRICE[staff_level]}'
                str_part_3 = utils.colored(50, 205, 50, text)

            print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<23}' + ' - ' f'{str_part_3:<18}')

        print_go_back()

        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')

        if validate_input(user_choice, 5):

            if int(user_choice) > 0:
                # Make sure location has been purchased first

                if stats['location'][str(user_choice)]['purchased'] == True:
                    # Check if remaining cash will above 0 after purchase, if so continue, else loop
                    staff_level = stats['location'][str(user_choice)]['staff_lvl']
                    remaining_cash = stats["cash"] - STAFF_PRICE[staff_level]

                    if remaining_cash >= 0:
                        new_staff_lvl = staff_level + 1
                        stats['location'][str(user_choice)]['staff_lvl'] = new_staff_lvl
                        stats["cash"] = remaining_cash
                        loc = int(user_choice) - 1
                        text = f'Staff level {new_staff_lvl} purchased for {LOC_NAME[loc]} for £{STAFF_PRICE[staff_level]}.'
                        print(utils.colored(50, 205, 50, text))
                        text = f'Remaining cash £{remaining_cash}'
                        print(utils.colored(0, 255, 255, text))
                        # Get player input
                        text = utils.colored(255, 165, 0, "Press Enter to continue...")
                        input(f'{text}')

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
        # Get player input
        text = utils.colored(255, 165, 0, "What name would you like to use?")
        user_name = input(f'{text}\n')
        print('')

        if user_name:

            while True:
                print(f'Hello {user_name}\n')
                # Get player input
                text = utils.colored(255, 165, 0, "Would you like to change your name? (yes / no) ")
                yes_no  = input(f'{text}\n')
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
    # Get player input
    text = utils.colored(255, 165, 0, "Press Enter to continue...")
    input(f'{text}\n')
    return user_id


def show_credits():
    '''
    Display credits on screen
    '''
    clear_terminal()
    print(constants.CREDITS)
    # Get player input
    text = utils.colored(255, 165, 0, "Press Enter to return to main menu...")
    input(f'\n{text}')
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
    # Get player input
    text = utils.colored(255, 165, 0, "Press Enter to retry...")
    input(f'{text}')
    clear_terminal()


def clear_terminal():
    '''
    Clears terminal for better user experience
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def print_go_back():
    '''
    Print 0. Go Back in yellow
    '''
    text = utils.colored(255,255,0, f'\n0. Go Back')
    print(text)

def main():
    '''
    Main functions to run once code has loaded
    '''
    main_menu()

#Setting default text color
print(utils.colored(0, 0, 0, 'text'))

#set_up_new_character()
main()