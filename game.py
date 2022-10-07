'''
Runs the main part of the game
'''
from random import randrange
from math import floor
import constants
from utils import (
  cyan, red, clear_terminal, print_press_enter_to, orange, green, gold,
  pink
  )
from shared import (cost_to_make, get_portions_avaliable)
from save_load import (save_loop, save_data)

# gspread constants
SHEET = constants.SHEET


def run_day(stats):
    '''
    Runs the game code for each day.
    Day runs from 8 am until 5pm. 540 minutes in total.
    Each minute is a chance for something to happen.
    '''
    clear_terminal()

    if (stats["day"] % 1) == 0:
        hour = 8  # Game time, hours
    else:
        hour = 12  # Game time, hours

    price = stats["selling_price"]  # Selling Price
    minute = 00  # Game time, minute
    cust_count = []  # Temp customer count for AM and PM
    open_loc_name = []  # Open Location Name
    open_loc_num = []  # Open Location Number stats['location']['?']
    loc_sale_value = []  # Location Sales Value
    sold = 0  # Units sold for part of the day, resets mid-day.
    feedback = {  # Feedback table for declined sales
        "value buy": [],  # Commented price over value but still bought
        "value": [],  # "Not enough value for the price"
        "cost buy": [],  # Commented high cost for area but still bought
        "cost": []  # "I won't pay that here"
    }
    rep_score = 0  # Daily Repscore
    potential_cust = 0  # Total count for all potential customers
    sold_out_text = 0
    rep_modifier = 1 + (stats["reputation"] / 4)
    prod_markup = constants.PRODUCT_VALUE_MAX_INCREASE

    prod_value = (  # Product Value
        cost_to_make(stats) *
        prod_markup *
        rep_modifier
      )

    for count, i in enumerate(constants.LOCATION_NAMES):
        if (
            stats["location"][f"{count+1}"]["purchased"] and
            stats["location"][f"{count+1}"]["cart_lvl"] > 0 and
            stats["location"][f"{count+1}"]["staff_lvl"] > 0
        ):
            cust_count.append(0)
            open_loc_name.append(constants.LOCATION_NAMES[count])
            open_loc_num.append(count+1)
            loc_sale_value.append(0)
            feedback["cost"].append(0)
            feedback["cost buy"].append(0)
            feedback["value"].append(0)
            feedback["value buy"].append(0)

    total_locations = len(open_loc_name)
    cust_chance = []
    product_cost = cost_to_make(stats)
    portions = get_portions_avaliable(stats)
    footfall = constants.LOCATION_FOOTFALL

    for key in range(total_locations):
        staff_foot_inc = constants.STAFF_FOOTFALL_INCREASE
        staff_lvl = stats["location"][str(open_loc_num[key])]["staff_lvl"]
        staff_mod = 1 + ((staff_foot_inc * staff_lvl) / 100)
        cust_chance.append(
          (footfall[key] * rep_modifier * staff_mod)
            )

    while True:
        for key in range(total_locations):

            while cust_chance[key] * 100 >= randrange(0, 101):
                potential_cust += 1
                will_buy = False
                goto_1 = False
                goto_2 = False
                goto_3 = False

                # Base selling price > what customer likes pay at location.
                osp = constants.OPTIMAL_SELLING_PRICE[open_loc_name[key]]
                osp = osp * rep_modifier
                if price > osp:
                    goto_1 = True
                else:
                    goto_2 = True

                # Base selling price <= optimal + max increase.
                max_markup = constants.MAX_PRICE_OVER_OPTIMAL
                if goto_1 and (price - osp) / max_markup < randrange(100):
                    will_buy = True
                    feedback["cost buy"][key] += 1
                elif goto_1:
                    feedback["cost"][key] += 1
                    rep_score -= 1

                # Product value * max markup is > base selling price.
                if goto_2 and (price >= prod_value):
                    goto_3 = True
                elif goto_2:
                    will_buy = True
                    rep_score += 1

                # Diff between .
                diff = price - prod_value
                if goto_3 and (diff / prod_markup) * 100 <= randrange(100):
                    will_buy = True
                    feedback["value buy"][key] += 1
                elif goto_3:
                    feedback["value"][key] += 1
                    rep_score -= 1

                # Customer is happy to buy product
                if will_buy:
                    cust_count[key] += 1
                    portions -= 1
                    cart_sell_inc = constants.CART_SELLING_INCREASE
                    # Location cart level
                    cart_lvl = (
                        stats["location"][str(open_loc_num[key])]["cart_lvl"]
                    )
                    # Selling Price Modifier i.e 1.05
                    sell_price_mod = 1 + ((cart_sell_inc * cart_lvl) / 100)
                    sales_value = (price * sell_price_mod) - product_cost
                    loc_sale_value[key] += sales_value
                    stats["cash"] += sales_value

                    if portions == 0:
                        break

            if portions == 0:
                break

        if portions == 0:
            sold_out_text = red(f'SOLD OUT at {hour}:{minute}')
            minute = 59

            if hour < 12:
                hour = 11
            else:
                hour = 16

        minute += 1

        if minute == 60:
            minute = 00
            hour += 1

        if hour == 12 and minute == 00:
            for i in range(total_locations):
                sold += cust_count[i]
            stats = deduct_stock(stats, sold)
            data = [
                cust_count, sold,
                open_loc_name, loc_sale_value,
                sold_out_text, feedback, rep_score,
                potential_cust
            ]
            clear_terminal()
            text = cyan("12 noon time sales report:")
            print(f'{text}')
            stats = sales_report(stats, data)
            break

        if hour == 17:
            for i in range(total_locations):
                sold += cust_count[i]
            stats = deduct_stock(stats, sold)
            data = [
                cust_count, sold,
                open_loc_name, loc_sale_value,
                sold_out_text, feedback, rep_score,
                potential_cust
            ]
            clear_terminal()
            text = cyan("End of day sales report:")
            print(f'{text}')
            stats = sales_report(stats, data)
            break

    stats["day"] += 0.5
    if stats["day"] == constants.LAST_DAY + 1:
        return True, stats
    return False, stats


