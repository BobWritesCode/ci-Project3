# FUNCTION TO USER COLOR TEXT IN CONSTANTS

def colored(r, g, b, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text_choose_from_options = colored(0, 255, 255, 'Choose from the following options:')

# CONSTANTS START HERE

CART_COSTS = [200, 400, 600, 1000, 1600]

LOCATION_NAMES = ["Cheap Street", "Meow Park", "Downtown", "The Mall", "Stadium"]

LOCATION_COSTS = [200, 400, 600, 1000, 1600]

STAFF_COSTS = [200, 400, 600, 1000, 1600]

STOCK_OPTIONS = ['bun', 'sausage', 'onion', 'sauce']

STARTING_CASH = 1000

STOCK_COSTS = {
  # id : [name, portions, cost]
  'bun' : ['Pack of Hotdog Buns', 6, 1], 
  'sausage' : ['Pack of Hotdog Sausage', 8, 2], 
  'onion' : ['Onion', 10, 1], 
  'sauce' : ['Jar of Special Sauce', 20, 5]
}

BACKGROUND_STORY = f"""
------------------------------------
Background
------------------------------------

You have hit some really hard times lately and nearly lost everything.
Your down to your last £{STARTING_CASH}. Luckily your friend has told
you about a sure way to earn some quick cash... HOTDOGS!
He has told you where you can do to buy your first hotdog cart and
where you can set up for cheap. Everything else though is up to you.

You make your way down to the local hotdog supplies market and have a
look around. Most of what you see is outside your budget but see there
are a few things around to get you started...."""

CREDITS = f"""
Credits:
------------------------------------
{"Code by:":<20}{"Warwick Hart":<40}
{"Inspired by:":<20}{"Lemonade Stand by Bob Jamison":<40}"""


MAIN_MENU_OPTIONS = f"""
{text_choose_from_options}
------------------------------------
1. New Game
2. Retrieve a previous game
3. View leaderboard
4. Credits
"""


DAILY_MENU_OPTIONS = f"""
{text_choose_from_options}
------------------------------------
1. Purchase location
2. Purchase / upgrade cart(s)
3. Hire / upgrade staff
4. Purchase stock
5. Change Recipes
6. Set selling prices
7. Start trading (and save)
8. Print Stats
0. Save and quit
"""

PURCHASE_STOCK_OPTIONS = f"""
{text_choose_from_options}
------------------------------------
1. Pack of Hotdog buns (pack of 8) £{STOCK_COSTS['bun'][2]}.00
2. Pack of Hotdogs (pack of 6) £{STOCK_COSTS['sausage'][2]}.00
3. Onion (Makes 10 portions) £{STOCK_COSTS['onion'][2]}.00
4. Jar of Special Sauce (20 portions) £{STOCK_COSTS['sauce'][2]}.00"""