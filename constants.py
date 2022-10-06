def colored(red, green, blue, text):
    '''
    Allows to change text colour
    '''
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
      red, green, blue, text
      )


text_choose_from_options = colored(
  0, 255, 255, 'Choose from the following options:'
  )

# CONSTANTS START HERE

CART_COSTS = [200, 400, 600, 1000, 1600]
CART_SELLING_INCREASE = 5
LAST_DAY = 20
LOCATION_FOOTFALL = [20, 40, 80, 160, 320]
LOCATION_NAMES = [
  "Cheap Street",
  "Meow Park",
  "Downtown",
  "The Mall",
  "Fairground"
]

LOCATION_COSTS = [200, 400, 600, 1000, 1600]

MAX_PRICE_OVER_OPTIMAL = 3  # £3 over optimal before 100% decline

OPTIMAL_SELLING_PRICE = {
  # Location : Optimal selling price before any bonuses
  LOCATION_NAMES[0]: 2.0,
  LOCATION_NAMES[1]: 3.0,
  LOCATION_NAMES[2]: 4.0,
  LOCATION_NAMES[3]: 5.0,
  LOCATION_NAMES[4]: 7.0
}

OPTIMAL_RECIPE = {
  # Location : Bun, Sausage, Onion, Sauce
  LOCATION_NAMES[0]: [1, 1, 1, 1],
  LOCATION_NAMES[1]: [1, 1, 2, 2],
  LOCATION_NAMES[2]: [1, 1, 3, 3],
  LOCATION_NAMES[3]: [1, 1, 3, 5],
  LOCATION_NAMES[4]: [1, 2, 5, 5]
}

PRODUCT_VALUE_MAX_INCREASE = 3  # 300% (Product value * 300%)
STAFF_COSTS = [200, 400, 600, 1000, 1600]
STAFF_FOOTFALL_INCREASE = 10

STARTING_CASH = 1000

STOCK_COSTS = {
  # id : [name, portions, cost]
  'bun': ['Pack of Hotdog Buns', 6, 1],
  'sausage': ['Pack of Hotdog Sausage', 8, 2],
  'onion': ['Onion', 10, 1],
  'sauce': ['Jar of Special Sauce', 20, 5]
}

STOCK_OPTIONS = [
  'bun',
  'sausage',
  'onion',
  'sauce'
]

BACKGROUND_STORY = f"""
------------------------------------
Background
------------------------------------

You have hit some really hard times lately and nearly lost everything. \
Your down to your last £{STARTING_CASH}. Luckily your friend has told \
you about a sure way to earn some quick cash... HOTDOGS!
He has told you where you can do to buy your first hotdog cart and \
where you can set up for cheap. Everything else though is up to you.

You make your way down to the local hotdog supplies market and have a \
look around. Most of what you see is outside your budget but see there \
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

text = colored(255, 255, 0, '0. Save and quit')

DAILY_MENU_OPTIONS = f"""
{text_choose_from_options}
------------------------------------
1. Purchase location
2. Purchase / upgrade cart(s)
3. Hire / upgrade staff
4. Purchase stock
5. Change Recipes
6. Set selling prices
7. Start trading

{text}"""

text = colored(0, 255, 255, 'Pricing for products:')

PURCHASE_STOCK_OPTIONS = f"""
{text}
------------------------------------
Pack of Hotdog buns (pack of {STOCK_COSTS['bun'][1]}) \
  £{STOCK_COSTS['bun'][2]}.00
Pack of Hotdogs (pack of {STOCK_COSTS['sausage'][1]}) \
  £{STOCK_COSTS['sausage'][2]}.00
Onion (Makes {STOCK_COSTS['onion'][1]} portions) \
  £{STOCK_COSTS['onion'][2]}.00
Jar of Special Sauce ({STOCK_COSTS['sauce'][1]} portions) \
  £{STOCK_COSTS['sauce'][2]}.00"""