def sales_report(stats, data):
    '''
    Print sales report to terminal
    '''
    # cust_count = data[0]
    # sold = data[1]
    # open_loc_name = data[2]
    # loc_sale_value = data[3]
    # sold_out_text = data[4]
    # feedback = data[5]
    # rep_score = data[6]
    # potential_cust = data[7]
    if data[4]:
        print(data[4])
    total_sale_value = 0
    for i in data[3]:
        total_sale_value += i
    print('------------------------------------')
    print(f'{"Location":<13}{"-":<3}{"Units":<8}{"-":<3}{"Value (£)":<8}')
    print('------------------------------------')
    for count, i in enumerate(data[0]):
        text = data[2][count]
        text2 = i
        text3 = floor(data[3][count]*100)/100
        print(f'{text:<13}{"-":<3}{text2:<8}{"-":<3}{text3:<8}')
    print('------------------------------------')
    text = green(f'{data[1]}')
    print(f'Total daily units sold: {text}')
    text = green(f'£{floor(total_sale_value*100)/100}')
    print(f'Total daily sales value: {text} (var +/- £0.01)')
    print('\nSales values are net profit (Sold price minus product cost.')
    print_press_enter_to("Press Enter to see feedback..")
    print(f'\n{cyan("Customer feedback / improvements to be made:")}')
    print('-----------------------------------------------------------')
    print(f'{"Location":<13}{"-":<3}{"Amount":<6}{"-":<3}{"Comment":<13}')
    print('-----------------------------------------------------------')
    txt_bought = orange('(Bought)')
    txt_decline = red('(Declined)')

    for count, i in enumerate(data[0]):
        first = True
        for j in data[5]:
            if data[5][j][count] > 0:
                if first:
                    text = data[2][count]
                    dash = "-"
                    first = False
                else:
                    text = ""
                    dash = ""
                if j == "value buy":
                    text2 = f"{txt_bought}   Add a litttle more value."
                elif j == "value":
                    text2 = f"{txt_decline} Add much more value."
                elif j == "cost buy":
                    text2 = f"{txt_bought}   A little expensive."
                elif j == "cost":
                    text2 = f"{txt_decline} Well overpriced!"
                text3 = data[5][j][count]
                print(f'{text:<13}{dash:<3}{text3:<6}{"-":<3}{text2:<13}')
        if not first:
            print(
                '-----------------------------------------------------------'
                )

    print_press_enter_to("Press Enter to see if any reputation update...\n")
    rep_change(stats, data[6], data[7])

    if (stats["day"] % 1) == 0:
        print_press_enter_to("Press Enter to continue to MID-DAY\
 PREPARATION...")
    else:
        print_press_enter_to("Press Enter to continue to NEXT DAY...")

    return stats


