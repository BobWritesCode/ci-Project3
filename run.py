'''
Main game module
'''
import random
import string
from utils import (yellow, green, cyan, pink, gold, orange,
                   print_press_enter_to, clear_terminal,
                   validate_input, validate_yes_no, print_error_message)
import constants
from save_load import (retrieve_save, set_up_character, save_data)
from game_menu import (daily_menu)

# Write your code to expect a terminal of 80 characters wide and 24 rows high
print(f'Preparing to start {constants.GAMETITLE}...\n')
print(pink('Welcome to Hotdog Tycoon'))

# gspread constants
SHEET = constants.SHEET


def show_leaderboard_data():
    '''
    Gets leaderbaord data from Google sheet and displays in terminal
    '''
    clear_terminal()
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    print(f'{yellow("************************************")}')
    print(f'{cyan("Top 10 highscores for classic mode")}')
    print(f'{yellow("************************************")}\n')
    print(f"{data[0][0]:<20}{ data[0][1]:<20}")

    print(constants.LINE)

    for key in data[1:10]:
        print(f"{key[0]:<20}{'£ ' +'{:.2f}'.format(float(key[1])):<20}")

    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def main_menu():
    '''
    Display main menu and options
    '''
    while True:
        clear_terminal()
        print(constants.MAIN_MENU_OPTIONS)
        text = orange("Input choice (1-4): ")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 4):
            continue

        if user_choice == '1':
            new_game()
        elif user_choice == '2':
            stats = retrieve_save()
            if stats is not None:
                daily_menu(stats)
            main_menu()
        elif user_choice == '3':
            show_leaderboard_data()
        elif user_choice == '4':
            show_credits()
        elif user_choice == '0':
            main()


def new_game():
    '''
    Create new user and set up for a new game
    '''
    clear_terminal()
    print(cyan("Let\'s get you set up:"))
    print(constants.LINE)
    print('Welcome to your new game. The first thing we need to do is set '
          + 'you up with a\nnew account.')
    user_name = create_user_name()
    user_id = create_user_id()
    data = [user_id, user_name]
    stats = set_up_character(data, True)
    save_data(stats, True)
    print_press_enter_to("Press Enter to continue...")
    background_story(stats)


def background_story(stats):
    '''
    Tell the user the background story
    '''
    clear_terminal()
    print(constants.BACKGROUND_STORY)
    print_press_enter_to("Press Enter to continue...")
    daily_menu(stats)


def create_user_name():
    '''
    Allow user to create their own name for the game
    '''
    while True:
        print(pink("\nChoose a name for your hotdog empire!"))
        print(f'\n{pink("Tip: ")}Must be more than 5 and less then 20 '
              + 'characters')
        user_name = input(f'\n{orange("Company name: ")}')

        if not user_name:
            continue

        if len(user_name) < 5 or length > 20:
            print_error_message("Company name must be least 5 and no more "
                                + "than 20 characters")
            continue

        print(f'\n{gold(user_name)} has been born!\n')
        yes_no = input(orange('Are you happy with this name? (yes / no) '))

        if not validate_yes_no(yes_no):
            continue

        if yes_no.lower() in ['y', 'ye', 'yes']:
            return user_name


def create_user_id():
    '''
    Creates user ID and checks to make sure not already in user
    before showing user.
    '''
    user_id = ''
    print('\nPlease wait why your new user ID is created...')

    while True:
        user_id = "".join(
            string.ascii_uppercase[random.randrange(0, 25)] for x in range(6)
            )
        user_data = SHEET.worksheet('user_data')
        cell_list = user_data.findall(user_id)
        if len(cell_list) == 0:
            break

    clear_terminal()
    print(f'{cyan("User ID created")}')
    print(constants.LINE)
    print(f'\nYour new user ID is: {green(user_id)}\n')
    print(f'{pink("Important: ")}Please keep this safe as this is how you '
          + 'can retrieve your progress.')
    return user_id


def show_credits():
    '''
    Display credits on screen
    '''
    clear_terminal()
    print(constants.CREDITS)
    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def main():
    '''
    Main functions to run once code has loaded
    '''
    main_menu()


# Setting default text color
print(cyan(''))
main()
