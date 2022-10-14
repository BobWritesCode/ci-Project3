'''
Daily game menu
'''
from math import (ceil, floor)
from game import (run_day, end_game)
from utils import (cyan, clear_terminal, gold, pink, green, print_go_back,
                   print_press_enter_to, red, orange, print_error_message,
                   print_current_balance,
                   validate_input, validate_yes_no, yellow)
from save_load import (save_data)
from shared import (cost_to_make, get_portions_available)
import constants


def daily_menu(stats):
    '''
    Daily player menu to purchase upgrades and make changes to recipes
    '''

    while True:
        clear_terminal()

        if (stats["day"] % 1) == 0:
            text_time_of_day = "Morning"
        else:
            text_time_of_day = "Afternoon"

        print(menu_string(stats, text_time_of_day))
        user_choice = input(orange(f'\n{"Input choice (0-8) : "}'))

        if not validate_input(user_choice, 8):
            continue

        if (not stats["location"]["1"]["purchased"]
                and user_choice == '7'):
            print_error_message("No locations purchased yet.")
            continue

        if (stats["location"]["1"]["cart_lvl"] == 0
                and user_choice == '7'):
            print_error_message("No carts purchased yet.")
            continue

        if (stats["location"]["1"]["staff_lvl"] == 0
                and user_choice == '7'):
            print_error_message("No staff purchased yet.")
            continue

        if (get_portions_available(stats) == 0
                and user_choice == '7'):
            # If both True
            print_error_message("You have no stock to sell.")
            continue

        break

    if user_choice == '1':
        purchase_location(stats)
    elif user_choice == '2':
        purchase_cart_menu(stats)
    elif user_choice == '3':
        purchase_staff_menu(stats)
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
        else:
            save_data(stats, False)
            daily_menu(stats)
    elif user_choice == '8':
        help_menu(stats)
    elif user_choice == '0':
        clear_terminal()
        print(f'\n{pink("IMPORTANT: ")} Make sure you write down your '
              + 'Game ID as you will need it to return to this game.')
        print(f'\nGame ID: {gold(stats["user_id"])}')
        save_data(stats, False)
        print_press_enter_to("\nPress Enter to go to main menu...")


