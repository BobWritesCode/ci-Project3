# Write your code to expect a terminal of 80 characters wide and 24 rows high
GAMETITLE = 'Hotdog Empire Tycoon' #Name change pending
print(f'Preparing to start {GAMETITLE}...\n')

import gspread
from google.oauth2.service_account import Credentials
import os
import string
import random
import constants
import utils
from math import floor

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
    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def main_menu():
    '''
    Display main menu and options
    '''
    clear_terminal()
    while True:
        print(utils.main_menu_header(255, 0, 0,'Welcome to Hotdog Tycoon'))
        print(constants.MAIN_MENU_OPTIONS)
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')
        if validate_input(user_choice, 4):
            break
    if user_choice == '1':
        new_game()
    elif user_choice == '2':
        retrieve_save()
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
    data = [user_id, user_name]
    stats = set_up_character(data , True)
    save_data(stats, True)
    background_story(stats)


def background_story(stats):
    '''
    Tell the user the background story
    '''
    clear_terminal()
    print(constants.BACKGROUND_STORY)
    print_press_enter_to("Press Enter to continue...")
    daily_menu(stats)


def set_up_character(data, new_player):
    '''
    Function sets all new character stats to default values
    '''
    if new_player:
        user_id = data[0]
        name = data[1]
        data = [
            user_id,                        #0
            name,                           #1
            0,                              #2
            float(constants.STARTING_CASH), #3
            float(0),                       #4
            int(0),                         #5
            int(0),                         #6
            int(0),                         #7
            int(0),                         #8
            int(1),                         #9
            int(1),                         #10
            int(2),                         #11
            int(1),                         #12
            float(3.50),                    #13
            False,                        #14
            int(0),                         #15
            int(0),                         #16
            False,                        #17
            int(0),                         #18
            int(0),                         #19
            False,                        #20
            int(0),                         #21
            int(0),                         #22
            False,                        #23
            int(0),                         #24
            int(0),                         #25
            False,                        #26
            int(0),                         #27
            int(0),                         #28
            False                         #29
        ]
    else:
        to_check = [14,17,20,23,26,29]
        for i in to_check:
            data[i] = False if data[i] == "FALSE" else True

    stats = {
        "user_id" : data[0],                #0
        "name" : data[1],                   #1
        "day" : int(data[2]),                    #2
        "cash" : float(data[3]),            #3
        "reputation" : float(data[4]),      #4
        "sausage" : int(data[5]),           #5
        "bun" : int(data[6]),               #6
        "onion" : int(data[7]),             #7
        "sauce" : int(data[8]),             #8
        "recipe" : {
            "bun" : int(data[9]),           #9
            "sausage" : int(data[10]),      #10
            "onion" : int(data[11]),        #11
            "sauce" : int(data[12])         #12
        },
        "selling_price" : float(data[13]),  #13
        "location" : {
            "1" : {
                "purchased" : data[14],     #14
                "cart_lvl" : int(data[15]), #15
                "staff_lvl" : int(data[16]) #16
            },
            "2" : {
                "purchased" : data[17],      #17
                "cart_lvl" : int(data[18]),  #18
                "staff_lvl" : int(data[19])  #19
            },
            "3" : {
                "purchased" : data[20],      #20
                "cart_lvl" : int(data[21]),  #21
                "staff_lvl" : int(data[22])  #23
            },
            "4" : {
                "purchased" : data[23],      #23
                "cart_lvl" : int(data[24]),  #24
                "staff_lvl" : int(data[25])  #25
            },
            "5" : {
                "purchased" : data[26],      #26
                "cart_lvl" : int(data[27]),  #27
                "staff_lvl" : int(data[28])  #28
            }
        },
        "game_over" : data[29]               #29
    }
    return stats


def daily_menu(stats):
    '''
    Daily player menu to purchase upgrades and make changes to recipes
    '''
    clear_terminal()
    while True:
        text = utils.colored(0, 255, 255, "Daily preparation")
        print(f'{text}')
        print('------------------------------------')
        print(f'Day: {stats["day"]} out of 10')
        print(f'Current Cash: £{stats["cash"]}\n')
        print(constants.DAILY_MENU_OPTIONS)
        # Get player input
        text = utils.colored(255, 165, 0, "Input choice:")
        user_choice = input(f'\n{text}')
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
        change_recipe_menu(stats)
    elif user_choice == '6':
        set_selling_price(stats)
    elif user_choice == '7':
        run_day(stats, False)
    elif user_choice == '0':
        save_data(stats, False)
        main()


