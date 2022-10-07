'''
utils
'''
import os


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
    Changes to PINK if printed to termail
    '''
    return colored(255, 105, 180, text)


def gold(text):
    '''
    Changes to GOLD if printed to termail
    '''
    return colored(255, 215, 0, text)


def green(text):
    '''
    Changes to GREEN if printed to termail
    '''
    return colored(50, 205, 50, text)


def cyan(text):
    '''
    Changes to CYAN if printed to termail
    '''
    return colored(0, 255, 255, text)


def orange(text):
    '''
    Changes to ORANGE if printed to termail
    '''
    return colored(255, 165, 0, text)


def red(text):
    '''
    Changes to RED if printed to termail
    '''
    return colored(255, 0, 0, text)


def yellow(text):
    '''
    Changes to YELLOW if printed to termail
    '''
    return colored(255, 255, 0, text)


# Credit:
# https://www.codegrepper.com/code-examples
# /python/how+to+color+text+in+python+3
def colored(c_red, c_green, c_blue, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(
        c_red, c_green, c_blue, text
        )