def menu_string(stats, text_time_of_day):
    '''
    Doc string for daily game menu
    '''
    selling_price = "Base price: £{:.2f}".format(stats["selling_price"])
    recipe = "Cost: £{:.2f}".format(cost_to_make(stats))
    cash = "£{:.2f}".format(stats["cash"])
    stock = f"Stock: {get_portions_available(stats)}"

    action_cart = ""
    action_staff = ""
    action_loc = ""

    for key in stats["location"]:
        if (stats["location"][key]["purchased"]
                and stats["location"][key]["cart_lvl"] == 0):
            action_cart = "ACTION REQUIRED"
            break

    for key in stats["location"]:
        if (stats["location"][key]["purchased"]
                and stats["location"][key]["staff_lvl"] == 0):
            action_staff = "ACTION REQUIRED"
            break

    if not stats["location"]["1"]["purchased"]:
        action_loc = "ACTION REQUIRED"

    game_id = f'(Game ID : {cyan(stats["user_id"])})'
    company_name = stats['name']
    day = floor(stats["day"])

    return f"""{gold(company_name)} - {game_id}
{constants.LINE}
Current balance {green(cash)}
Day: {pink(day)} / {constants.LAST_DAY}
Time of Day: {pink(text_time_of_day)}
Company reputation: {gold(stats['reputation'])} / 5

{cyan('Choose from the following options:')}
{constants.LINE}
{'1. Purchase location':<33}{red(action_loc):<10}
{'2. Purchase / upgrade cart(s)':<33}{red(action_cart):<10}
{'3. Hire / upgrade staff':<33}{red(action_staff):<10}
{'4. Purchase stock':<33}{green(stock):<10}
{'5. Change Recipe':<33}{green(recipe):<10}
{'6. Set selling prices':<33}{green(selling_price):<10}

{pink("7. Start trading")} - Day {day} - {text_time_of_day}
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
        print(constants.LINE)
        print(f'Current balance {green(print_current_balance(stats))}\n')

        print('Each location purchase means more customers to sell to. '
              + 'The better the location \nthe more potential customers.\n')

        print(f'{pink("TIP")}: Each location will need a cart and a staff '
              + 'member before they sell any \nhotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            str_part_1 = f'{count}. {key}'

            if not purchase_loc_try(stats, count):
                print(f'{str_part_1:<16}' + ' - '
                      + f'{red("Not yet available"):<53}')

            elif not stats['location'][str(count)]['purchased']:
                text = f'PURCHASE for £{loc_cost[count - 1]}'
                print(f'{str_part_1:<16}' + ' - ' + f'{green("Available"):<53}'
                      + ' - ' f'{cyan(text):<30}')

            else:
                print(f'{str_part_1:<16}' + ' - '
                      + f'{gold("Purchased"):<52}')

        print_go_back()
        user_choice = input(f'\n{orange("Input choice: ")}')

        if not validate_input(user_choice, 5):
            continue

        if int(user_choice) == 0:
            break

        if (not stats['location'][str(user_choice)]['purchased']
                and purchase_loc_try(stats, int(user_choice))):
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
        print(f'{cyan("Purchase or upgrade carts at your hotdog pitch ")}'
              + f'{cyan("locations")}')
        print(constants.LINE)
        print(f'Current balance {green(print_current_balance(stats))}\n')
        print('Each upgrade on a cart will produce better quality hotdogs.'
              + f' So you will sell {constants.CART_SELLING_INCREASE}% more'
              + ' for each level on top the base selling price without any'
              + ' penalties at that \nlocation.')
        print(f'\n{pink("TIP")}: Each location will need a staff member'
              + ' before they sell any hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            cart_level = stats['location'][str(count)]['cart_lvl']
            str_part_1 = f'{count}. {key}'

            if cart_level == 0:
                str_part_2 = red('Not currently owned')
            else:
                str_part_2 = cyan(f'Current level is {cart_level}')

            if not stats['location'][str(count)]['purchased']:
                str_part_3 = red('Purchase location first')
            elif cart_level == 0:
                str_part_3 = green(f'PURCHASE for £ {cart_price[cart_level]}')
            elif cart_level == 5:
                str_part_3 = gold('No further upgrades')
            else:
                str_part_3 = green(f'UPGRADE for £{cart_price[cart_level]}')

            print(
                f'{str_part_1:<16}' + ' - ' +
                f'{str_part_2:<23}' + ' - ' +
                f'{str_part_3:<18}'
                )

        print_go_back()

        result = input(f'\n{orange("Input choice (0-5): ")}')

        if not validate_input(result, 5):
            continue

        if int(result) == 0:
            break

        # Make sure location has been purchased first.
        if not stats['location'][str(result)]['purchased']:
            print_error_message("Purchase Land")
            continue

        # Check if cart is not already at max level.
        cart_level = stats['location'][str(result)]['cart_lvl']
        if cart_level == 5:
            print_error_message("Already at max level.")
            continue

        # Check if remaining cash will above 0 after purchase, if so
        # continue, else loop.
        remaining_cash = stats["cash"] - cart_price[cart_level]
        if remaining_cash >= 0:
            new_cart_lvl = cart_level + 1
            stats['location'][str(result)]['cart_lvl'] = new_cart_lvl
            stats["cash"] = remaining_cash
            loc = int(result) - 1
            print(green(f'Cart level {new_cart_lvl} purchased for ')
                  + green(f'{loc_name[loc]} for £{cart_price[cart_level]}.'))
            print(cyan(f'Remaining balance {print_current_balance(stats)}'))
            print_press_enter_to("Press Enter to continue...")
            continue

        print_error_message("Not enough funds")
        continue

    daily_menu(stats)


def purchase_staff_menu(stats):
    '''
    Hire and train staff menu
    '''

    loc_name = constants.LOCATION_NAMES
    staff_price = constants.STAFF_COSTS

    while True:
        clear_terminal()
        print(cyan("Hire and train staff for your hotdog pitch")
              + cyan("locations."))
        print(constants.LINE)
        print(f'Current balance {green(print_current_balance(stats))}\n')
        print('Better trained staff encourage returning customers meaning more'
              + ' footfall.\n')
        print(f'{pink("TIP")}: Each location will need a cart before they sell'
              + ' any hotdogs.\n')

        for count, key in enumerate(loc_name, start=1):
            staff_level = stats['location'][str(count)]['staff_lvl']
            text1 = f'{count}. {key}'
            if staff_level == 0:
                text2 = red('Vacant position')
            else:
                text2 = cyan(f'Current level is {staff_level}')
            if not stats['location'][str(count)]['purchased']:
                text3 = red('Purchase location first')
            elif staff_level == 0:
                text3 = green(f'PURCHASE for £ {staff_price[staff_level]}')
            elif staff_level == 5:
                text3 = gold('No training required')
            else:
                text3 = green(f'TRAIN for £{staff_price[staff_level]}')

            print(f'{text1:<16}' + ' - ' + f'{text2:<23}'
                  + ' - ' f'{text3:<18}')

        print_go_back()

        user_choice = input(f'\n{orange("Input choice (0-5): ")}')

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
        print(green(f'Staff level {new_staff_lvl} purchased for')
              + green(f'{loc_name[loc]} for £{staff_price[staff_level]}.'))
        text = f'Remaining balance {print_current_balance(stats)}'
        print(cyan(text))
        print_press_enter_to("Press Enter to continue...")
        continue

    daily_menu(stats)


def purchase_stock_menu(stats):
    '''
    Purchase stock menu
    '''
    while True:
        clear_terminal()
        # Header
        print(f'{cyan("Purchase consumable stock")}')
        print(constants.LINE)
        print(f'Current balance {green(print_current_balance(stats))}')
        print('You have enough ingredients to sell '
              + f'{gold(get_portions_available(stats))} hotdogs.\n')

        # Show current ingredients in stock
        print(f'{cyan("Current stock:")}')
        print(constants.LINE)
        print(f'{stats["bun"]:<5} x {"Hotdog bun(s)":<20}'
              + f'| {stats["sausage"]:<5} x Sausage(s)')
        print(f'{stats["onion"]:<5} x {"Onion(s)":<20}'
              + f'| {stats["sauce"]:<5} x Special sauce(s)')

        # Show price list for ingredients
        print(constants.PURCHASE_STOCK_OPTIONS)

        # Tip to show.
        print(f"\n{pink('TIP: ')}This will purchase the amount of "
              + "ingredients you \nneed for the amount of hotdogs "
              + "you want to stock. All sales are final")

        print_go_back()

        # Get user input
        user_choice = input(orange('\nHow many hotdogs would you like to '
                            + 'have in stock? '))

        # Validation checks
        if not validate_input(user_choice, 99999):
            continue
        if int(user_choice) == 0:
            break

        # Setting up variables
        cost = 0
        basket = {  # Create empty basket
            "stock": [],
            "recipe": [],
            "portions": [],
            "cost": [],
            "total_qty_r": [],  # Total Qty Required
            "total_qty_c": []  # Total cost for item
        }

        # Calculate how many ingredients need to be purchased and thee
        # costs including total cost.
        for count, key in enumerate(constants.STOCK_OPTIONS):
            basket["stock"].append(stats[key])
            basket["recipe"].append(stats['recipe'][key])
            basket["portions"].append(constants.STOCK_COSTS[key][1])
            basket["cost"].append(constants.STOCK_COSTS[key][2])
            basket["total_qty_r"].append(
                ceil(
                    (
                        int(user_choice)
                        - (
                            basket["stock"][count]
                            / basket["recipe"][count]
                        )
                    )
                    / basket["portions"][count]
                    * basket["recipe"][count]
                    )
                )

            if basket["total_qty_r"][count] < 0:
                basket["total_qty_r"][count] = 0

            basket["total_qty_c"].append(
                basket["total_qty_r"][count]
                * basket["cost"][count]
                )

            cost += basket["total_qty_c"][count]

        # If cost is 0 then no ingredients required to be purchased
        # Show error to user then go back to beginning of loop.
        if cost == 0:
            print_error_message("\nYou already have this many hotdogs in "
                                + "stock.")
            continue

        # Displaying checkout to the user
        while True:
            clear_terminal()
            # Header
            print(f'\n{cyan("Checkout:")}')
            print(constants.LINE)
            print(f'{"Item:":<23}{"Qty:":<10}{"Portions:":<12}'
                  + f'{"Sub total:":<10}')
            print(constants.LINE)

            # Basket
            for count, key in enumerate(constants.STOCK_COSTS):
                text = (basket["portions"][count]
                        * basket["total_qty_r"][count])
                text2 = basket["total_qty_c"][count]
                print(f'{constants.STOCK_COSTS[key][0]:<23}'
                      + f'{basket["total_qty_r"][count]:<12}'
                      + f'{text:<10}'
                      + f'£{"{:.2f}".format(text2):<10}')

            print(constants.LINE)

            # Basket total
            print('TOTAL COST: ' + green(f"£{'{:.2f}'.format(cost)}"))

            # User input required
            user_choice = input(f'\n{orange("Would you like to make this")}'
                                + f'{orange(" purchase? (yes / no) ")}')

            # Validate user input
            if not validate_yes_no(user_choice):
                continue
            if user_choice.lower() in ['y', 'yes']:

                # Check if remaining cash will above 0 after purchase,
                # if so continue, else loop
                remaining_cash = stats["cash"] - cost
                if remaining_cash < 0:
                    print_error_message("Not enough funds")
                    break

                # Update player stock with purchased items
                for count, i in enumerate(constants.STOCK_OPTIONS):
                    stats[i] += (basket["portions"][count]
                                 * basket["total_qty_r"][count])

                # Purchase successful, update user cash balance.
                print(green('Purchase Successful'))
                stats["cash"] = remaining_cash
                print(cyan('Remaining balance '
                      + f'{print_current_balance(stats)}'))
                print_press_enter_to("Press Enter to continue...")
                break

            # Purchaser unsuccessful
            print(red('Purchase Aborted'))
            print_press_enter_to("Press Enter to continue...")
            break

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
            print(f'{red("Check instructions and try again.")}')
            print_press_enter_to("Press Enter to continue...")
        else:
            if validate_input(data[0], 999) and validate_input(data[1], 999):
                return True
        return False
        # def validate_recipe_change() end here

    # Main function thread starts here
    while True:
        clear_terminal()

        # Set variables
        bun = green(stats['recipe']['bun'])
        sausage = green(stats['recipe']['sausage'])
        onion = green(stats['recipe']['onion'])
        sauce = green(stats['recipe']['sauce'])

        # Display current recipe to user
        print(f'{cyan("Make changes to your recipe")}')
        print(constants.LINE)
        print(cyan("\nCurrent Recipe:"))
        print(constants.LINE)
        print(f'{cyan("Ingredient "):<12}{"|":<2}'
              + f'{cyan("Portions per serving"):<0}')
        print(constants.LINE)
        print(f'{"1. Buns":<12}{"|":<2}{f"{bun}":<4} (Min 1 - Max 1)')
        print(f'{"2. Sausages":<12}{"|":<2}{f"{sausage}":<4} (Min 1 - Max 2)')
        print(f'{"3. Onions":<12}{"|":<2}{f"{onion}":<4} (Min 0 - Max 5)')
        print(f'{"4. Sauce":<12}{"|":<2}{f"{sauce}":<4} (Min 0 - Max 5)')

        # Display cost to make each hotdog
        prod_cost = cost_to_make(stats)
        markup = constants.PRODUCT_VALUE_MAX_INCREASE
        text = green(f'£{str("{:.2f}".format(prod_cost))}')
        print(f'\nCost to make each hotdog you sell: {text}')

        # Display recommended retail cost to user
        prod_cost *= markup
        text = gold(f'£{str("{:.2f}".format(prod_cost + .50))}')
        print(f'Recommended retail price: {text}')
        print(f'\n{pink("TIP:")} Use this to guide your selling price.')

        print_go_back()

        # Show tip to user
        print(f'\n{pink("HOW: ")}To update your recipe type the ingredient'
              + ' and amount i.e. "3 4".')

        # Get user input to change recipe
        result = input(f'\n{orange("Enter change i.e. 3 4: ")}')
        # Split string into a list
        result = result.split()

        # Validate user input
        if not validate_recipe_change(result):
            continue
        if int(result[0]) == 0:
            break
        if int(result[0]) > 4:
            print_error_message("Invalid choice.")
            continue
        if ((int(result[0]) == 1 and int(result[1]) > 1)
                or (int(result[0]) == 2 and int(result[1]) > 2)
                or (int(result[0]) == 3 and int(result[1]) > 5)
                or (int(result[0]) == 4 and int(result[1]) > 5)):
            print_error_message("Check maximum amounts.")
            continue
        if ((int(result[0]) == 1 and int(result[1]) < 1)
                or (int(result[0]) == 2 and int(result[1]) < 1)
                or (int(result[0]) == 3 and int(result[1]) < 0)
                or (int(result[0]) == 4 and int(result[1]) < 0)):
            print_error_message("Check minimum amounts.")
            continue

        # Update variables
        stock_chosen = (constants.STOCK_OPTIONS[int(result[0])-1])
        stats['recipe'][stock_chosen] = int(result[1])

        # Display ingredient being change and to what  new amount
        print(green(f'Updated {stock_chosen.capitalize()} to '
                    + f'{result[1]} per serving.'))

        print_press_enter_to("Press Enter to continue...")
        continue

    daily_menu(stats)


def set_selling_price(stats):
    '''
    Allow user to set selling price of hotdogs
    '''
    while True:
        clear_terminal()

        # Set variable(s)
        curr_price = stats["selling_price"]
        production_cost = cost_to_make(stats)
        net_profit = round(curr_price - production_cost, 2)

        # Header
        print(f'{cyan("Set the selling price of your product")}')
        print(constants.LINE)

        # Display text to user
        text = green("£" + str(round(production_cost, 2)))
        print(f'\nThe current cost for to make your your product is {text}')
        text = green("£"+"{:.2f}".format(stats["selling_price"]))
        print(f'\nCurrent selling price is {text}')

        # Change colour of profit margin based on positive or negative
        # number.
        if net_profit >= 0:
            print(f'\n{green("Profit per serving is: ")}£{net_profit}')
        else:
            print(f'\n{red("Loss per serving is: ")}£{net_profit}')

        print_go_back()

        # Get user input for new selling price.
        new_price = input(f'\n{orange("Enter new price: £")}')

        # Validate user input
        if validate_price_change(new_price):

            # If user puts 0, go back to game menu.
            if float(new_price) == 0:
                break

            # Update selling price to user input
            new_price = round(float(new_price), 2)
            stats["selling_price"] = float(new_price)
            print(green('\nUpdated selling price to '
                        + f'£{"{:.2f}".format(new_price)}'))

            # User input to continue
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
