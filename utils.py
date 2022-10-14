'''
utils
'''
from os import system, name
from math import floor


def validate_yes_no(value):
    '''
    Checks to make sure user typed expected response.
    Acceptable ['y','ye','yes','n','no'], return True
    Else return False.
    '''
    if value.lower() in ['y', 'ye', 'yes', 'n', 'no']:
        return True

    print_error_message("Invalid input.")
    return False


def validate_input(value, max_value):
    '''
    Inside the try, converts input string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if outside the expected range.
    '''
    try:
        try:
            int_value = int(value)
        except TypeError:
            print_error_message("Invalid input.")
            return False
        if int_value >= 0 and int_value <= int(max_value):
            return True
        raise ValueError()
    except ValueError:
        print_error_message("Invalid input.")
        return False
    return True


def print_current_balance(stats):
    '''
    Print cash statement
    '''
    return f'£{"{:.2f}".format(floor(stats["cash"]*100)/100)}'


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
    system('cls' if name == 'nt' else 'clear')


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
    print(f"\n{yellow('0. Go Back')}")


def pink(text):
    '''
    Changes to PINK if printed to terminal
    '''
    return coloured(255, 105, 180, text)


def gold(text):
    '''
    Changes to GOLD if printed to terminal
    '''
    return coloured(255, 215, 0, text)


def green(text):
    '''
    Changes to GREEN if printed to terminal
    '''
    return coloured(50, 205, 50, text)


def cyan(text):
    '''
    Changes to CYAN if printed to terminal
    '''
    return coloured(0, 255, 255, text)


def orange(text):
    '''
    Changes to ORANGE if printed to terminal
    '''
    return coloured(255, 165, 0, text)


def red(text):
    '''
    Changes to RED if printed to terminal
    '''
    return coloured(255, 0, 0, text)


def yellow(text):
    '''
    Changes to YELLOW if printed to terminal
    '''
    return coloured(255, 255, 0, text)


# Credit:
# https://www.codegrepper.com/code-examples
# /python/how+to+color+text+in+python+3
def coloured(c_red, c_green, c_blue, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(
        c_red, c_green, c_blue, text
        )
