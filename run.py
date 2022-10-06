import gspread
from google.oauth2.service_account import Credentials
import os
import string
import random
import constants
import utils
from math import floor
from math import ceil
from random import randrange
from utils import pink
from utils import gold
from utils import green
from utils import cyan
from utils import orange
from utils import red

# Write your code to expect a terminal of 80 characters wide and 24 rows high
GAMETITLE = 'Hotdog Empire Tycoon'  # Name change pending
print(f'Preparing to start {GAMETITLE}...\n')

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
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
        print(pink('Welcome to Hotdog Tycoon'))
        print(constants.MAIN_MENU_OPTIONS)
        text = orange("Input choice:")
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
    print('Welcome to your new game. The first thing we need to do is set you\
 up with a')
    print('new account.\n')
    user_name = create_user_name()
    user_id = create_user_id(user_name)
    data = [user_id, user_name]
    stats = set_up_character(data, True)
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
            user_id,  # 0
            name,  # 1
            1.0,  # 2
            float(constants.STARTING_CASH),  # 3
            float(0),  # 4
            int(0),  # 5
            int(0),  # 6
            int(0),  # 7
            int(0),  # 8
            int(1),  # 9
            int(1),  # 10
            int(2),  # 11
            int(1),  # 12
            float(3.50),  # 13
            False,  # 14
            int(0),  # 15
            int(0),  # 16
            False,  # 17
            int(0),  # 18
            int(0),  # 19
            False,  # 20
            int(0),  # 21
            int(0),  # 22
            False,  # 23
            int(0),  # 24
            int(0),  # 25
            False,  # 26
            int(0),  # 27
            int(0),  # 28
            False,  # 29
            0  # 30
        ]
    else:
        to_check = [14, 17, 20, 23, 26, 29]
        for i in to_check:
            if data[i] == "FALSE":
                data[i] = False
            else:
                data[i] = True

    stats = {
        "user_id": data[0],  # 0
        "name": data[1],  # 1
        "day": float(data[2]),  # 2
        "cash": float(data[3]),  # 3
        "reputation": float(data[4]),  # 4
        "sausage": int(data[5]),  # 5
        "bun": int(data[6]),  # 6
        "onion": int(data[7]),  # 7
        "sauce": int(data[8]),  # 8
        "recipe": {
            "bun": int(data[9]),  # 9
            "sausage": int(data[10]),  # 10
            "onion": int(data[11]),  # 11
            "sauce": int(data[12])  # 12
        },
        "selling_price": float(data[13]),  # 13
        "location": {
            "1": {
                "purchased": data[14],  # 14
                "cart_lvl": int(data[15]),  # 15
                "staff_lvl": int(data[16])  # 16
            },
            "2": {
                "purchased": data[17],  # 17
                "cart_lvl": int(data[18]),  # 18
                "staff_lvl": int(data[19])  # 19
            },
            "3": {
                "purchased": data[20],  # 20
                "cart_lvl": int(data[21]),  # 21
                "staff_lvl": int(data[22])  # 23
            },
            "4": {
                "purchased": data[23],  # 23
                "cart_lvl": int(data[24]),  # 24
                "staff_lvl": int(data[25])  # 25
            },
            "5": {
                "purchased": data[26],  # 26
                "cart_lvl": int(data[27]),  # 27
                "staff_lvl": int(data[28])  # 28
            }
        },
        "game_over": data[29],  # 29
        "game_save_row": data[30]  # 30
    }
    return stats


def daily_menu(stats):
    '''
    Daily player menu to purchase upgrades and make changes to recipes
    '''
    clear_terminal()

    if (stats["day"] % 1) == 0:
        text_time_of_day = pink("Morning")
    else:
        text_time_of_day = pink("Afternoon")

    while True:
        text = cyan("Daily preparation")
        print(text)
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}')
        text = pink(int(floor(stats["day"])))
        print(f'Day: {text}out of 10')
        print(f'Time of Day: {text_time_of_day}')
        text = gold(stats['reputation'])
        print(f'Company reputation: {text} / 5')
        print(constants.DAILY_MENU_OPTIONS)
        # Get player input
        text = orange("Input choice:")
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
        run_day(stats)
    elif user_choice == '0':
        save_data(stats, False)
        main()


def print_current_balance(stats):
    '''
    Print cash statment
    '''
    return f'£{"{:.2f}".format(floor(stats["cash"]*100)/100)}'


