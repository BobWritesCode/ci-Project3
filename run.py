'''
Main game module
'''
from math import (floor, ceil)
import random
import string
from utils import (
    yellow, green, cyan, pink, gold, red, orange, print_go_back,
    print_press_enter_to, clear_terminal, print_error_message
    )
import constants
from shared import (cost_to_make)
from save import (save_data, retrieve_save, set_up_character, save_loop)
from game import (run_day)

# Write your code to expect a terminal of 80 characters wide and 24 rows high
print(f'Preparing to start {constants.GAMETITLE}...\n')
print(pink('Welcome to Hotdog Tycoon'))

# gspread constants

SHEET = constants.SHEET


def show_leaderboard_data():
    '''
    Gets leaderbaord data from Google sheet and displays in terminal
    '''
    clear_terminal()
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    print(f'{yellow("************************************")}')
    print(f'{cyan("Top 10 highscores for classic mode")}')
    print(f'{yellow("************************************")}\n')
    print(f"{data[0][0]:<20}{data[0][1]:<20}")
    print('------------------------------------')
    for key in data[1:10]:
        print(f"{key[0]:<20}{key[1]:<20}")
    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def check_top_10():
    '''
    Checks top 10 of leaderboard to see if user qualifies
    '''
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    return data


def main_menu():
    '''
    Display main menu and options
    '''
    clear_terminal()

    while True:
        print(constants.MAIN_MENU_OPTIONS)
        text = orange("Input choice: ")
        user_choice = input(f'\n{text}')
        if validate_input(user_choice, 4):
            break

    if user_choice == '1':
        new_game()
    elif user_choice == '2':
        stats = retrieve_save()
        if stats is not None:
            daily_menu(stats)
        main_menu()
    elif user_choice == '3':
        show_leaderboard_data()
    elif user_choice == '4':
        show_credits()
    elif user_choice == '0':
        main_menu()


def new_game():
    '''
    Create new user and set up for a new game
    '''
    clear_terminal()
    print(cyan("Let\' get you set up:"))
    print('------------------------------------')
    print('Welcome to your new game. The first thing we need to do is set you\
 up with a new account.\n')
    user_name = create_user_name()
    user_id = create_user_id()
    data = [user_id, user_name]
    stats = set_up_character(data, True)
    save_data(stats, True)
    background_story(stats)


def background_story(stats):
    '''
    Tell the user the background story
    '''
    clear_terminal()
    print(constants.BACKGROUND_STORY)
    print_press_enter_to("Press Enter to continue...")
    daily_menu(stats)


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
        print(cyan("Daily preparation"))
        print('------------------------------------')
        text = green(print_current_balance(stats))
        print(f'Current balance {text}')
        text = pink(int(floor(stats["day"])))
        print(f'Day: {text} out of {constants.LAST_DAY}')
        print(f'Time of Day: {text_time_of_day}')
        text = gold(stats['reputation'])
        print(f'Company reputation: {text} / 5')
        print(constants.DAILY_MENU_OPTIONS)
        text = orange("Input choice (0-8): ")
        user_choice = input(f'\n{text}')

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
        main()


def print_current_balance(stats):
    '''
    Print cash statment
    '''
    return f'£{"{:.2f}".format(floor(stats["cash"]*100)/100)}'


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


