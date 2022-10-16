'''
Main game module
'''
from random import randrange
from string import ascii_uppercase
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

    # Get highscores from Google worksheet
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()

    # Header
    print(f'{yellow("**************************************")}')
    print(f'{cyan("Top 10 leaderboard for classic mode")}')
    print(f'{yellow("**************************************")}\n')

    # Show table headings
    print(f"#    {data[0][0]:<22}{ data[0][1]:<20}")
    print(constants.LINE)

    # Show top 10 with scores
    for index, key in enumerate(data[1:11], 1):
        print(f"{str(index)+'.':<4} {key[0]:<22}"
              + f'£ {"{:.2f}".format(float(key[1])):<20}')

    # Get user input to exit to main menu.
    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def main_menu():
    '''
    Display main menu and options
    '''
    while True:
        clear_terminal()
        # Display manu menu options.
        print(constants.MAIN_MENU_OPTIONS)

        # Get user input
        user_choice = input(orange("\nInput choice (1-4): "))

        # Validate user input
        if not validate_input(user_choice, 4):
            continue

        # Depending on user input perform listed action(s).
        if user_choice == '1':
            new_game()
        elif user_choice == '2':
            stats = retrieve_save()
            if stats is not None:
                daily_menu(stats)
        elif user_choice == '3':
            show_leaderboard_data()
        elif user_choice == '4':
            show_credits()
        elif user_choice == '0':
            print_error_message("Invalid choice.")


def new_game():
    '''
    Create new user and set up for a new game
    '''
    clear_terminal()

    # Header
    print(cyan("Let\'s get you set up:"))
    print(constants.LINE)

    # Heading text
    print('Welcome to your new game. The first thing we need to do is set '
          + 'you up with a\nnew account.')

    # Run create_user_name() for user to choose a company name.
    user_name = create_user_name()

    # Run create_user_id() to get a game ID.abs(x)
    user_id = create_user_id()

    data = [user_id, user_name]

    # Run set_up_character() to set up users game data.
    stats = set_up_character(data, True)

    # Save data
    save_data(stats, True)

    print_press_enter_to("Press Enter to continue...")

    # Show user backstory.
    background_story(stats)


def background_story(stats):
    '''
    Tell the user the background story
    '''
    clear_terminal()

    # Show backstory
    print(constants.BACKGROUND_STORY)

    print_press_enter_to("Press Enter to continue...")

    # Move to game menu.
    daily_menu(stats)


def create_user_name():
    '''
    Allow user to create their own name for the game
    '''
    while True:
        print(pink("\nChoose a name for your hotdog empire!"))
        print(f'\n{pink("Tip: ")}Must be more than 5 and less then 20 '
              + 'characters')

        # Get user input to choose company name.
        user_name = input(f'\n{orange("Company name: ")}')

        # Validate user has typed something.
        if not user_name:
            continue

        # Validate length of name user has chosen.
        if len(user_name) < 5 or len(user_name) > 20:
            print_error_message("Company name must be least 5 and no more "
                                + "than 20 characters")
            continue

        while True:
            # Feedback user choice to them.
            print(f'\n{gold(user_name)} has been born!\n')

            # Get user input to confirm to proceed with name.
            yes_no = input(orange('Are you happy with this name? (yes / no) '))

            # Validate user input
            if not validate_yes_no(yes_no):
                continue
            if yes_no.lower() in ['y', 'ye', 'yes']:
                return user_name
            if yes_no.lower() in ['n', 'no']:
                clear_terminal()
                break


def create_user_id():
    '''
    Creates user ID and checks to make sure not already in user
    before showing user.
    '''
    user_id = ''
    print('\nPlease wait why your new user ID is created...')

    # Create game ID
    while True:
        user_id = "".join(
            ascii_uppercase[randrange(0, 25)] for x in range(6)
            )
        user_data = SHEET.worksheet('user_data')
        # Make sure game Id does not exist in database,
        # If yes, create new ID.
        cell_list = user_data.findall(user_id)
        if len(cell_list) == 0:
            break

    clear_terminal()
    print(f'{cyan("User ID created")}')
    print(constants.LINE)
    # Show user game ID.
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