def run_day(stats, AMPM):
    '''
    Runs the game code for each day.
    '''
    portions = get_portions_avaliable(stats)
    expected_cost = constants.LOCATION_EXP_COST[0]
    while not AMPM:
        footfall = constants.LOCATION_FOOTFALL
        rep_modifier = (stats["reputation"] + 2) / 2
        customers_served = footfall[0] * rep_modifier
        print(customers_served)

        print_press_enter_to("Part of day over")
        AMPM = True
    stats["day"]+=1
    daily_menu(stats)


def get_portions_avaliable(stats):
    '''
    Return how many portions of hotdogs are avaliable based on stock and recipe
    '''
    sausage = stats["sausage"]
    bun = stats["bun"]
    onion = stats["onion"]
    sauce = stats["sauce"]

    r_sauasge = stats["recipe"]["sausage"]
    r_bun = stats["recipe"]["bun"]
    r_onion = stats["recipe"]["onion"]
    r_sauce = stats["recipe"]["sauce"]

    portions = sausage / r_sauasge
    if (bun / r_bun) < portions : portions = (bun / r_bun)
    if (onion / r_onion) < portions : portions = (onion / r_onion)
    if (sauce / r_sauce) < portions : portions = (sauce / r_sauce)

    print(floor(portions))

    print_press_enter_to("Continue")
    return floor(portions)


def save_data(stats, first_save):
    '''
    Save player data to database.
    The for loop looks through the coloumn 1 data from Google sheets.
    If it finds a match it updates that row.
    Else creates a new row with data.
    If "exit = True" go to main menu after save.
    '''
    if not first_save:
        text = utils.colored(0, 255, 255, "SAVING.... Please do not close.")
        print(f'\n{text}')
    data_to_save = []
    data_to_save = convert_dict_to_array(stats, data_to_save)
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)
    i = 0
    found = False
    if not first_save:
        for cell_value in col_array:
            i+=1
            if cell_value == stats['user_id']:
                j = 0
                found = True
                for y in data_to_save:
                    j+=1
                    worksheet.update_cell(i, j, y)
                text = "Data saved."
                print(utils.colored(50, 205, 50, text))
    if not found or first_save:
        worksheet.append_row(data_to_save)
    print_press_enter_to("Press Enter to continue...")


def retrieve_save():
    '''
    Retrieve saved game data and resume game from where last left off.
    '''
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)
    max_i = len(col_array)
    found = False
    while not found:
        clear_terminal()
        text = utils.colored(0, 255, 255, "Retrieve a previous game")
        print(f'{text}')
        print('------------------------------------')
        print('\nYou will need your game ID to retrieve a previous game.')
        print_go_back()
        text = utils.colored(255, 165, 0, "Enter Game ID:")
        user_input = input(f'\n{text}')
        i = 0
        # Cycle through rows in Google sheet until GAME ID finds a Match
        text = utils.colored(0, 255, 255, "SEARCHING...")
        print(f'\n{text}')
        for cell_value in col_array:
            i+=1
            if cell_value == user_input:
                found = True
                text = utils.colored(0, 255, 255, "GAME FOUND...")
                print(f'\n{text}')
                # Copy data from row where GAME ID matches
                data = worksheet.row_values(i)
                stats = set_up_character(data, False)
                text = utils.colored(50, 205, 50, "GAME LOADED.")
                print(f'\n{text}')
                print_press_enter_to("Press Enter to continue...")
                daily_menu(stats)
                break
        # If no GAME ID match then show error.
        if not found:
            print_error_message("No game found")