def run_day(stats):
    '''
    Runs the game code for each day.
    Day runs from 8 am until 5pm. 540 minutes in total.
    Each minute is a chance for something to happen.
    '''
    clear_terminal()

    if (stats["day"] % 1) == 0:
        hour = 8  # Game time, hours
    else:
        hour = 12  # Game time, hours

    price = stats["selling_price"]  # Selling Price
    minute = 00  # Game time, minute
    cust_count = []  # Temp customer count for AM and PM
    open_loc_name = []  # Open Location Name
    open_loc_num = []  # Open Location Number stats['location']['?']
    loc_sale_value = []  # Location Sales Value
    sold = 0  # Units sold for part of the day, resets mid-day.
    feedback = {  # Feedback table for declined sales
        "value buy": [],  # Commented price over value but still bought
        "value": [],  # "Not enough value for the price"
        "cost buy": [],  # Commented high cost for area but still bought
        "cost": []  # "I won't pay that here"
    }
    rep_score = 0  # Daily Repscore
    sold_out_text = 0
    rep_modifier = 1 + (stats["reputation"] / 4)
    prod_markup = constants.PRODUCT_VALUE_MAX_INCREASE

    prod_value = (  # Product Value
        cost_to_make(stats) *
        prod_markup *
        rep_modifier
      )

    for count, i in enumerate(constants.LOCATION_NAMES):
        if (
            stats["location"][f"{count+1}"]["purchased"] and
            stats["location"][f"{count+1}"]["cart_lvl"] > 0 and
            stats["location"][f"{count+1}"]["staff_lvl"] > 0
        ):
            cust_count.append(0)
            open_loc_name.append(constants.LOCATION_NAMES[count])
            open_loc_num.append(count+1)
            loc_sale_value.append(0)
            feedback["cost"].append(0)
            feedback["cost buy"].append(0)
            feedback["value"].append(0)
            feedback["value buy"].append(0)

    total_locations = len(open_loc_name)
    cust_chance = []
    product_cost = cost_to_make(stats)
    portions = get_portions_avaliable(stats)
    footfall = constants.LOCATION_FOOTFALL

    for i in range(total_locations):
        SFI = constants.STAFF_FOOTFALL_INCREASE
        staff_lvl = stats["location"][str(open_loc_num[i])]["staff_lvl"]
        z = 1 + ((SFI * staff_lvl) / 100)
        cust_chance.append((540 / (footfall[i] * rep_modifier * z))*100)

    while True:
        for i in range(total_locations):
            x = randrange(floor(cust_chance[i]))

            while x <= 100:
                will_buy = False
                goto_1 = False
                goto_2 = False
                goto_3 = False

                # Base selling price > what customer likes pay at location.
                osp = constants.OPTIMAL_SELLING_PRICE[open_loc_name[i]]
                osp = osp * rep_modifier
                if price > osp:
                    goto_1 = True
                else:
                    goto_2 = True

                # Base selling price <= optimal + max increase.
                max_markup = constants.MAX_PRICE_OVER_OPTIMAL
                if goto_1 and (price - osp) / max_markup < randrange(100):
                    will_buy = True
                    feedback["cost buy"][i] += 1
                elif goto_1:
                    feedback["cost"][i] += 1
                    rep_score -= 1

                # Product value * max markup is > base selling price.
                if goto_2 and (price >= prod_value):
                    goto_3 = True
                elif goto_2:
                    will_buy = True
                    rep_score += 1

                # Diff between .
                diff = price - prod_value
                if goto_3 and (diff / prod_markup) * 100 <= randrange(100):
                    will_buy = True
                    feedback["value buy"][i] += 1
                elif goto_3:
                    feedback["value"][i] += 1
                    rep_score -= 1

                # Customer is happy to buy product
                if will_buy:
                    cust_count[i] += 1
                    portions -= 1
                    CSI = constants.CART_SELLING_INCREASE
                    # Location cart level
                    cl = stats["location"][str(open_loc_num[i])]["cart_lvl"]
                    # Selling Price Modifier i.e 1.05
                    spm = 1 + ((CSI * cl) / 100)
                    sales_value = (price * spm) - product_cost
                    loc_sale_value[i] += sales_value
                    stats["cash"] += sales_value

                    if portions == 0:
                        break

                x = randrange(floor(cust_chance[i]))

            if portions == 0:
                break

        if portions == 0:
            sold_out_text = red(f'SOLD OUT at {hour}:{minute}')
            minute = 59

            if hour < 12:
                hour = 11
            else:
                hour = 16

        minute += 1

        if minute == 60:
            minute = 00
            hour += 1

        if hour == 12 and minute == 00:
            for i in range(total_locations):
                sold += cust_count[i]
            stats = deduct_stock(stats, sold)
            data = [
                cust_count, sold,
                open_loc_name, loc_sale_value,
                sold_out_text, feedback, rep_score
            ]
            clear_terminal()
            text = cyan("12 noon time sales report:")
            print(f'{text}')
            stats = sales_report(stats, data)
            break

        if hour == 17:
            for i in range(total_locations):
                sold += cust_count[i]
            stats = deduct_stock(stats, sold)
            data = [
                cust_count, sold,
                open_loc_name, loc_sale_value,
                sold_out_text, feedback, rep_score
            ]
            clear_terminal()
            text = cyan("End of day sales report:")
            print(f'{text}')
            stats = sales_report(stats, data)
            break

    stats["day"] += 0.5
    daily_menu(stats)


