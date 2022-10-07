'''
Daily game menu
'''
from math import ceil
from game import (run_day, end_game)
from utils import (
  cyan, clear_terminal, gold, pink, green, print_go_back,
  print_press_enter_to, red, orange, print_error_message,
  print_current_balance, print_portions_in_stock,
  validate_input, validate_yes_no, yellow
  )
from save_load import (save_data)
from shared import (cost_to_make)
import constants


def daily_menu(stats):
    '''
    Daily player menu to purchase upgrades and make changes to recipes
    '''
    clear_terminal()

    if (stats["day"] % 1) == 0:
        text_time_of_day = pink("Morning")
    else:
        text_time_of_day = pink("Afternoon")

    while True:
        print(menu_string(stats, text_time_of_day))
        user_choice = input(orange(f'\n{"Input choice (0-8) :"}'))
        if validate_input(user_choice, 8):
            break

    if user_choice == '1':
        purchase_location(stats)
    elif user_choice == '2':
        purchase_cart_menu(stats)
    elif user_choice == '3':
        puchase_staff_menu(stats)
    elif user_choice == '4':
        purchase_stock_menu(stats)
    elif user_choice == '5':
        change_recipe_menu(stats)
    elif user_choice == '6':
        set_selling_price(stats)
    elif user_choice == '7':
        result, stats = run_day(stats)
        if result:
            end_game(stats)
        daily_menu(stats)
    elif user_choice == '8':
        help_menu(stats)
    elif user_choice == '0':
        save_data(stats, False)


def menu_string(stats, text_time_of_day):
    '''
    Doc string for daily game menu
    '''
    return f"""
{gold(stats["name"])}
------------------------------------
Current balance {stats["cash"]}
Day: {stats["day"]} out of {constants.LAST_DAY}
Time of Day: {text_time_of_day}
Company reputation:

{cyan('Choose from the following options:')}
------------------------------------
1. Purchase location
2. Purchase / upgrade cart(s)
3. Hire / upgrade staff
4. Purchase stock
5. Change Recipe
6. Set selling prices

{pink("7. Start trading")}
{gold("8. Help")}
{yellow('0. Save and quit')}"""


def purchase_location(stats):
    '''
    Purchase location menu for player
    '''
    loc_name = constants.LOCATION_NAMES
    loc_cost = constants.LOCATION_COSTS

    while True:
        clear_terminal()
        print(f'{cyan("Purchase hotdog pitch locations")}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print('Each location purchase means more customer to sell to.\
 The better the location the more potential customers.\n')
        text = pink("TIP")
        print(f'{text}: Each location will need a cart and a staff member\
 before they sell any hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            str_part_1 = f'{count}. {key}'

            if not purchase_loc_try(stats, count):
                str_part_2 = red("Not yet avaliable")
                text = f'PURCHASE for £{loc_cost[count - 1]}'
                print(
                    f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}'
                    )
            elif not stats['location'][str(count)]['purchased']:
                str_part_2 = green("Avaliable")
                text = f'PURCHASE for £{loc_cost[count - 1]}'
                print(
                    f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}' +
                    ' - ' f'{cyan(text):<30}'
                    )
            else:
                str_part_2 = gold("Purchased")
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<52}')

        print_go_back()
        user_choice = input(f'\n{orange("Input choice: ")}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        if (
            not stats['location'][str(user_choice)]['purchased'] and
            purchase_loc_try(stats, int(user_choice))
        ):
            remaining_cash = stats["cash"] - loc_cost[int(user_choice)-1]
        elif not purchase_loc_try(stats, int(user_choice)):
            print_error_message('Can not make this purchase yet.')
            continue
        else:
            print_error_message('Already Purchased.')
            continue

        # Check if remaining cash will remain >= 0
        if remaining_cash >= 0:
            stats['location'][str(user_choice)]['purchased'] = True
            var_1 = loc_name[int(user_choice)-1]
            var_2 = loc_cost[int(user_choice)-1]
            print(green(f'Your purchased {var_1} for £{var_2}'))
            stats["cash"] = remaining_cash
            print(cyan(f'Remaining balance {print_current_balance(stats)}'))
            print_press_enter_to("Press Enter to continue...")
        else:
            print_error_message("Not enough funds")

    daily_menu(stats)


def purchase_loc_try(stats, count):
    '''
    Error check for buying location
    '''
    try:
        stats['location'][str(count - 1)]['purchased']
    except KeyError:
        return True
    else:
        return stats['location'][str(count-1)]['purchased']