def convert_dict_to_array(data, data_to_save):
    '''
    Convert dict game data to an array so it can be saved to Google Sheet
    '''
    for i in data:
        if type(data[f'{i}']) is dict:
            convert_dict_to_array(data[f'{i}'], data_to_save)
        else:
            data_to_save.append(data[f"{i}"])
    return data_to_save


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
                        print_press_enter_to("Press Enter to continue...")
                    else:
                        print_error_message("Not enough funds")
                else:
                    print_error_message('Already Purchase')
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
                        print_press_enter_to("Press Enter to continue...")
                    else:
                        print_error_message("Not enough funds")
                else:
                    print_error_message("Purchase Land")
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
        print_portions_in_stock(stats)
        print(constants.PURCHASE_STOCK_OPTIONS)
        print_go_back()
        text = utils.colored(255, 165, 0, "Input choice: ")
        user_choice = input(f'\n{text}')
        if validate_input(user_choice, 4):
            if int(user_choice) == 0:
                break
            else:
                if user_choice == '1':
                    item = 'bun'
                elif user_choice == '2':
                    item = 'sausage'
                elif user_choice == '3':
                    item = 'onion'
                elif user_choice == '4':
                    item = 'sauce'
                item_name = constants.STOCK_COSTS[item][0]
                item_qty = constants.STOCK_COSTS[item][1]
                item_cost = constants.STOCK_COSTS[item][2]
                text = utils.colored(50, 205, 50, f"{item_name} ({item_qty} portions)")
                print(f'You selected {text} for £{item_cost}.00')
                text = utils.colored(255, 165, 0, "How many would you like to purchase?")
                user_choice_qty = input(f'\n{text}')
                if validate_input(user_choice_qty, 999999):
                    cost = int(item_cost) * int(user_choice_qty)
                    new_qty = int(user_choice_qty) * int(item_qty)
                    print('\nCheckout:')
                    str1 = utils.colored(50, 205, 50, item_name)
                    str2 = utils.colored(50, 205, 50, user_choice_qty)
                    str3 = utils.colored(50, 205, 50, new_qty)
                    str4 = utils.colored(50, 205, 50, f'£{cost}.00')
                    print(f'{"Item:":<10}{str1:<10}')
                    print(f'{"Qty:":<10}{str2:<10}')
                    print(f'{"Portions:":<10}{str3:<10}')
                    print(f'{"TOTAL:":<10}{str4:<10}')
                    text = utils.colored(255, 165, 0, "Would you like to make this purchase? (type: yes) ")
                    yes_no = input(f'\n{text}\n')
                    if validate_yes_no(yes_no):
                        if yes_no.lower() in ['y','yes']:
                            # Check if remaining cash will above 0 after purchase, if so continue, else loop
                            remaining_cash = stats["cash"] - cost
                            if remaining_cash >= 0:
                                # Update player stock with purchased items
                                stats[item] = int(stats[item]) + int(new_qty)
                                print(utils.colored(50, 205, 50, 'Purchase Successful'))
                                # Update player cash
                                stats["cash"] = remaining_cash
                                text = f'Remaining cash £{remaining_cash}'
                                print(utils.colored(0, 255, 255, text))
                                print_press_enter_to("Press Enter to continue...")
                            else:
                                print_error_message("Not enough funds")
                        else:
                                print(utils.colored(255, 0, 0, 'Purchase Aborted'))
                                print_press_enter_to("Press Enter to continue...")
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
                        print_press_enter_to("Press Enter to continue...")
                    else:
                        print_error_message("Not enough funds")
                else:
                    print_error_message("Purchase Land")
            else:
                break
    daily_menu(stats)


def change_recipe_menu(stats):
    '''
    Player is able to change recipe menu
    '''
    while True:
        clear_terminal()
        bun = stats['recipe']['bun']
        sausage = stats['recipe']['sausage']
        onion = stats['recipe']['onion']
        sauce = stats['recipe']['sauce']
        text = utils.colored(0, 255, 255, "Make changes to your recipe")
        print(f'{text}')
        print('------------------------------------\n')
        print_portions_in_stock(stats)
        print(utils.colored(0, 255, 255, "\nCurrent Recipe:"))
        print('------------------------------------')
        text1 = utils.colored(0, 255, 255, "Ingrediant")
        text2 = utils.colored(0, 255, 255, "Portions per serving")
        print(f'{text1:<12}{"|":<2}{text2:<0}')
        print('------------------------------------')
        print(f'{"1. Buns":<12}{"|":<2}{f"{bun}":<0}')
        print(f'{"2. Sausages":<12}{"|":<2}{f"{sausage}":<0}')
        print(f'{"3. Onions":<12}{"|":<2}{f"{onion}":<0}')
        print(f'{"4. Sauce":<12}{"|":<2}{f"{sauce}":<0}')
        print_go_back()
        print('\nTo update your recipe type the ingrediant and amount i.e. "3 4" will update onion to 4 potions per serving.\n')
        # Get player input
        text = utils.colored(255, 165, 0, "Enter change i.e. 3 4 (max 999):")
        user_choice = input(f'{text}')
        user_choice = user_choice.split()
        if validate_recipe_change(user_choice):
            if int(user_choice[0]) == 0:
                break
            stock_choosen = constants.STOCK_OPTIONS[int(user_choice[0])-1]
            stats['recipe'][stock_choosen] = int(user_choice[1])
            text = utils.colored(50, 205, 50, f'Updated {stock_choosen.capitalize()} to {user_choice[1]} per serving.')
            print(text)
            print_press_enter_to("Press Enter to continue...")
    daily_menu(stats)