def rep_change(stats, rep_score, sold):
    '''
    Calculates if reputations needs to be changed after daily sales
    performance. Then updates player stats.
    '''
    rep_percent = rep_score / sold
    c_rep = stats["reputation"]

    print(f'{cyan("Reputation update:")}')
    print('------------------------------------')

    if rep_percent > 0.5:
        print('HAPPY CUSTOMERS and GREAT PERFORMANCE!')
    elif rep_percent < 0.5:
        print('Bad performance... Check feedback on what to change.')

    if rep_percent > 0.5 and c_rep < 5:
        stats["reputation"] += 0.5
        print(
            f"{green('Reputation increase:')}\
                {gold('-' + str(stats['reputation']))}"
            )
    elif rep_percent > 0.5 and c_rep == 5:
        print(gold("Reputation already at a 5!"))
    elif rep_percent < 0.5 and c_rep > 0:
        stats["reputation"] -= 0.5
        print(
            f"{red('Reputation decrease:')}\
            {gold('-' + str(stats['reputation']))}"
            )
    elif rep_percent < 0.5 and c_rep == 0:
        print(red("Reputation already at 0."))
    else:
        print("No reputation change")

    print('------------------------------------')

    return stats


def sales_report(stats, data):
    '''
    Print sales report to terminal
    '''
    cust_count = data[0]
    sold = data[1]
    open_loc_name = data[2]
    loc_sale_value = data[3]
    sold_out_text = data[4]
    feedback = data[5]
    rep_score = data[6]
    if sold_out_text:
        print(sold_out_text)
    total_sale_value = 0
    for i in loc_sale_value:
        total_sale_value += i
    print('------------------------------------')
    print(f'{"Location":<13}{"-":<3}{"Units":<8}{"-":<3}{"Value (£)":<8}')
    print('------------------------------------')
    for count, i in enumerate(cust_count):
        text = open_loc_name[count]
        text2 = i
        text3 = floor(loc_sale_value[count]*100)/100
        print(f'{text:<13}{"-":<3}{text2:<8}{"-":<3}{text3:<8}')
    print('------------------------------------')
    text = green(f'{sold}')
    print(f'Total daily units sold: {text}')
    text = green(f'£{floor(total_sale_value*100)/100}')
    print(f'Total daily sales value: {text} (var +/- £0.01')
    print('\nSales values are net profit (Sold price minus product cost.')
    print_press_enter_to("Press Enter to see feedback..")
    print(f'\n{cyan("Customer feedback / improvemnts")}')
    print('-----------------------------------------------------------')
    print(f'{"Location":<13}{"-":<3}{"Amount":<6}{"-":<3}{"Comment":<13}')
    print('-----------------------------------------------------------')
    txt_bought = orange('(Bought)')
    txt_decline = red('(Declined)')

    for count, i in enumerate(cust_count):
        first = True
        for j in feedback:
            if feedback[j][count] > 0:
                if first:
                    text = open_loc_name[count]
                    dash = "-"
                    first = False
                else:
                    text = ""
                    dash = ""
                if j == "value buy":
                    text2 = f"{txt_bought}   Add a litttle more value."
                elif j == "value":
                    text2 = f"{txt_decline} Add much more value."
                elif j == "cost buy":
                    text2 = f"{txt_bought}   A little expensive."
                elif j == "cost":
                    text2 = f"{txt_decline} Well overpriced!"
                text3 = feedback[j][count]
                print(f'{text:<13}{dash:<3}{text3:<6}{"-":<3}{text2:<13}')
        if not first:
            print(
                '-----------------------------------------------------------'
                )

    print_press_enter_to("Press Enter to see if any reputation update...\n")
    rep_change(stats, rep_score, sold)

    if (stats["day"] % 1) == 0:
        print_press_enter_to("Press Enter to continue to MID-DAY\
 PREPARATION...")
    else:
        print_press_enter_to("Press Enter to continue to NEXT DAY...")

    return stats


