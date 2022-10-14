'''
functions to save and reload game data
'''
from math import (floor)
from utils import (cyan, green, orange, print_go_back, print_press_enter_to,
                   clear_terminal, print_error_message, gold)
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
    The for loop looks through row 1 data from Google sheets.
    If it finds a match it updates that row. Else creates a new
    column with data.
    '''
    # Do not run when character is set up.
    if not first_save:
        print(f'\n{cyan("Please do not close.")}')
        print(f'{gold("SAVING...")}')

    # Set up variables
    data_to_save = []
    found = False

    # Run function to convert dict to list, and return list
    data_to_save = convert_dict_to_array(stats, data_to_save)

    # Get data from Google Sheet.
    worksheet = SHEET.worksheet("user_data")
    row_array = worksheet.row_values(1)

    # Do not run when character is first set up
    if not first_save:
        # If player stats already have save column saved then
        # no need to search.
        if int(stats["game_save_row"]) != int(0):
            col = stats["game_save_row"]
            # Run save_loop() - Saves data.
            found = save_loop(col, data_to_save, worksheet)
        else:
            # If play stats do not have column save then search
            # array for correct column.
            for col, key in enumerate(row_array, 1):
                if key == stats['user_id']:
                    # Run save_loop() - Saves data.
                    found = save_loop(col, data_to_save, worksheet)
                    break

        print(f'{green("Data saved. Safe to continue.")}', end='\r')

    if not found or first_save:
        # Last empty column in worksheet.
        col = len(worksheet.row_values(1)) + 1
        # Run save_loop() - Saves data.
        found = save_loop(col, data_to_save, worksheet)


def save_loop(col, data, worksheet):
    '''
    Saves data[] to the correct row in Google.
    '''
    # Converts column number into letter notation used in spreadsheets
    # for columns. Example: 26 = Z, 27 = AA, 28 = AB...
    # CREDIT :
    # https://stackoverflow.com/questions/23861680/convert-spreadsheet
    # -number-to-column-letter
    column_int = int(col)
    start_index = 1
    letter = ''
    while column_int > 25 + start_index:
        letter += chr(65 + int((column_int-start_index)/26) - 1)
        column_int = column_int - (int((column_int-start_index)/26))*26
    letter += chr(65 - start_index + (int(column_int)))

    # Creates string for cell notation for spreadsheet.
    s_col = f'user_data!{letter}1'

    # Saves data to worksheet
    SHEET.values_update(s_col,
                        params={'valueInputOption': 'RAW'},
                        body={'values': data})

    return True


def convert_dict_to_array(data, data_to_save):
    '''
    Convert dict game data to an array so it can be saved to Google Sheet
    '''
    for key in data:
        if isinstance(data[f'{key}'], dict):
            # If key is a dict then loop function
            convert_dict_to_array(data[f'{key}'], data_to_save)
        else:
            # If key is not a dict then append to table.
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

        # Header
        print(f'{cyan("Retrieve a previous game")}')
        print(constants.LINE)

        # Show instructions to user
        print('\nYou will need your game ID to retrieve a previous game.')
        print_go_back()

        # Get user input of game ID.
        user_input = input(f'\n{orange("Enter Game ID: ")}')

        # If user input is 0 go back to main menu.
        if user_input == '0':
            break

        # If user input is not 6 character long show error message.
        if len(str(user_input)) != 6:
            print_error_message("\nNot a valid Game ID.")
            continue

        print(f'\n{cyan("SEARCHING...")}')

        # Cycle through row values until Game ID finds a match.
        for count, key in enumerate(row_array):
            if key != user_input:
                continue

            # Copy data from column where Game ID found match.
            data = worksheet.col_values(count + 1)

            # Run function set_up_character()
            # Converts data retrieved from worksheet into data format
            # game uses.
            stats = set_up_character(data, False)

            # To save searching again later for correct column when saving
            # apply correct column to game data.
            stats["game_save_row"] = count + 1

            # If game found but completed, show error message.
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
