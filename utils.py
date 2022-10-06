def main_menu_header(red, green, blue, text):
    colored_text = colored(red, green, blue, text)
    return f"""
************************************
{colored_text}
************************************
MAIN MENU
------------------------------------
Can you prove that you are able to take a small hotdog stand and turn it into \
a great hotdog empire?!"""


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


# Credit:
# https://www.codegrepper.com/code-examples/python/how+to+color+text+in+python+3
def colored(red, green, blue, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(
        red, green, blue, text
        )