def deduct_stock(stats, sold):
    '''
    Deduct any stock that has been sold and return stats back to calling
    function.
    '''
    stats["sausage"] -= stats["recipe"]["sausage"] * sold
    stats["bun"] -= stats["recipe"]["bun"] * sold
    stats["onion"] -= stats["recipe"]["onion"] * sold
    stats["sauce"] -= stats["recipe"]["sauce"] * sold
    return stats


def get_portions_avaliable(stats):
    '''
    Return how many portions of hotdogs are avaliable based on stock and recipe
    '''
    p = 9999
    for i in constants.STOCK_OPTIONS:
        if stats["recipe"][i] > 0:
            x = stats[i] / stats["recipe"][i]
            if x < p:
                p = x
    return floor(p)


def save_data(stats, first_save):
    '''
    Save player data to database.
    The for loop looks through the coloumn 1 data from Google sheets.
    If it finds a match it updates that row. Else creates a new row with data.
    If "exit = True" go to main menu after save.
    '''

    def save_loop(i, data, save_percent):
        '''
        Inner function to save_data()
        Finds the correct row in Google sheet to save game data.
        '''
        j = 0
        for y in data:
            j += 1
            worksheet.update_cell(i, j, y)
            text = cyan(f' SAVING... {floor((j/save_percent)*100)}%')
            print(f'{text}', end='\r')
        return True

    def convert_dict_to_array(data, data_to_save):
        '''
        Inner function to save_data()
        Convert dict game data to an array so it can be saved to Google Sheet
        '''
        for i in data:
            if type(data[f'{i}']) is dict:
                convert_dict_to_array(data[f'{i}'], data_to_save)
            else:
                data_to_save.append(data[f"{i}"])
        return data_to_save

    if not first_save:
        text = cyan("Please do not close.")
        print(f'\n{text}')
    data_to_save = []
    data_to_save = convert_dict_to_array(stats, data_to_save)
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)
    found = False
    if not first_save:
        if int(stats["game_save_row"]) != int(0):
            i = stats["game_save_row"]
            found = save_loop(i, data_to_save, len(data_to_save))
        else:
            for cell_value in col_array:
                i += 1
                if cell_value == stats['user_id']:
                    found = save_loop(i, data_to_save, len(data_to_save))
                    break
        text = green("Data saved. Now safe to close.")
        print(f'{text}', end='\r')
    if not found or first_save:
        worksheet.append_row(data_to_save)
    print_press_enter_to("Press Enter to continue...")


def retrieve_save():
    '''
    Retrieve saved game data and resume game from where last left off.
    '''
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)
    found = False
    while not found:
        clear_terminal()
        text = cyan("Retrieve a previous game")
        print(f'{text}')
        print('------------------------------------')
        print('\nYou will need your game ID to retrieve a previous game.')
        print_go_back()
        text = orange("Enter Game ID:")
        user_input = input(f'\n{text}')
        # Cycle through rows in Google sheet until GAME ID finds a Match
        text = cyan("SEARCHING...")
        print(f'\n{text}')
        for i, cell_value in enumerate(col_array):
            if cell_value == user_input:
                found = True
                text = cyan("GAME FOUND...")
                print(f'\n{text}')
                # Copy data from row where GAME ID matches
                data = worksheet.row_values(i+1)
                stats = set_up_character(data, False)
                stats["game_save_row"] = i+1
                text = green("GAME LOADED.")
                print(f'\n{text}')
                print_press_enter_to("Press Enter to continue...")
                daily_menu(stats)
                break
        # If no GAME ID match then show error.
        if not found:
            print_error_message("No game found")