def deduct_stock(stats, sold):
    '''
    Deduct any stock that has been sold and return stats back to calling
    function.
    '''
    stats["sausage"] -= stats["recipe"]["sausage"] * sold
    stats["bun"] -= stats["recipe"]["bun"] * sold
    stats["onion"] -= stats["recipe"]["onion"] * sold
    stats["sauce"] -= stats["recipe"]["sauce"] * sold
    return stats


def rep_change(stats, rep_score, oppotunities):
    '''
    Calculates if reputations needs to be changed after daily sales
    performance. Then updates player stats.
    '''
    rep_percent = (rep_score / oppotunities) if oppotunities != 0 else 0

    c_rep = stats["reputation"]

    print(f'{cyan("Reputation update:")}')
    print('------------------------------------')
    if rep_percent > 0.5:
        print('HAPPY CUSTOMERS and GREAT PERFORMANCE!')
    elif rep_percent < -0.5:
        print('Bad performance... Check feedback on what to change.')

    if rep_percent > 0.5 and c_rep < 5:
        stats["reputation"] += 0.5
        print(
            f"{green('Reputation increase:')}\
                {gold('+ 0.5')}"
            )
    elif rep_percent > 0.5 and c_rep == 5:
        print(gold("Reputation already at a 5!"))
    elif rep_percent < -0.5 and c_rep > 0:
        stats["reputation"] -= 0.5
        print(
            f"{red('Reputation decrease:')}\
            {gold('- 0.5')}"
            )
    elif rep_percent < -0.5 and c_rep == 0:
        print(red("Reputation already at 0."))
    else:
        print("No reputation change")

    print('------------------------------------')

    return stats


def end_game(stats):
    '''
    After last day has been completed, this function will save the player and
    upload their score to the leaderboard if they are in the top X of players.
    '''
    clear_terminal()
    stats["game_over"] = True
    print(f'{gold("CONGRATULATIONS!")}')
    print('\nYou completed the final day. Let\'s see how you did!')
    print('But first lets save your game!')

    save_data(stats, False)
    clear_terminal()

    cash = stats["cash"]
    rep = stats["reputation"]
    sum1 = 0
    sum2 = 0
    sum3 = 0

    for key in stats["location"]:
        sum1 += 1 if stats["location"][str(key)]["purchased"] else 0
        sum2 += stats["location"][str(key)]["cart_lvl"]
        sum3 += stats["location"][str(key)]["staff_lvl"]

    print(f'{gold("Your final score!")}\n')
    text = green("£" + str(floor(cash * 100) / 100))
    print(f'You managed to earn a whooping {text}')
    text = gold(str(sum1)) + pink(" / 5")
    print(f'\n{text} Locations purchased!')
    text = gold(str(sum2)) + pink(" / 25")
    print(f'{text} Carts purchased and upgraded!')
    text = gold(str(sum3)) + pink(" / 25")
    print(f'{text } Hired and uptrained staff!')
    text = gold(str(rep)) + pink(" / 5")
    print(f'{text} Reputation!')
    percent = (sum1 + sum2 + sum3 + rep) / 60
    text = gold(str(floor(percent * 100)) + "%")
    print(f'{text} Completion rating!')
    print('\nI hope you are happy with what you have achieved becuase I am.')
    print('Let\'s see if you managed to secure a place on our leaderboard.')

    top_10 = check_top_10()
    for count, key in enumerate(top_10[1:10], 2):
        if cash > float(key[1]):
            print(f'You placed {count - 1}')
            row = count
            data_to_save = [
                stats["name"],
                stats["cash"]
            ]
            worksheet = SHEET.worksheet("leaderboard")
            save_loop(row, data_to_save, len(data_to_save), worksheet)
            break
    else:
        print('Sadly you didn\'t make the top 10 this time. Maybe next time?')

    print(f'\n{gold("THANK YOU FOR PLAYING!")}')
    print_press_enter_to('Press Enter to quit.')
    stats = {}
    # main()


def check_top_10():
    '''
    Checks top 10 of leaderboard to see if user qualifies
    '''
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    return data