def purchase_location(stats):
    '''
    Purchase location menu for player
    '''
    loc_name = constants.LOCATION_NAMES
    loc_cost = constants.LOCATION_COSTS

    while True:
        clear_terminal()
        text = cyan("Purchase hotdog pitch locations")
        print(f'{text}')
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
            if not stats['location'][str(count)]['purchased']:
                str_part_2 = green("Avaliable")
                text = f'PURCHASE for £{loc_cost[count - 1]}'
                str_part_3 = cyan(text)
                print(
                    f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<53}' +
                    ' - ' f'{str_part_3:<30}'
                    )
            else:
                str_part_2 = gold("Purchased")
                print(f'{str_part_1:<16}' + ' - ' + f'{str_part_2:<52}')

        print_go_back()

        text = orange("Input choice: ")
        user_choice = input(f'\n{text}')

        check_1 = True if validate_input(user_choice, 5) else False
        if check_1 and int(user_choice) > 0:
            check_2 = True
        else:
            break

        if check_2 and not stats['location'][str(user_choice)]['purchased']:

            remaining_cash = stats["cash"] - loc_cost[int(user_choice)-1]
            check_3 = True
        else:
            print_error_message('Already Purchased')

        # Check if remaining cash will remain >= 0
        if check_3 and remaining_cash >= 0:
            stats['location'][str(user_choice)]['purchased'] = True
            var_1 = loc_name[int(user_choice)-1]
            var_2 = loc_cost[int(user_choice)-1]
            print(green(f'Your purchased {var_1} for £{var_2}'))
            stats["cash"] = remaining_cash
            text = f'Remaining balance {print_current_balance(stats)}'
            print(cyan(text))
            print_press_enter_to("Press Enter to continue...")
        else:
            print_error_message("Not enough funds")

    daily_menu(stats)


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
    main()


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


def create_user_name():
    '''
    Allow user to create their own name for the game
    '''
    while True:
        text = orange("Choose a name for your hotdog empire!")
        user_name = input(f'{text}\n')

        if not user_name:
            continue

        while True:
            print(f'\n{gold(user_name)} has been born!\n')
            text = orange("Are you happy with this name? (yes / no) ")
            yes_no = input(f'{text}')

            if not validate_yes_no(yes_no):
                continue

            if yes_no.lower() in ['y', 'ye', 'yes']:
                return user_name

            break


def create_user_id():
    '''
    Creates user ID and checks to make sure not already in user
    before showing user.
    '''
    user_id = ''
    print('\nPlease wait why your new user ID is created...')
    while True:
        user_id = "".join(
            string.ascii_uppercase[random.randrange(0, 25)] for x in range(6)
            )
        user_data = SHEET.worksheet('user_data')
        cell_list = user_data.findall(user_id)
        if len(cell_list) == 0:
            break
    clear_terminal()
    print(f'{cyan("User ID created")}')
    print('------------------------------------')
    print(
        f'\nYour new user ID is: {green(user_id)}\n'
        )
    text = (
        'Please keep this safe as this is how you can retrieve your progress.'
    )
    print(f'{pink("Important:")} {text}')
    return user_id


def show_credits():
    '''
    Display credits on screen
    '''
    clear_terminal()
    print(constants.CREDITS)
    print_press_enter_to("Press Enter to return to main menu...")
    main_menu()


def validate_input(value, max_value):
    '''
    Inside the try, converts input string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if outside the expected range.
    '''
    try:
        try:
            int_value = int(value)
        except TypeError:
            print_error_message("Invalid input.")
            return False
        if int_value >= 0 and int_value <= int(max_value):
            return True
        raise ValueError()
    except ValueError:
        print_error_message("Invalid input.")
        return False
    return True


def validate_yes_no(value):
    '''
    Checks to make sure user typed expected response.
    Acceptable ['y','ye','yes','n','no'], return True
    Else return False.
    '''
    if value.lower() in ['y', 'ye', 'yes', 'n', 'no']:
        return True

    print_error_message("Invalid input.")
    return False


def print_portions_in_stock(stats):
    '''
    Print how many portions from ingridants player currently has
    '''
    text = cyan("Your current stock:")
    print(f'{text}')
    print('------------------------------------')
    print(f'{stats["bun"]} x Hotdog bun(s)')
    print(f'{stats["sausage"]} x Hotdog sausage(s)')
    print(f'{stats["onion"]} x Onion(s)')
    print(f'{stats["sauce"]} x Special sauce(s)')


def main():
    '''
    Main functions to run once code has loaded
    '''
    main_menu()


# Setting default text color
print(cyan(''))
main()