def purchase_location(stats):
    '''
    Purchase location menu for player
    '''
    LOC_NAME = constants.LOCATION_NAMES
    LOC_COST = constants.LOCATION_COSTS
    while True:
        clear_terminal()
        text = cyan("Purchase hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print('Each location purchase means more customer to sell to.\
 The better the location the more potential customers.\n')
        text = pink("TIP")
        print(f'{text}: Each location will need a cart and a staff member\
 before they sell any hotdogs.\n')

        for count, key in enumerate(LOC_NAME, start=1):
            str_part_1 = f'{count}. {key}'
            if not stats['location'][str(count)]['purchased']:
                str_part_2 = green("Avaliable")
                text = f'PURCHASE for £{LOC_COST[count - 1]}'
                str_part_3 = cyan(text)
                print(
                    f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}' +
                    ' - ' f'{str_part_3:<30}'
                    )
            else:
                str_part_2 = gold("Purchased")
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<52}')

        print_go_back()

        text = orange("Input choice:")
        user_choice = input(f'\n{text}')

        check_1 = True if validate_input(user_choice, 5) else None
        if check_1 and int(user_choice) > 0:
            check_2 = True
        else:
            break

        if check_2 and not stats['location'][str(user_choice)]['purchased']:

            remaining_cash = stats["cash"] - LOC_COST[int(user_choice)-1]
            check_3 = True
        else:
            print_error_message('Already Purchased')

        # Check if remaining cash will remain >= 0
        if check_3 and remaining_cash >= 0:
            stats['location'][str(user_choice)]['purchased'] = True
            var_1 = LOC_NAME[int(user_choice)-1]
            var_2 = LOC_COST[int(user_choice)-1]
            print(green(f'Your purchased {var_1} for £{var_2}'))
            stats["cash"] = remaining_cash
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")
        else:
            print_error_message("Not enough funds")

    daily_menu(stats)


def purchase_cart_menu(stats):
    '''
    Purchase cart menu for player
    '''
    LOC_NAME = constants.LOCATION_NAMES
    CART_PRICE = constants.CART_COSTS

    while True:
        clear_terminal()
        text = cyan("Purchase or upgrade carts at your\
 hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print(f'Each upgrade on a cart will produce better quality hotdogs. So\
 you will sell {constants.CART_SELLING_INCREASE}% more for each level on top\
 the base selling price without an penelties at that location.')
        text = pink("TIP")
        print(f'\n{text}: Each location will need a staff member before they\
 sell any hotdogs.\n')

        for x, y in enumerate(LOC_NAME, start=1):
            cart_level = stats['location'][str(x)]['cart_lvl']
            str_part_1 = f'{x}. {y}'
            if cart_level == 0:
                text = 'Not currently owned'
                str_part_2 = red(text)
            else:
                str_part_2 = cyan(f'Current level is {cart_level}')
            if not stats['location'][str(x)]['purchased']:
                str_part_3 = red('Purchase location first')
            elif cart_level == 0:
                str_part_3 = green(f'PURCHASE for £ {CART_PRICE[cart_level]}')
            elif cart_level == 5:
                text = 'No further upgrades'
                str_part_3 = gold(text)
            else:
                text = f'UPGRADE for £{CART_PRICE[cart_level]}'
                str_part_3 = green(text)
            print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<23}' + ' - ' f'{str_part_3:<18}')
        
        print_go_back()

        text = orange("Input choice (0-5):")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        # Make sure location has been purchased first
        if not stats['location'][str(user_choice)]['purchased']:
            print_error_message("Purchase Land")
            continue

        # Check if remaining cash will above 0 after purchase, if so continue, else loop
        cart_level = stats['location'][str(user_choice)]['cart_lvl']
        if cart_level == 5:
            print_error_message("Already at max level.")
            continue

        remaining_cash = stats["cash"] - CART_PRICE[cart_level]
        if remaining_cash >= 0:
            new_cart_lvl = cart_level + 1
            stats['location'][str(user_choice)]['cart_lvl'] = new_cart_lvl
            stats["cash"] = remaining_cash
            loc = int(user_choice) - 1
            text = f'Cart level {new_cart_lvl} purchased for {LOC_NAME[loc]} for £{CART_PRICE[cart_level]}.'
            print(green(text))
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")
        else:
            print_error_message("Not enough funds")

    daily_menu(stats)


