# FUNCTION TO USER COLOR TEXT IN CONSTANTS

def colored(r, g, b, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text_choose_from_options = colored(0, 255, 255, 'Choose from the following options:')

# CONSTANTS START HERE

CART_COSTS = [200, 400, 600, 1000, 1600]
LOCATION_EXP_COST = [3.0, 3.5, 4.0, 5.0, 7.0]
LOCATION_FOOTFALL = [20, 40, 80, 160, 320]
LOCATION_NAMES = ["Cheap Street", "Meow Park", "Downtown", "The Mall", "Fairground"]
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
4. Credits"""

text_save = colored(255,255,0, '0. Save and quit')

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

{text_save}"""

PURCHASE_STOCK_OPTIONS = f"""
{text_choose_from_options}
------------------------------------
1. Pack of Hotdog buns (pack of {STOCK_COSTS['bun'][1]}) £{STOCK_COSTS['bun'][2]}.00
2. Pack of Hotdogs (pack of {STOCK_COSTS['sausage'][1]}) £{STOCK_COSTS['sausage'][2]}.00
3. Onion (Makes {STOCK_COSTS['onion'][1]} portions) £{STOCK_COSTS['onion'][2]}.00
4. Jar of Special Sauce ({STOCK_COSTS['sauce'][1]} portions) £{STOCK_COSTS['sauce'][2]}.00

5. Buy X portions of recipe hotdogs"""