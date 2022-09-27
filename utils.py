def main_menu_header(r, g, b, text):
  colored_text = colored(r, g, b, text)
  return f"""
************************************
{colored_text}
************************************
MAIN MENU
------------------------------------
Can you prove that you are able to take a small hotdog stand and turn it into
a great hotdog empire?!
"""


# Credit: https://www.codegrepper.com/code-examples/python/how+to+color+text+in+python+3
def colored(r, g, b, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