def purchase_stock_menu(stats):
    '''
    Purchase stock menu
    '''
    while True:
        clear_terminal()
        text = cyan("Purchase consumable stock to purchase")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print_portions_in_stock(stats)
        print(constants.PURCHASE_STOCK_OPTIONS)
        print_go_back()
        print("\nThis will order the minimum amount of ingredants to fullfill\
 the amount of Hotdogs you want to sell.")
        text = orange("Input amount (max 99999): ")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 99999):
            continue

        if int(user_choice) == 0:
            break

        cost = 0
        basket = {  # Create empty basket
            "stock": [],
            "recipe": [],
            "portions": [],
            "cost": [],
            "total_qty_r": [],  # Total Qty Required
            "total_qty_c": []  # Total cost for item
        }

        for count, i in enumerate(constants.STOCK_OPTIONS):
            stock = constants.STOCK_OPTIONS[count]
            basket["stock"].append(stats[stock])
            basket["recipe"].append(stats['recipe'][stock])
            basket["portions"].append(constants.STOCK_COSTS[stock][1])
            basket["cost"].append(constants.STOCK_COSTS[stock][2])
            basket["total_qty_r"].append(
                ceil(
                    (
                        int(user_choice) -
                        (
                            basket["stock"][count] /
                            basket["recipe"][count]
                        )
                    ) /
                    basket["portions"][count] *
                    basket["recipe"][count]
                    )
                )

            if basket["total_qty_r"][count] < 0:
                basket["total_qty_r"][count] = 0

            basket["total_qty_c"].append(
                basket["total_qty_r"][count] *
                basket["cost"][count]
                )

            cost += basket["total_qty_c"][count]

        text = cyan("\nCheckout:")
        print(f'{text}')
        print(f'{"Item:":<10}{"Qty":<10}{"Portions":<10}{"SUB TOTAL:":<10}')
        print('------------------------------------')

        for count, i in enumerate(constants.STOCK_OPTIONS):
            text1 = constants.STOCK_OPTIONS[count]
            text2 = basket["total_qty_r"][count]
            text3 = basket["portions"][count] * basket["total_qty_r"][count]
            text4 = "{:.2f}".format(basket["total_qty_c"][count])
            print(f'{text1:<10} {text2:<10} {text3:<10} £{text4:<10}')

        print('------------------------------------')
        text = "{:.2f}".format(cost)
        text = green(f"£{text}")
        print(f'TOTAL COST: {text}')
        text = orange("Would you like to make this purchase? (type: yes) ")
        yes_no = input(f'\n{text}\n')

        if not validate_yes_no(yes_no):
            continue

        if yes_no.lower() in ['y', 'yes']:
            # Check if remaining cash will above 0 after purchase,
            # if so continue, else loop
            remaining_cash = stats["cash"] - cost

            if remaining_cash < 0:
                print_error_message("Not enough funds")
                continue

            # Update player stock with purchased items
            for count, i in enumerate(constants.STOCK_OPTIONS):
                stats[i] += (
                    basket["portions"][count] *
                    basket["total_qty_r"][count]
                )

            print(green('Purchase Successful'))
            stats["cash"] = remaining_cash
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")

        else:
            print(red('Purchase Aborted'))
            print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def puchase_staff_menu(stats):
    '''
    Hire and train staff menu
    '''
    loc_name = constants.LOCATION_NAMES
    staff_price = constants.STAFF_COSTS

    while True:
        clear_terminal()
        text = cyan("Hire and train staff for your\
 hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print('Better trained staff encourage returning customers meaning more\
 footfall.\n')
        text = pink("TIP")
        print(f'{text}: Each location will need a cart before they sell any\
 hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            staff_level = stats['location'][str(count)]['staff_lvl']
            str_part_1 = f'{count}. {key}'
            if staff_level == 0:
                text = 'Vacant position'
                str_part_2 = red(text)
            else:
                text = f'Current level is {staff_level}'
                str_part_2 = cyan(text)
            if not stats['location'][str(count)]['purchased']:
                text = 'Purchase location first'
                str_part_3 = red(text)
            elif staff_level == 0:
                text = f'PURCHASE for £ {staff_price[staff_level]}'
                str_part_3 = green(text)
            elif staff_level == 5:
                text = 'No traning required'
                str_part_3 = gold(text)
            else:
                text = f'TRAIN for £{staff_price[staff_level]}'
                str_part_3 = green(text)
            print(
                f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<23}' +
                ' - ' f'{str_part_3:<18}'
                )

        print_go_back()

        text = orange("Input choice (0-5):")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        # Make sure location has been purchased first
        if not stats['location'][str(user_choice)]['purchased']:
            print_error_message("Purchase Land")
            continue

        # Check if remaining cash < 0 after purchase, if
        # so continue, else pass
        staff_level = stats['location'][str(user_choice)]['staff_lvl']
        if staff_level == 5:
            print_error_message("Already at max level.")
            continue

        remaining_cash = stats["cash"] - staff_price[staff_level]
        if remaining_cash < 0:
            print_error_message("Not enough funds")
            continue

        new_staff_lvl = staff_level + 1
        stats['location'][str(user_choice)]['staff_lvl'] = new_staff_lvl
        stats["cash"] = remaining_cash
        loc = int(user_choice) - 1
        text = f'Staff level {new_staff_lvl} purchased for\
 {loc_name[loc]} for £{staff_price[staff_level]}.'
        print(green(text))
        text = f'Remaining balance {print_current_balance(stats)}'
        print(cyan(text))
        print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def change_recipe_menu(stats):
    '''
    Player is able to change recipe menu
    '''

    def validate_recipe_change(data):
        '''
        Check user input for recipe change is valid
        '''
        if len(data) == 1 and data[0] == str(0):
            return True
        if len(data) != 2:
            text = red('Check instructions and try again.')
            print(f'{text}')
            print_press_enter_to("Press Enter to continue...")
        else:
            if validate_input(data[0], 999) and validate_input(data[1], 999):
                return True
        return False

    while True:
        clear_terminal()
        bun = green(stats['recipe']['bun'])
        sausage = green(stats['recipe']['sausage'])
        onion = green(stats['recipe']['onion'])
        sauce = green(stats['recipe']['sauce'])
        text = cyan("Make changes to your recipe")
        print(f'\n{text}')
        print('------------------------------------')

        print(cyan("\nCurrent Recipe:"))
        print('------------------------------------')
        text1 = cyan("Ingrediant")
        text2 = cyan("Portions per serving")
        print(f'{text1:<12}{"|":<2}{text2:<0}')
        print('------------------------------------')
        print(f'{"1. Buns":<12}{"|":<2}{f"{bun}":<4} (Min 1 - Max 1)')
        print(f'{"2. Sausages":<12}{"|":<2}{f"{sausage}":<4} (Min 1 - Max 2)')
        print(f'{"3. Onions":<12}{"|":<2}{f"{onion}":<4} (Min 0 - Max 5)')
        print(f'{"4. Sauce":<12}{"|":<2}{f"{sauce}":<4} (Min 0 - Max 5)')
        prod_cost = cost_to_make(stats)
        markup = constants.PRODUCT_VALUE_MAX_INCREASE
        prod_cost *= markup
        text = pink(f'£{str("{:.2f}".format(prod_cost))}')
        print(f'\nCurrent base product value is: {text}')
        print_go_back()
        print('\nTo update your recipe type the ingrediant and amount i.e.\
 "3 4".\n')
        text = orange("Enter change i.e. 3 4:")
        user_choice = input(f'{text}')
        user_choice = user_choice.split()
        if validate_recipe_change(user_choice):
            if int(user_choice[0]) == 0:
                break
            if int(user_choice[0]) > 4:
                print_error_message("Invalid choice.")
            else:
                if (
                    (
                        int(user_choice[0]) == 1 and
                        int(user_choice[1]) > 1
                    ) or
                    (
                        int(user_choice[0]) == 2 and
                        int(user_choice[1]) > 2
                    ) or
                    (
                        int(user_choice[0]) == 3 and
                        int(user_choice[1]) > 5
                    ) or
                    (
                        int(user_choice[0]) == 4 and
                        int(user_choice[1]) > 5
                    )
                ):
                    print_error_message("Check maximum amounts.")
                else:
                    if (
                        (
                            int(user_choice[0]) == 1 and
                            int(user_choice[1]) < 1
                        ) or
                        (
                            int(user_choice[0]) == 2 and
                            int(user_choice[1]) < 1
                        ) or
                        (
                            int(user_choice[0]) == 3 and
                            int(user_choice[1]) < 0
                        ) or
                        (
                            int(user_choice[0]) == 4 and
                            int(user_choice[1]) < 0
                        )
                    ):
                        print_error_message("Check minimum amounts.")
                    else:
                        stock_choosen = constants.STOCK_OPTIONS[int(user_choice[0])-1]
                        stats['recipe'][stock_choosen] = int(user_choice[1])
                        text = green(f'Updated\
 {stock_choosen.capitalize()} to {user_choice[1]} per serving.')
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
        text = cyan("Set the selling price of your\
 product")
        print(f'{text}')
        print('------------------------------------')
        production_cost = cost_to_make(stats)
        text = green("£" + str(round(production_cost, 2)))
        print(f'\nThe current cost for to make your your product is {text}')
        text = green("£"+"{:.2f}".format(stats["selling_price"]))
        print(f'\nCurrent selling price is {text}')
        net_profit = round(curr_price - production_cost, 2)

        if net_profit >= 0:
            text = green("Profit per serving is:")
            print(f'\n{text}£{net_profit}')
        else:
            text = red("Loss per serving is: ")
            print(f'\n{text}£{net_profit}')

        print_go_back()
        text = orange("Enter new price: £")
        new_price = input(f'\n{text}')

        if validate_price_change(new_price):
            if float(new_price) == 0:
                break
            new_price = round(float(new_price), 2)
            stats["selling_price"] = float(new_price)
            text = green(f'\nUpdated selling price to\
 £{"{:.2f}".format(new_price)}')
            print(text)
            print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def cost_to_make(stats):
    '''
    Works out the cost of making each hotdog
    '''
    bun = (
        stats['recipe']['bun'] *
        constants.STOCK_COSTS['bun'][2] /
        constants.STOCK_COSTS['bun'][1]
    )

    sausage = (
        stats['recipe']['sausage'] *
        constants.STOCK_COSTS['sausage'][2] /
        constants.STOCK_COSTS['sausage'][1]
    )

    onion = (
        stats['recipe']['onion'] *
        constants.STOCK_COSTS['onion'][2] /
        constants.STOCK_COSTS['onion'][1]
    )

    sauce = (
        stats['recipe']['sauce'] *
        constants.STOCK_COSTS['sauce'][2] /
        constants.STOCK_COSTS['sauce'][1]
    )

    return bun + sausage + onion + sauce


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


def create_user_name():
    '''
    Allow user to create their own name for the game
    '''
    while True:
        # Get player input
        text = orange("What name would you like to use?")
        user_name = input(f'{text}\n')
        print('')
        if user_name:
            while True:
                print(f'Hello {user_name}\n')
                # Get player input
                text = orange("Would you like to change\
 your name? (yes / no) ")
                yes_no = input(f'{text}\n')
                print('')
                if validate_yes_no(yes_no):
                    if yes_no.lower() in ['n', 'no']:
                        return user_name
                    else:
                        break


def create_user_id(user_name):
    '''
    Creates user ID and checks to make sure not already in user
    before showing user.
    '''
    user_id = ''
    print('Please wait why your new user ID is created...')
    while True:
        user_id = "".join(
            string.ascii_uppercase[random.randrange(0, 25)] for x in range(6)
            )
        user_data = SHEET.worksheet('user_data')
        cell_list = user_data.findall(user_id)
        if len(cell_list) == 0:
            break
    clear_terminal()
    print('Welcome to your new game. The first thing we need to do is set you\
 up with a new new account.\n')
    print('------------------------------------')
    print('USER ID CREATED')
    print('------------------------------------')
    print(
        f'\n{user_name}, your new user ID is: {green(user_id)}\n'
        )
    print(
        'Please keep this safe as this is how you can retrieve your progress'
        )
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
    if value.lower() in ['y', 'ye', 'yes', 'n', 'no']:
        return True
    else:
        print_error_message("invalid input")
        return False


def print_error_message(data):
    '''
    Function to provide appropriate error message
    '''
    if data:
        text = red(data)
    else:
        text = red('Error.')
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
    text = cyan("Your current stock:")
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
    text = orange(f'\n{text}')
    input(f'{text}')


def print_go_back():
    '''
    Print 0. Go Back in yellow
    '''
    text = utils.colored(255, 255, 0, '\n0. Go Back')
    print(text)


def main():
    '''
    Main functions to run once code has loaded
    '''
    main_menu()


# Setting default text color
print(utils.colored(0, 0, 0, 'text'))
main()
