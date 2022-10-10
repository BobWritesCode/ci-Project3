'''
functions to save and reload game data
'''

from math import (floor)
from utils import (cyan, green, orange, print_go_back, print_press_enter_to,
                   clear_terminal, print_error_message)
import constants

# gspread constants

SCOPE = constants.SCOPE
CREDS = constants.CREDS
SCOPED_CREDS = constants.SCOPED_CREDS
GSPREAD_CLIENT = constants.GSPREAD_CLIENT
SHEET = constants.SHEET


def save_data(stats, first_save):
    '''
    Save player data to database.
    The for loop looks through the coloumn 1 data from Google sheets.
    If it finds a match it updates that row. Else creates a new row with data.
    If "exit = True" go to main menu after save.
    '''

    if not first_save:
        print(f'\n{cyan("Please do not close.")}')

    data_to_save = []
    data_to_save = convert_dict_to_array(stats, data_to_save)
    worksheet = SHEET.worksheet("user_data")
    row_array = worksheet.row_values(1)
    found = False

    if not first_save:
        if int(stats["game_save_row"]) != int(0):
            col = stats["game_save_row"]
            found = save_loop(col, data_to_save, data_to_save, worksheet)
        else:
            for col, key in enumerate(row_array, 1):
                if key == stats['user_id']:
                    found = save_loop(
                        col, data_to_save, data_to_save, worksheet
                        )
                    break

        print(f'{green("Data saved. Safe to continue.")}', end='\r')

    if not found or first_save:
        worksheet.append_row(data_to_save)

    print_press_enter_to("Press Enter to continue...")


def save_loop(col, data, save_percent, worksheet):
    '''
    Saves data[] to the correct row in Google.
    '''

    # CREDIT :
    # https://stackoverflow.com/questions/23861680/convert-spreadsheet
    # -number-to-column-letter
    column_int = int(col)
    start_index = 1  # it can start either at 0 or at 1
    letter = ''
    while column_int > 25 + start_index:
        letter += chr(65 + int((column_int-start_index)/26) - 1)
        column_int = column_int - (int((column_int-start_index)/26))*26
    letter += chr(65 - start_index + (int(column_int)))

    s_col = f'user_data!{letter}1'
    SHEET.values_update(
        s_col,
        params={'valueInputOption': 'RAW'},
        body={'values': data}
    )

    return True


def convert_dict_to_array(data, data_to_save):
    '''
    Convert dict game data to an array so it can be saved to Google Sheet
    '''
    for key in data:
        if isinstance(data[f'{key}'], dict):
            convert_dict_to_array(data[f'{key}'], data_to_save)
        else:
            data_to_save.append([data[f"{key}"]])

    return data_to_save


def retrieve_save():
    '''
    Retrieve saved game data and resume game from where last left off.
    '''
    worksheet = SHEET.worksheet("user_data")
    row_array = worksheet.row_values(1)

    while True:
        clear_terminal()

        print(f'{cyan("Retrieve a previous game")}')
        print(constants.LINE)
        print('\nYou will need your game ID to retrieve a previous game.')
        print_go_back()

        user_input = input(f'\n{orange("Enter Game ID: ")}')

        if user_input == '0':
            break

        if len(str(user_input)) != 6:
            print_error_message("\nNot a valid Game ID.")
            continue

        print(f'\n{cyan("SEARCHING...")}')

        # Cycle through rows in Google sheet until GAME ID finds a match
        for count, key in enumerate(row_array):
            if key != user_input:
                continue

            # Copy data from row where GAME ID matches
            data = worksheet.col_values(count + 1)
            stats = set_up_character(data, False)
            stats["game_save_row"] = count + 1

            if stats["game_over"]:
                print_error_message("\nGame already completed")
                break

            return stats
        else:
            # If no Game ID match then show error.
            print_error_message("No game found")


def set_up_character(data, new_player):
    '''
    Function sets all new character stats to default values
    '''
    if new_player:
        user_id = data[0]
        name = data[1]
        data = [  # Player starting values
            user_id,  # 0 Game ID
            name,  # 1 Company name
            1.0,  # 2 Day
            float(constants.STARTING_CASH),  # 3 Cash
            float(0),  # 4 Reputation
            int(0),  # 5 Stock sausages
            int(0),  # 6 Stock Buns
            int(0),  # 7 Stock Onions
            int(0),  # 8 Stock Sauce
            int(1),  # 9 Recipe Buns
            int(1),  # 10 Recipe Sausage
            int(2),  # 11 Recipe Onions
            int(1),  # 12 Recipe Sauce
            float(2.50),  # 13 Selling Price
            False,  # 14 Location 1 Purchased
            int(0),  # 15 Location 1 Cart lvl
            int(0),  # 16 Location 1 Staff lvl
            False,  # 17 Location 2 Purchased
            int(0),  # 18 Location 2 Cart lvl
            int(0),  # 19 Location 2 Staff lvl
            False,  # 20 Location 3 Purchased
            int(0),  # 21 Location 3 Cart lvl
            int(0),  # 22 Location 3 Staff lvl
            False,  # 23 Location 4 Purchased
            int(0),  # 24 Location 4 Cart lvl
            int(0),  # 25 Location 4 Staff lvl
            False,  # 26 Location 5 Purchased
            int(0),  # 27 Location 5 Cart lvl
            int(0),  # 28 Location 5 Staff lvl
            False,  # 29 Game Over
            0  # 30 Database Row
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