def purchase_cart_menu(stats):
    '''
    Purchase cart menu for player
    '''
    loc_name = constants.LOCATION_NAMES
    cart_price = constants.CART_COSTS

    while True:
        clear_terminal()
        text = cyan("Purchase or upgrade carts at your\
 hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print(f'Each upgrade on a cart will produce better quality hotdogs. So\
 you will sell {constants.CART_SELLING_INCREASE}% more for each level on top\
 the base selling price without an penelties at that location.')
        text = pink("TIP")
        print(f'\n{text}: Each location will need a staff member before they\
 sell any hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            cart_level = stats['location'][str(count)]['cart_lvl']
            str_part_1 = f'{count}. {key}'
            if cart_level == 0:
                text = 'Not currently owned'
                str_part_2 = red(text)
            else:
                str_part_2 = cyan(f'Current level is {cart_level}')
            if not stats['location'][str(count)]['purchased']:
                str_part_3 = red('Purchase location first')
            elif cart_level == 0:
                str_part_3 = green(f'PURCHASE for £ {cart_price[cart_level]}')
            elif cart_level == 5:
                text = 'No further upgrades'
                str_part_3 = gold(text)
            else:
                text = f'UPGRADE for £{cart_price[cart_level]}'
                str_part_3 = green(text)
            print(
                f'{str_part_1:<16}' + ' - ' +
                f'{str_part_2:<23}' + ' - ' +
                f'{str_part_3:<18}'
                )

        print_go_back()

        text = orange("Input choice (0-5): ")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        # Make sure location has been purchased first
        if not stats['location'][str(user_choice)]['purchased']:
            print_error_message("Purchase Land")
            continue

        # Check if remaining cash will above 0 after purchase, if so continue,
        # else loop
        cart_level = stats['location'][str(user_choice)]['cart_lvl']
        if cart_level == 5:
            print_error_message("Already at max level.")
            continue

        remaining_cash = stats["cash"] - cart_price[cart_level]
        if remaining_cash >= 0:
            new_cart_lvl = cart_level + 1
            stats['location'][str(user_choice)]['cart_lvl'] = new_cart_lvl
            stats["cash"] = remaining_cash
            loc = int(user_choice) - 1
            text = f'Cart level {new_cart_lvl} purchased for {loc_name[loc]} \
 for £{cart_price[cart_level]}.'
            print(green(text))
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")
        else:
            print_error_message("Not enough funds")

    daily_menu(stats)


def puchase_staff_menu(stats):
    '''
    Hire and train staff menu
    '''
    loc_name = constants.LOCATION_NAMES
    staff_price = constants.STAFF_COSTS

    while True:
        clear_terminal()
        text = cyan("Hire and train staff for your\
 hotdog pitch locations")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print('Better trained staff encourage returning customers meaning more\
 footfall.\n')
        text = pink("TIP")
        print(f'{text}: Each location will need a cart before they sell any\
 hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            staff_level = stats['location'][str(count)]['staff_lvl']
            str_part_1 = f'{count}. {key}'
            if staff_level == 0:
                text = 'Vacant position'
                str_part_2 = red(text)
            else:
                text = f'Current level is {staff_level}'
                str_part_2 = cyan(text)
            if not stats['location'][str(count)]['purchased']:
                text = 'Purchase location first'
                str_part_3 = red(text)
            elif staff_level == 0:
                text = f'PURCHASE for £ {staff_price[staff_level]}'
                str_part_3 = green(text)
            elif staff_level == 5:
                text = 'No traning required'
                str_part_3 = gold(text)
            else:
                text = f'TRAIN for £{staff_price[staff_level]}'
                str_part_3 = green(text)
            print(
                f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<23}' +
                ' - ' f'{str_part_3:<18}'
                )

        print_go_back()

        text = orange("Input choice (0-5): ")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        # Make sure location has been purchased first
        if not stats['location'][str(user_choice)]['purchased']:
            print_error_message("Purchase Land")
            continue

        # Check if remaining cash < 0 after purchase, if
        # so continue, else pass
        staff_level = stats['location'][str(user_choice)]['staff_lvl']
        if staff_level == 5:
            print_error_message("Already at max level.")
            continue

        remaining_cash = stats["cash"] - staff_price[staff_level]
        if remaining_cash < 0:
            print_error_message("Not enough funds")
            continue

        new_staff_lvl = staff_level + 1
        stats['location'][str(user_choice)]['staff_lvl'] = new_staff_lvl
        stats["cash"] = remaining_cash
        loc = int(user_choice) - 1
        text = f'Staff level {new_staff_lvl} purchased for\
 {loc_name[loc]} for £{staff_price[staff_level]}.'
        print(green(text))
        text = f'Remaining balance {print_current_balance(stats)}'
        print(cyan(text))
        print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def purchase_stock_menu(stats):
    '''
    Purchase stock menu
    '''
    while True:
        clear_terminal()
        text = cyan("Purchase consumable stock to purchase")
        print(f'{text}')
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}\n')
        print_portions_in_stock(stats)
        print(constants.PURCHASE_STOCK_OPTIONS)
        print_go_back()
        print("\nThis will order the minimum amount of ingredants to fullfill\
 the amount of Hotdogs you want to sell.")
        text = orange("Input amount (max 99999): ")
        user_choice = input(f'\n{text}')

        if not validate_input(user_choice, 99999):
            continue

        if int(user_choice) == 0:
            break

        cost = 0
        basket = {  # Create empty basket
            "stock": [],
            "recipe": [],
            "portions": [],
            "cost": [],
            "total_qty_r": [],  # Total Qty Required
            "total_qty_c": []  # Total cost for item
        }

        for count, i in enumerate(constants.STOCK_OPTIONS):
            stock = constants.STOCK_OPTIONS[count]
            basket["stock"].append(stats[stock])
            basket["recipe"].append(stats['recipe'][stock])
            basket["portions"].append(constants.STOCK_COSTS[stock][1])
            basket["cost"].append(constants.STOCK_COSTS[stock][2])
            basket["total_qty_r"].append(
                ceil(
                    (
                        int(user_choice) -
                        (
                            basket["stock"][count] /
                            basket["recipe"][count]
                        )
                    ) /
                    basket["portions"][count] *
                    basket["recipe"][count]
                    )
                )

            if basket["total_qty_r"][count] < 0:
                basket["total_qty_r"][count] = 0

            basket["total_qty_c"].append(
                basket["total_qty_r"][count] *
                basket["cost"][count]
                )

            cost += basket["total_qty_c"][count]

        text = cyan("\nCheckout:")
        print(f'{text}')
        print(f'{"Item:":<10}{"Qty":<10}{"Portions":<10}{"SUB TOTAL:":<10}')
        print('------------------------------------')

        for count, i in enumerate(constants.STOCK_OPTIONS):
            text1 = constants.STOCK_OPTIONS[count]
            text2 = basket["total_qty_r"][count]
            text3 = basket["portions"][count] * basket["total_qty_r"][count]
            text4 = "{:.2f}".format(basket["total_qty_c"][count])
            print(f'{text1:<10} {text2:<10} {text3:<10} £{text4:<10}')

        print('------------------------------------')
        text = "{:.2f}".format(cost)
        text = green(f"£{text}")
        print(f'TOTAL COST: {text}')
        text = orange("Would you like to make this purchase? (type: yes) ")
        yes_no = input(f'\n{text}')

        if not validate_yes_no(yes_no):
            continue

        if yes_no.lower() in ['y', 'yes']:
            # Check if remaining cash will above 0 after purchase,
            # if so continue, else loop
            remaining_cash = stats["cash"] - cost

            if remaining_cash < 0:
                print_error_message("Not enough funds")
                continue

            # Update player stock with purchased items
            for count, i in enumerate(constants.STOCK_OPTIONS):
                stats[i] += (
                    basket["portions"][count] *
                    basket["total_qty_r"][count]
                )

            print(green('Purchase Successful'))
            stats["cash"] = remaining_cash
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")

        else:
            print(red('Purchase Aborted'))
            print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def change_recipe_menu(stats):
    '''
    Player is able to change recipe menu
    '''

    def validate_recipe_change(data):
        '''
        Check user input for recipe change is valid
        '''
        if len(data) == 1 and data[0] == str(0):
            return True
        if len(data) != 2:
            text = red('Check instructions and try again.')
            print(f'{text}')
            print_press_enter_to("Press Enter to continue...")
        else:
            if validate_input(data[0], 999) and validate_input(data[1], 999):
                return True
        return False

    while True:
        clear_terminal()

        bun = green(stats['recipe']['bun'])
        sausage = green(stats['recipe']['sausage'])
        onion = green(stats['recipe']['onion'])
        sauce = green(stats['recipe']['sauce'])

        print(f'\n{cyan("Make changes to your recipe")}')
        print('------------------------------------')
        print(cyan("\nCurrent Recipe:"))
        print('------------------------------------')
        print(f'{cyan("Ingrediant"):<12}{"|":<2}\
 {cyan("Portions per serving"):<0}')
        print('------------------------------------')
        print(f'{"1. Buns":<12}{"|":<2}{f"{bun}":<4} (Min 1 - Max 1)')
        print(f'{"2. Sausages":<12}{"|":<2}{f"{sausage}":<4} (Min 1 - Max 2)')
        print(f'{"3. Onions":<12}{"|":<2}{f"{onion}":<4} (Min 0 - Max 5)')
        print(f'{"4. Sauce":<12}{"|":<2}{f"{sauce}":<4} (Min 0 - Max 5)')

        prod_cost = cost_to_make(stats)
        markup = constants.PRODUCT_VALUE_MAX_INCREASE
        text = green(f'£{str("{:.2f}".format(prod_cost))}')
        print(f'\nCost to make each hotdog you sell: {text}')
        prod_cost *= markup
        text = gold(f'£{str("{:.2f}".format(prod_cost))}')
        print(f'Current base product value is: {text}')
        print(f'\n{pink("TIP:")} Use this to guide your selling price')
        print('\nTo update your recipe type the ingrediant and amount i.e. \
 "3 4".')
        print_go_back()
        user_choice = input(f'\n{orange("Enter change i.e. 3 4: ")}')
        user_choice = user_choice.split()

        if not validate_recipe_change(user_choice):
            continue

        if int(user_choice[0]) == 0:
            break

        if int(user_choice[0]) > 4:
            print_error_message("Invalid choice.")
            continue

        if (
            (int(user_choice[0]) == 1 and int(user_choice[1]) > 1) or
            (int(user_choice[0]) == 2 and int(user_choice[1]) > 2) or
            (int(user_choice[0]) == 3 and int(user_choice[1]) > 5) or
            (int(user_choice[0]) == 4 and int(user_choice[1]) > 5)
        ):
            print_error_message("Check maximum amounts.")
            continue

        if (
            (int(user_choice[0]) == 1 and int(user_choice[1]) < 1) or
            (int(user_choice[0]) == 2 and int(user_choice[1]) < 1) or
            (int(user_choice[0]) == 3 and int(user_choice[1]) < 0) or
            (int(user_choice[0]) == 4 and int(user_choice[1]) < 0)
        ):
            print_error_message("Check minimum amounts.")
            continue

        stock_choosen = (constants.STOCK_OPTIONS[int(user_choice[0])-1])
        stats['recipe'][stock_choosen] = int(user_choice[1])
        text = green(f'Updated {stock_choosen.capitalize()} to \
 {user_choice[1]} per serving.')
        print(text)
        print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def set_selling_price(stats):
    '''
    Allow user to set selling price of hotdogs
    '''
    while True:
        clear_terminal()
        curr_price = stats["selling_price"]
        text = cyan("Set the selling price of your product")
        print(f'{text}')
        print('------------------------------------')
        production_cost = cost_to_make(stats)
        text = green("£" + str(round(production_cost, 2)))
        print(f'\nThe current cost for to make your your product is {text}')
        text = green("£"+"{:.2f}".format(stats["selling_price"]))
        print(f'\nCurrent selling price is {text}')
        net_profit = round(curr_price - production_cost, 2)

        if net_profit >= 0:
            text = green("Profit per serving is:")
            print(f'\n{text}£{net_profit}')
        else:
            text = red("Loss per serving is: ")
            print(f'\n{text}£{net_profit}')

        print_go_back()
        text = orange("Enter new price: £")
        new_price = input(f'\n{text}')

        if validate_price_change(new_price):
            if float(new_price) == 0:
                break
            new_price = round(float(new_price), 2)
            stats["selling_price"] = float(new_price)
            text = green(f'\nUpdated selling price to\
 £{"{:.2f}".format(new_price)}')
            print(text)
            print_press_enter_to("Press Enter to continue...")

    daily_menu(stats)


def validate_price_change(data):
    '''
    Check user input valid value for price change
    '''
    try:
        try:
            float_value = float(data)
        except TypeError:
            print_error_message("Invalid input.")
            return False
        if float_value >= 0:
            return True
        raise ValueError()
    except ValueError:
        print_error_message("Invalid input.")
        return False
    return True


def help_menu(stats):
    '''
    Displays help screen to the user
    '''
    clear_terminal()
    print(constants.HELP_SCREEN1)
    print_press_enter_to("Press Enter to continue...")
    print(constants.HELP_SCREEN2)
    print_press_enter_to("Press Enter to continue...")
    print(constants.HELP_SCREEN3)
    print_press_enter_to("Press Enter to continue...")
    print(constants.HELP_SCREEN4)
    print_press_enter_to("Press Enter to return to menu...")
    daily_menu(stats)