def set_selling_price(stats):
    '''
    Allow user to set selling price of hotdogs
    '''
    while True:
        clear_terminal()
        curr_price = stats["selling_price"]
        text = utils.colored(0, 255, 255, "Set the selling price of your product")
        print(f'{text}')
        print('------------------------------------')
        production_cost = cost_to_make(stats)
        text = utils.colored(50, 205, 50, "£"+ str(round(production_cost, 2)))
        print(f'\nThe current cost for to make your your product is {text}')
        text = utils.colored(50, 205, 50, "£"+"{:.2f}".format(stats["selling_price"]))
        print(f'\nCurrent selling price is {text}')
        net_profit = round(curr_price - production_cost, 2)
        if net_profit >= 0:
            text = utils.colored(50, 205, 50, "Profit per serving is:")
            print(f'\n{text}£{net_profit}')
        else:
            text = utils.colored(255, 0, 0, "Loss per serving is: ")
            print(f'\n{text}£{net_profit}')
        print_go_back()
        text = utils.colored(255, 165, 0, "Enter new price: £")
        new_price = input(f'\n{text}')
        if validate_price_change(new_price):
            if float(new_price) == 0:
                break
            new_price = round(float(new_price) , 2)
            stats["selling_price"] = float(new_price)
            text = utils.colored(50, 205, 50, f'\nUpdated selling price to £{new_price}')
            print(text)
            print_press_enter_to("Press Enter to continue...")
    daily_menu(stats)


def cost_to_make(stats):
    '''
    Works out the cost of making each hotdog
    '''
    bun = stats['recipe']['bun'] * constants.STOCK_COSTS['bun'][2] / constants.STOCK_COSTS['bun'][1]
    sausage = stats['recipe']['sausage'] * constants.STOCK_COSTS['sausage'][2] / constants.STOCK_COSTS['sausage'][1]
    onion = stats['recipe']['onion'] * constants.STOCK_COSTS['onion'][2] / constants.STOCK_COSTS['onion'][1]
    sauce = stats['recipe']['sauce'] * constants.STOCK_COSTS['sauce'][2] / constants.STOCK_COSTS['sauce'][1]
    return (bun + sausage + onion + sauce)


def validate_price_change(data):
    '''
    Check user input valid value for price change
    '''
    try:
        try:
            float_value = float(data)
        except:
            print_error_message("invalid input")
            return False
        if float_value >= 0:
          return True
        else:
            raise ValueError()
    except ValueError as e:        
        print_error_message("invalid input")
        return False
    return True


def validate_recipe_change(data):
    '''
    Check user input for recipe change is valid
    '''
    if len(data) == 1 and int(data[0]) == 0:
        return True
    if len(data) != 2:
        text = utils.colored(255, 0, 0, 'Too little or too many values.')
        print(f'{text}')
        print_press_enter_to("Press Enter to continue...")
    else:
        if validate_input(data[0], 999) and validate_input(data[1], 999): 
            return True
    return False


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
    return user_id


def show_credits():
    '''
    Display credits on screen
    '''
    clear_terminal()
    print(constants.CREDITS)
    print_press_enter_to("Press Enter to return to main menu...")
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
            print_error_message("invalid input")
            return False
        if int_value >= 0 and int_value <= int(max_value):
          return True
        else:
            raise ValueError()
    except ValueError as e:        
        print_error_message("invalid input")
        return False
    return True


def validate_yes_no(value):
    '''
    Checks to make sure user typed expected response.
    Acceptable ['y','ye','yes','n','no'], return True
    Else return False.
    '''
    if value.lower() in ['y','ye','yes','n','no']:
        return True
    else:
        print_error_message("invalid input")
        return False


def print_error_message(data):
    '''
    Function to provide appropriate error message
    '''
    if data:
        text = utils.colored(255, 0, 0, data)
    else:
        text = utils.colored(255, 0, 0, 'Error.')
    print(f'{text}')
    print_press_enter_to("Press Enter to retry...")
    clear_terminal()


def clear_terminal():
    '''
    Clears terminal for better user experience
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def print_portions_in_stock(stats):
    '''
    Print how many portions from ingridants player currently has
    '''
    text = utils.colored(0, 255, 255, "Your current stock:")
    print(f'{text}')
    print('------------------------------------')
    print(f'{stats["bun"]} x Hotdog bun(s)')
    print(f'{stats["sausage"]} x Hotdog sausage(s)')
    print(f'{stats["onion"]} x Onion(s)')
    print(f'{stats["sauce"]} x Special sauce(s)')


def print_press_enter_to(text):
    '''
    Print "Press Enter....
    '''
    text = utils.colored(255, 165, 0, f'\n{text}')
    input(f'{text}')


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
main()