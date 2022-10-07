'''
functions to save and reload game data
'''

from math import (floor)
from utils import (
    cyan, green, orange, print_go_back, print_press_enter_to,
    clear_terminal, print_error_message
    )

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
        text = cyan("Please do not close.")
        print(f'\n{text}')

    data_to_save = []
    data_to_save = convert_dict_to_array(stats, data_to_save)
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)
    found = False

    if not first_save:
        if int(stats["game_save_row"]) != int(0):
            row = stats["game_save_row"]
            found = save_loop(row, data_to_save, len(data_to_save), worksheet)
        else:
            for row, key in enumerate(col_array, 1):
                if key == stats['user_id']:
                    found = save_loop(
                        row, data_to_save, len(data_to_save), worksheet
                        )
                    break

        text = green("Data saved. Safe to continue.")
        print(f'{text}', end='\r')

    if not found or first_save:
        worksheet.append_row(data_to_save)

    print_press_enter_to("Press Enter to continue...")


def save_loop(row, data, save_percent, worksheet):
    '''
    Finds the correct row in Google sheet to save game data.
    '''
    for count, key in enumerate(data, 1):
        worksheet.update_cell(row, count, key)
        text = cyan(f' SAVING... {floor((count/save_percent)*100)}%')
        print(f'{text}', end='\r')

    return True


def convert_dict_to_array(data, data_to_save):
    '''
    Convert dict game data to an array so it can be saved to Google Sheet
    '''
    for key in data:
        if isinstance(data[f'{key}'], dict):
            convert_dict_to_array(data[f'{key}'], data_to_save)
        else:
            data_to_save.append(data[f"{key}"])

    return data_to_save


def retrieve_save():
    '''
    Retrieve saved game data and resume game from where last left off.
    '''
    worksheet = SHEET.worksheet("user_data")
    col_array = worksheet.col_values(1)

    while True:
        clear_terminal()

        print(f'{cyan("Retrieve a previous game")}')
        print('------------------------------------')
        print('\nYou will need your game ID to retrieve a previous game.')
        print_go_back()
        user_input = input(f'\n{orange("Enter Game ID: ")}')

        if user_input == '0':
            return None
        if len(str(user_input)) != 6:
            print_error_message("\nNot a valid Game ID.")
            continue

        print(f'\n{cyan("SEARCHING...")}')

        # Cycle through rows in Google sheet until GAME ID finds a match
        for count, key in enumerate(col_array):
            if key != user_input:
                continue

            # Copy data from row where GAME ID matches
            data = worksheet.row_values(count + 1)
            stats = set_up_character(data, False)
            stats["game_save_row"] = count + 1

            if stats["game_over"]:
                print_error_message("\nGame already completed")
                break

            return stats
        else:
            # If no GAME ID match then show error.
            print_error_message("No game found")


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
