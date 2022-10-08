'''
Constants
'''
import gspread
from google.oauth2.service_account import Credentials
from utils import (cyan, pink, gold)

# gspread constants

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hotdog_Tycoon_Data')

# CONSTANTS START HERE

CART_COSTS = [50, 100, 200, 400, 800]
CART_SELLING_INCREASE = 5
GAMETITLE = 'Hotdog Empire Tycoon'
LAST_DAY = 10
LOCATION_FOOTFALL = [0.04, 0.08, 0.12, 0.20, 0.32]

LOCATION_NAMES = [
  "Cheap Street",
  "Central Park",
  "The Beach",
  "The Mall",
  "Fairground"
]

LOCATION_COSTS = [50, 150, 300, 600, 1200]

MAX_PRICE_OVER_OPTIMAL = 3  # £3 over optimal before 100% decline

OPTIMAL_SELLING_PRICE = {
  # Location : Optimal selling price before any bonuses
  LOCATION_NAMES[0]: 3.0,
  LOCATION_NAMES[1]: 3.5,
  LOCATION_NAMES[2]: 4.0,
  LOCATION_NAMES[3]: 5.0,
  LOCATION_NAMES[4]: 6.0
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
STAFF_COSTS = [50, 200, 400, 600, 800]
STAFF_FOOTFALL_INCREASE = 5

STARTING_CASH = 500

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

BACKGROUND_STORY = f"""------------------------------------
{cyan('Background')}
------------------------------------

You have hit some really hard times lately and nearly lost everything. \
Your down to your last £{STARTING_CASH}. Luckily your friend has told \
you about a sure way to earn some quick cash... HOTDOGS!
He has told you where you can do to buy your first hotdog cart and \
where you can set up for cheap. Everything else though is up to you.

You make your way down to the local hotdog supplies market and have a \
look around. Most of what you see is outside your budget but see there \
are a few things around to get you started...."""

CREDITS = f"""Credits:
------------------------------------
{"Code by:":<20}{"Warwick Hart":<40}
{"Inspired by:":<20}{"Lemonade Stand by Bob Jamison":<40}"""


MAIN_MENU_OPTIONS = f"""************************************
{gold('HOTDOG EMPIRE TYCOON')}
************************************

{cyan('MAIN MENU')}
------------------------------------
Can you prove that you are able to take a small hotdog stand and turn it into \
a great hotdog empire?!

{cyan('Choose from the following options:')}
------------------------------------
1. New Game
2. Retrieve a previous game
3. View leaderboard
4. Credits"""

PURCHASE_STOCK_OPTIONS = f"""{cyan('Pricing for products:')}
------------------------------------
Pack of Hotdog buns (pack of {STOCK_COSTS['bun'][1]}) \
  £{STOCK_COSTS['bun'][2]}.00
Pack of Hotdogs (pack of {STOCK_COSTS['sausage'][1]}) \
  £{STOCK_COSTS['sausage'][2]}.00
Onion (Makes {STOCK_COSTS['onion'][1]} portions) \
  £{STOCK_COSTS['onion'][2]}.00
Jar of Special Sauce ({STOCK_COSTS['sauce'][1]} portions) \
  £{STOCK_COSTS['sauce'][2]}.00"""


HELP_SCREEN1 = f"""{cyan('Help:')}
-----------------------------------------------------------------------------
{gold('Main Objective:')} Your main objective is to collect as much wealth
before the final day. At the end your wealth will determine your score.

{pink('Day cycle:')} Every day has 2 parts, morning and afternoon. The
morning starts at 8am and finishes at 12noon, you can do purchases in the
morning and afternoon. The afternoon is from 12noon to 5pm. The afternoon
is slightly longer.

{pink('Sales Report:')} After the morning and afternoon shifts you will get
a sales report. This will show you how much product you sold at each
location, the profit you made at each location, as well as feedback."""

HELP_SCREEN2 = f"""
{pink('Feedback:')} The feedback reports to you when customers are not fully
satisfied. So, no news is good news! Use this feedback to adjust your recipe
and pricing to make sure you are maximising profits.

{pink('Locations:')} You need to purchase locations to be able to set up new
hotdog stands. The better the location, the more footfall you will have and
the more the customer will be willing to spend."""

HELP_SCREEN3 = f"""
{pink('Carts:')} For each location you need to purchase a cart. As you
upgrade the carts you will make a better product at that cart. The better the
product the more the customer will be happy to pay for it.

{pink('Staff:')} For each location you will need to hire a staff member. As
you uptrain the staff, you will attract more customers to that cart.

{pink('Stock:')} Your stock is divided between all your carts on a first come
first served basis. You need to make sure you have enough stock to last that
part of the day (morning or afternoon). If you run out of stock, that
part of the day is over. Some good news though, stock will not perish
day-to-day but does not count towards your wealth at the end of the last day\
."""

HELP_SCREEN4 = f"""
{pink('Recipe')} Customers don't want to always pay top price and get no
value. You need to pay attention to customer feedback and adjust your recipe
accordingly. Though, the more ingredients you use the less profit margin you
make. And if you want to be top of the leader board then this could matter!

{gold('GOOD LUCK!')}"""
