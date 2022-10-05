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


# Credit: https://www.codegrepper.com/code-examples/python/how+to+color+text+in+python+3
def colored(red, green, blue, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
        red, green, blue, text
        )
