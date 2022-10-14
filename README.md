# Hotdog Empire Tycoon


![Game Preview](./readme-content/imgs/preview.png)

## Live Site

[Hotdog Empire Tycoon](
  https://dashboard.heroku.com/apps/hotdog-empire-tycoon/)

## Repository

[https://github.com/BobWritesCode/ci-Project3](
  https://github.com/BobWritesCode/ci-Project3)

---

## Table of Contents

- [Hotdog Empire Tycoon](#hotdog-empire-tycoon)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
    - [Hotdog Empire Tycoon](#hotdog-empire-tycoon-1)
  - [UX &#8722; User Experience Design](#ux--user-experience-design)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Interested Party](#interested-party)
    - [Initial Concept](#initial-concept)
      - [Wireframes](#wireframes)
        - [Desktop](#desktop)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Logic](#logic)
    - [Initial Flow](#initial-flow)
    - [Python Logic](#python-logic)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [UX](#ux))
    - [Features Left to Implement](#features-left-to-implement)
  - [Data Model](#data-model)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [Other Tech](#other-tech)
      - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
    - [Python Testing](#python-testing)
      - [Manual Python Testing](#manual-python-testing)
        - [Manual Testing Documentation](#manual-testing-documentation)
      - [PEP8 Testing](#pep8-testing)
      - [Other Python Testing](#other-python-testing)
    - [W3C Validator](#w3c-validator)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
    - [GitHub](#github)
    - [GitPod](#gitpod)
      - [Cloning](#cloning)
      - [Editing](#editing)
    - [Working With Python](#working-with-python)
      - [Packages](#packages)
      - [Debugging](#debugging)
    - [Google Sheets](#google-sheets)
      - [Creating Sheets](#creating-sheets)
      - [API Credentials](#api-credentials)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---

## Objective

Design an interactive game that uses an existing API for to save user game data and a leaderboard.
The project should run in a CLI, deployed via Heroku, using Python.

***The needs within this project are not genuine and are made purely
for the purpose of completing this project.***

---

## Brief

### Hotdog Empire Tycoon

The goal of this site is to provide an interactive game where the user / player can compete for a place on the leaderboard. The final product should:

- be programmatically error free,
- be written using Python,
- have replayability,
- handle all user input errors gracefully and appropriately,
- give clear instructions regarding use and valid inputs.
---

## UX &#8722; User Experience Design

Some example user stories which will affect the design

#### First Time User

> *"As a person who like likes to play games, I would like something that provides some challenges but not overly difficult to learn."*
>
> *"As a competitive player, I would like to know how I compare with other users and go for top of a leaderboard."*
>
> *"As someone unfamiliar with tycoon game concept, I would like something that is to pick up and provides adequate direction."*

### Returning User

> *"As a returning user, I would like to see a list of current high-scores."*
>
> *"I would like to be able to continue a game where I left off."*
>
> *"I would the experience to be different each time I play."*

#### Interested Party

> *"As someone interested in how the application has been made, I am interested to see how user inputs have been validated and errors have been handled"*
>
>*"As someone interested in how the application wasm, I am interested to see any interesting code you made have used or created."*

---

### Initial Concept

I intend to make a game application inspired by a childhood memory of Lemonade stand. The version I played was a flash game but learnt from starting this project that it all started with the [original created by Bob Jamison](https://en.wikipedia.org/wiki/Lemonade_Stand).

I intend to:
- use an API to store user game data, which the user can also use to retrieve a previous game they have not completed yet.
- use an API to store a leaderboard, which users will be able to view.
- write error proof logic.
- a fun and interesting game.

I do not intend:
- to store any user sensitive information using the API.

#### Wireframes

Due to the nature of this project the wireframes are very basic. There is only
one page and the design does not change across any devices, only a change in
content.

##### Desktop

![Wireframe](./readme-content/imgs/wireframe.png)

---

#### Colour Scheme

I wanted to go for a vibrant eye-catching look. I also tried to keep to a colour theme as much as possible and not use too many colours.

- Cyan - Used mainly for headers.
- Pink - Used mainly for user tips.
- Orange - Used mainly for when user input was required.
- Red - Used mainly for errors and grabbing user attention.
- Yellow - Used mainly to highlight '0. Go Back' to the user
- Gold - Used mainly to highlight positive information to the user.
- Green - Used mainly for cash balance and some areas to help separate information from each other.

To create the different colour text in the game I used code found of [Grepper](https://www.codegrepper.com/code-examples/python/how+to+color+text+in+python+3).

```python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
```

I then created specific colour functions to have better readability, keep colours uniformed and make it quicker to add coloured text.

```python
def pink(text):
    '''
    Changes to PINK if printed to terminal
    '''
    return colored(255, 105, 180, text)
```

---

#### Typography

I do not use any external font outside the terminal except for the button provided by Code Institute to 'RUN PROGRAM'

---

#### Imagery

There is no imagery used for this project.

---

## Logic

### Initial Flow

This chart shows what the user will experience / see and is the concept of how the game will run

![Flowchart for frontend](./readme-content/imgs/flowchart-frontend.png)

---

### Python Logic

![Flowchart for backend](./readme-content/imgs/flowchart-backend.png)

---

## Features

### Existing Features

**Main Menu**

The main menu is the first screen a user will see, and give them 4 options to pink from:
- New game
- Load game
- View leaderboard 
- Credits

![Main Menu](./readme-content/imgs/main-menu.png)

---
- **Setting up a new Game**

The user will need to provide a new name for their new hotdog empire. This must be from 5 and up to 20 characters.

```python
if len(user_name) < 5 or length > 20:
    print_error_message("Company name must be least 5 and no more "
                        + "than 20 characters")
    continue
```

After a game ID will be created and given to the player. This game ID is important as it will be how the user can retrieve their game save.

```python
while True:
    user_id = "".join(
        string.ascii_uppercase[random.randrange(0, 25)] for x in range(6)
        )
    user_data = SHEET.worksheet('user_data')
    cell_list = user_data.findall(user_id)
    if len(cell_list) == 0:
        break
```
After this the user will be given a short back story that is pulled from `constants.py`

---
**Game Menu**

The game menu is the main screen a user will interact with while playing the game. The user menu gives the player 9 options to pick from, including:
- Purchase location
- Purchase / upgrade cart(s)
- Hire / upgrade staff
- Purchase stock
- Change recipe
- Set selling prices
- Start trading
- Help
- Save and quit

This menu also provides valuable information to the player, so they don't have to unnecessarily go in and out of menu options to get this information.

![Game menu](./readme-content/imgs/preview.png)

---
- **Purchase locations**

Here the user can purchase locations they to sell at. Logic is in place so the user has to purchase each location in order.

```python
if (not stats['location'][str(user_choice)]['purchased']
        and purchase_loc_try(stats, int(user_choice))):
    remaining_cash = stats["cash"] - loc_cost[int(user_choice)-1]
elif not purchase_loc_try(stats, int(user_choice)):
    print_error_message('Can not make this purchase yet.')
    continue
else:
    print_error_message('Already Purchased.')
    continue
```

![Purchase locations menu](./readme-content/imgs/purchase-locations.png)

---
- **Purchase / upgrade carts**

Within this screen the user can purchase and upgrade carts. Logic is in place so the user can only purchase carts that they have already purchased the location for.

```python
# Make sure location has been purchased first.
if not stats['location'][str(result)]['purchased']:
    print_error_message("Purchase Land")
    continue

# Check if cart is not already at max level.
cart_level = stats['location'][str(result)]['cart_lvl']
if cart_level == 5:
    print_error_message("Already at max level.")
    continue
```

![Purchase / upgrade carts menu](./readme-content/imgs/purchase-carts.png)

---
- **Hire / train staff**

This screen is very similar to purchase / upgrade carts with the same logic to check which options can be purchases and are currently upgradable.

![Hire / train staff menu](./readme-content/imgs/hire-staff.png)

---
- **Purchase stock**

The purchase stock screen has 2 stages. Firstly the main screen which shows the user information like how many ingredients they have in stock and how many products that makes based on their current recipe. At this stage the user can currently choose how many products they wish to have in stock ready to sell. If they input a number before the current stock level, logic will work out the amount of products need to be purchased and then show the user a checkout screen.

```python
def get_portions_available(stats):
    '''
    Return how many portions of hotdogs are available to sell
    based on current stock and recipe.
    '''
    # Max portions that can be sold in 1 part of the day
    max_por = 9999999
    # Find out which ingredient makes the least amount of hotdogs based
    # on recipe.
    for key in constants.STOCK_OPTIONS:
        if stats["recipe"][key] > 0:
            # How many hotdogs this ingredient will make
            ing_max = stats[key] / stats["recipe"][key]
            # Next, see if ing_max is smallest out of all ingredient, meaning
            # max hotdogs
            max_por = ing_max if ing_max < max_por else max_por

    return floor(max_por)
```

![Purchase stock menu](./readme-content/imgs/purchase-stock.png)

```python
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
```

![Purchase stock checkout](./readme-content/imgs/checkout.png)

---
- **Change recipe**

Within this screen the user can change how many ingredients are used to make each hotdog. It also displays the cost to make each hotdog based on recipe and current recommended retail price (RRP) (cost to make * 3 + 0.5). 

![Change recipe](./readme-content/imgs/change-recipe.png)

---
- **Set selling price**

This is simplest screen in the game. It quite simply allows the user to change the selling price of the product.

![Set selling price screen](./readme-content/imgs/set-selling-price.png)

---
- **Help section**

To assist the user to understand how to play the game, I have provided this help section. Due to the large blocks of text I have stored them in `constant.py` to avoid blocking up the code in `game_menu.py`.

```python
# Part of help text from constants.py
HELP_SCREEN1 = f"""{cyan('Help:')}
{LINE}
{gold('Main Objective:')} Your main objective is to collect as much wealth
before the final day. At the end your wealth will determine your score.

{pink('Day cycle:')} Every day has 2 parts, morning and afternoon. The
morning starts at 8am and finishes at 12noon, you can do purchases in the
morning and afternoon. The afternoon is from 12noon to 5pm. The afternoon
is slightly longer.
```

![Help screen](./readme-content/imgs/help-screen.png)

---
- **Save and quit** and,
- **Auto save**

The game features a save functionality. The user can choose to save at the game menu or the game automatically save at the end each trading cycle, as well as one last time when the game is completed.

There were a couple obstacles to overcome with the save function. 

1) When saving using `gspread` it does not accept data in a dictionary format. So I had to convert a dictionary to a list. When searching for a solution I was unable myself to come across one. I had to write the code myself. I was able to do this with the solution below.\
\
Simply it takes the dictionary and goes through it key by key appending a blank table.\
\
If the next entry is a dictionary within the dictionary it sends that through a new thread of the function. And repeats that unto it reaches a non dictionary key.\
\
It then returns to the original thread and moves on to the next key.\
\
This repeated until the dictionary has been fully completed.

```python
def convert_dict_to_array(data, data_to_save):
    '''
    Convert dict game data to an array so it can be saved to Google Sheet
    '''
    for key in data:
        if isinstance(data[f'{key}'], dict):
            # If key is a dict then loop function
            convert_dict_to_array(data[f'{key}'], data_to_save)
        else:
            # If key is not a dict then append to table.
            data_to_save.append([data[f"{key}"]])

    return data_to_save
```

2) When saving to a worksheet using `gspread`, saving to a row you can just use a number. But saving to a column you have to use letter notation. I was going to write the code myself but then thought there is a chance someone else has already done this and I can find the code online, which I did.\
\
CREDIT : https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter

```python
def save_loop(col, data, worksheet):
    '''
    Saves data[] to the correct row in Google.
    '''
    # Converts column number into letter notation used in spreadsheets
    # for columns. Example: 26 = Z, 27 = AA, 28 = AB...
    column_int = int(col)
    start_index = 1
    letter = ''
    while column_int > 25 + start_index:
        letter += chr(65 + int((column_int-start_index)/26) - 1)
        column_int = column_int - (int((column_int-start_index)/26))*26
    letter += chr(65 - start_index + (int(column_int)))

    # Creates string for cell notation for spreadsheet.
    s_col = f'user_data!{letter}1'

    # Saves data to worksheet
    SHEET.values_update(s_col,
                        params={'valueInputOption': 'RAW'},
                        body={'values': data})

    return True
```

---
- **Retrieve game**

As the game allows the user to save their game and provides then a Game ID. The user is able to retrieve their game providing it has not already been completed.

```python
# Cycle through row values until Game ID finds a match.
for count, key in enumerate(row_array):
    if key != user_input:
        continue

    # Copy data from column where Game ID found match.
    data = worksheet.col_values(count + 1)

    # Run function set_up_character()
    # Converts data retrieved from worksheet into data format
    # game uses.
    stats = set_up_character(data, False)
```

![Retrieve Game](./readme-content/imgs/retrieve-game.png)

---
- **End Game Summary**

After the user has completed the game they are given a end game summary, as well as seeing if the made the leaderboard.

![End game summary](./readme-content/imgs/end-screen.png)

---
- **Being added to leaderboard**

At the end of the game. Logic will check to see if the player's score has made the top 10 of the leaderboard. If so add player into list where they have placed and remove the bottom player. Then save new leaderboard to the database.

```python
# Get current leaderboard information from Google worksheet.
highscore = SHEET.worksheet('leaderboard')
data = highscore.get_all_values()

# Go through current leaderboard entries and see if placed
# higher than any of the current entries.
for count, key in enumerate(data[1:10], 2):

    # Player has placed higher then a player.
    if stats["cash"] > float(key[1]):
        print(f"\n{green('CONGRATULATIONS!!!')}")
        print(f'You placed number {gold(count - 1)} on our '
              + 'leaderboard!\n')

        # Insert data of player into correct place
        data.insert(count - 1, [stats["name"], stats["cash"]])

        # Remove data for player who is no in 11th place.
        data.pop()

        # Update Google worksheet
        SHEET.values_update(
            'leaderboard!A1',
            params={'valueInputOption': 'RAW'},
            body={'values': data}
              )
```

![Making leaderboard](./readme-content/imgs/make-leaderboard.png)

---
- **View leaderboard**

Allows users to see leaderboard and provide a goal to aim for while playing the game. The scores are saved to a Google worksheet.

```python
# Get highscores from Google worksheet
highscore = SHEET.worksheet('leaderboard')
data = highscore.get_all_values()

# Header
print(f'{yellow("************************************")}')
print(f'{cyan("Top 10 highscores for classic mode")}')
print(f'{yellow("************************************")}\n')

# Show table headings
print(f"{data[0][0]:<20}{ data[0][1]:<20}")
print(constants.LINE)

# Show top 10 with scores
for key in data[1:10]:
    print(f"{key[0]:<20}{'£ ' +'{:.2f}'.format(float(key[1])):<20}")
```

![Leaderboard](./readme-content/imgs/view-leaderboard.png)

---
- **View credits**

To pay homage to the original creator of the game that inspired this project and to also to the people who tested this game. I created a credits screen where I could show my appreciation.

![Credits](./readme-content/imgs/credits.png)

---
- **Sales Report**

At the end of each trading session the user will get a report to show how well the day went. It nicely separates each locations performance, showing units sold and total net profit.

```python
  # Add up total values from different locations.
  total_sale_value = 0
  for i in data[3]:
      total_sale_value += i

  # Show sales report to user. Location, units sold, net profit.
  print(constants.LINE)
  print(f'{"Location":<13}{"-":<3}{"Units":<8}{"-":<3}{"Value (£)":<8}')
  print(constants.LINE)

  for count, key in enumerate(data[0]):
      print(f'{data[2][count]:<13}{"-":<3}'
            + f'{key:<8}{"-":<3}'
            + f'{floor(data[3][count]*100)/100:<8}')

  print(constants.LINE)
  
  # Totals
  print(f'Total daily units sold: {green(data[1])}')
  text = green(f'£{floor(total_sale_value*100)/100}')
  print(f'Total daily sales value: {text} (var +/- £0.01)')
  print('\nSales values are net profit (Sold price minus product cost).')
```

![Sales Report](./readme-content/imgs/sales-report.png)

---
- **Feedback**

Based on the selling price and amount of ingredients used (to create value). Customers may think that the product is overpriced and decline to purchase. This section will let the user know, and if there is too much negative feedback for the user's liking they can make adjustments to their price and / or ingredients.

```python
# ((User selling price - optimal) / max increase) * 100
# less then X, customer will purchase. 
# Otherwise customer decline as overpriced.
max_markup = constants.MAX_PRICE_OVER_OPTIMAL
if goto_1 and (((price - osp) / max_markup)
                * 100 < randrange(100)):
    will_buy = True
elif goto_1:
    feedback["cost"][key] += 1
    rep_score -= 1
```

![Feedback](./readme-content/imgs/feedback.png)

---
- **Reputation**

If the user has a day with little negative feedback vs sales made. Then their reputation will increase. If it's a bad day the reputation will decrease. Reputation provides bonuses to footfall, value and sales price.

```python
# If good score, increase reputation providing not already at max
if rep_percent > 0.5 and c_rep < 5:
    stats["reputation"] += 0.5
    print(
        f"{green('Reputation increase:')}\
            {gold('+ 0.5')}"
        )
elif rep_percent > 0.5 and c_rep == 5:
    print(gold("Reputation already at a 5!"))
```

![Reputation](./readme-content/imgs/reputation.png)

---
- **Seamless transition back to menu**\
*(No random termination of program)*

It was very important to me that the user didn't reach the end of a function and the program just terminate. I spent time to make sure that as each function ended, it either had a `return` or I knew where it would go back to. An example of this is after the user completes the game. 

Once `end_game()` is completed it returns to `daily_menu()` then to either:
- `background_story()` > `new_game()` > `main_menu()`
- or straight to `main_menu()` if it was a previous game loaded. 

And `main_menu()` is in never ever `while True:` loop.

---
- **Continuous validation** and,
-  **Error Handling**

There are several areas within the game the user is required to p
input a string. Examples are: Choosing a name, navigating the menus, making changes to recipe.\
To make sure that there are no unexpected errors there are validation checks being done after the user provides their inputs and feeds back to the user if an error is detected.

```python
# Example of validation check when user is navigating the menus.
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
```

```python
    # Example of validation check when user is changing recipe

    # Get user input to change recipe
    result = input(f'\n{orange("Enter change i.e. 3 4: ")}')
    # Split string into a list
    result = result.split()

    # Validate user input
    if not validate_recipe_change(result):
        continue

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
```

![Error handling](./readme-content/imgs/error-handling.png)

---

### Features Left to Implement

- Random Events

Part of my original plan I wanted to implement random events that could happen during trading. Example: Random hygiene inspection, or, influencer visits. And these events would have positive or negative results for sales performance that day.

- Different day challenged (short version of 5 days)

One of the testers mentioned she felt the game was a little too long. 

> *"This is amazing I haven't seen anything like it! My only issues is its a little long, so I’m getting impatient to reach the end! Such a great one!"*

This has given me the idea to implement a 5-day challenge for people who want to a quick blitz are the game.

---

## Data Model

A Google Sheet was used to store users game data. No sensitive data is store in the Google Sheet. The sheets consists of two worksheets, 'leaderboard' and 'user_data'.

![Google Worksheet](./readme-content/imgs/google-worksheet.png)

---

## Technologies Used

### Python Packages

- `ascii_uppercase` from [string](https://docs.python.org/3/library/string.html): Used to create game id for user of 6 uppercase letters.

- [gspread](https://docs.gspread.org/en/latest/): Allows communication with Google Sheets.

- `floor` from [math](https://docs.python.org/3/library/math.html): Rounds down a float to an integer.

- `ceil` from [math](https://docs.python.org/3/library/math.html): Rounds up a float to an integer.

- `randrange` from [random](https://docs.python.org/3/library/random.html): Returns a random integer within a given range.

- `system` and `name` from [os](https://docs.python.org/3/library/os.html): Allows to clear the terminal.

---

### VS Code extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

- [Beautify](https://open-vsx.gitpod.io/extension/HookyQR/beautify)

- [Auto Close Tag](https://open-vsx.gitpod.io/extension/formulahendry/auto-close-tag)

---
### Other Tech

- [Online Spellcheck](https://www.online-spellcheck.com/): To check spelling.

- [Balsamiq](https://balsamiq.com/wireframes/): To create wireframe.

- [Draw.io](https://app.diagrams.net/): To create flowcharts.

- [ShareX](https://getsharex.com/): Used to snip screenshots.

- [GitPod](https://gitpod.io/): Used as workspace and code editor.

- [Heroku](https://www.heroku.com/): Used to deploy project for live use.

- [Google Worksheet](https://www.google.co.uk/sheets/about/): Used as database.

---

## Testing

### Testers

Prior to this final testing. I asked others to try out the game and see what errors they could find. Most reported everything ran smoothly and there were no unexpected errors but some formatting in places seemed off. All testers have been included within the Credits of the game and below in the credits section on this ReadMe.

> *"Hi. Just played your game 4 times, it's kinda addictive, unfortunately, it crashed once, and once the game did not save when accidentally going back into the menu. I'm not sure about the customer reviews and the formatting. I have attached a screenshot of the issue. My husband and I just spent over an hour playing this, so I would definitely say it's a job well done Wish you all the best!"*

![Feedback error](./readme-content/testing/feedback-error.png)

- I as unable to replicated the error of not saving when going back to main menu. If it was an error it seems to now be fixed.
- I have fixed this so lines do not appear when a location does not have any feedback to show. [commit: 528da9a](https://github.com/BobWritesCode/ci-Project3/commit/528da9a3b20c670ba178267e174cdeb28089011b)

> *"This is amazing I haven't seen anything like it! My only issues is it's a little long, so I’m getting impatient to reach the end! Such a great one!"*

- I have suggested in my future ideas to implement, to include a shorter 5 day version of the game instead of the current 10.

> *"This is absolutely fantastic! What a project, I love it.
I got through the entire game, didn’t encounter any errors but did find a few typos I’ll add screen shots (so easy fixes). This is a colossal effort sir, well done indeed I made it to 4 on the leaderboard too."*

- Typos were corrected. They were mainly caused by strings that forced a line of code to be longer then 78 characters. And when I then split the line of code into two lines, I forgot to take into account and include a space.

```python
# Example of before - WRONG!
# No space after long
print('This is meant to be a very long'
      + 'string I need to split across two lines')

'Output: the words long string would be joined as 1: longstring'

# Example of after - CORRECT!
# Space included after long
print('This is meant to be a very long '
      + 'string I need to split across two lines')

'Output: the words long string would be separate: long string'
```

> *"It's so nice and slick and the user interface is epic. I don't have too much feedback other than it works perfectly! I didn't find it immediately obvious that the amount of ingredients being bought was the total amount (I thought that it was additional ingredients), but this is clearly user error and nothing wrong with the game. It could be worth making this a little more obvious to people like me who didn't quite get it, but that's just quality of life stuff/ dummy proofing. You should be really proud, your effort has totally paid off!"*

- Taking this feedback on board, I changed the purchase stock screen to try and make it more obvious what was actually happening. [commit: 5725551](https://github.com/BobWritesCode/ci-Project3/commit/5725551feec0405289676eadb18051c45e424841)

### Python Testing

#### Manual Python Testing

<table>
  <tr>
    <th>What is being tested</th>
    <th>How</th>
    <th>Expected Response</th>
    <th>Actual Response</th>
    <th>Fix</th>
  </tr>
  <tr>
    <td>Run program</td>
    <td>n/a</td>
    <td>Loads main menu</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "0"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "1"</td>
    <td>Takes you to new game</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "2"</td>
    <td>Takes you to retrieve game</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "3"</td>
    <td>Takes you to leaderboard</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>Input "4"</td>
    <td>Takes you to credits</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Credits</td>
    <td>Hit enter when prompted</td>
    <td>Takes you back to main menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Leaderboard</td>
    <td>Hit enter when prompted</td>
    <td>Takes you back to main menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game</td>
    <td>Input : "Bobs"</td>
    <td>Error message and then loop back</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game</td>
    <td>Input : "String over 20 characters"</td>
    <td>Error message and then loop back</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Name</td>
    <td>Input : "Bobs Dogs"</td>
    <td>Asks if you are happy with this name</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "0"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "N"</td>
    <td>Loops back to input new name.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "No"</td>
    <td>Loops back to input new name.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "Y"</td>
    <td>Takes you to Game ID.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "yE"</td>
    <td>Takes you to Game ID.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>New Game - Confirm Name</td>
    <td>Input "YeS"</td>
    <td>Takes you to Game ID.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game ID</td>
    <td>A random 6 letter combination should be shown</td>
    <td>Ask user to hit enter.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game ID</td>
    <td>Hit enter when prompted.</td>
    <td>Takes you to backstory.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Backstory</td>
    <td>Hit enter when prompted</td>
    <td>Takes you to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Cash should be 500</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Day should be 0 out of 10</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Time of day should be 'Morning'</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Reputation should be 0 / 5</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Stock should be 0</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu - Stats</td>
    <td>Selling price should be 2.50</td>
    <td>As described.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "1"</td>
    <td>Takes you to location purchase</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "2"</td>
    <td>Takes you to cart purchase</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "3"</td>
    <td>Takes you hire staff</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "4"</td>
    <td>Takes you stock purchase</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "5"</td>
    <td>Takes you stock change recipe</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "6"</td>
    <td>Takes you to set selling price</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Do not purchase any location, any cart, hire any staff, or purchase any stock then input 7.</td>
    <td>Error message saying no location purchased</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Purchase location but do not purchase cart or hire staff member or purchase any stock then input 7.</td>
    <td>Error message saying no cart purchased</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Purchase location, cart, but do not hire staff member and do not buy any stock then input 7.</td>
    <td>Error message saying no staff member hired</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Purchase location, cart, hire staff member and do not buy any stock then input 7.</td>
    <td>Error message saying no stock to sell</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Purchase location, cart, hire staff member and buy any stock then input 7.</td>
    <td>Moves on to sales report</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "8"</td>
    <td>Take you to Help Screen</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Game Menu</td>
    <td>Input "0"</td>
    <td>Saves, and takes you to main menu</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>On first time visit. </td>
    <td>Location 1 should show available to be purchased, other 4 should be unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Before purchase location 1. Input '2'</td>
    <td>Error message. No money changes. Cart and staff for location do not become available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Before purchase location 1. Input '3'</td>
    <td>Error message. No money changes. Cart and staff for location do not become available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Before purchase location 1. Input '4'</td>
    <td>Error message. No money changes. Cart and staff for location do not become available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Before purchase location 1. Input '5'</td>
    <td>Error message. No money changes. Cart and staff for location do not become available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Purchase location 1</td>
    <td>Success message. Next location becomes available. Money changes correctly. Cart and staff for location available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Purchase location 2</td>
    <td>Success message. Next location becomes available. Money changes correctly. Cart and staff for location available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Purchase location 3</td>
    <td>Success message. Next location becomes available. Money changes correctly. Cart and staff for location available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Purchase location 4</td>
    <td>Success message. Next location becomes available. Money changes correctly. Cart and staff for location available.</td>
    <td></td>
    <td></td>
  </tr>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Purchase location 5</td>
    <td>Success message. Next location becomes available. Money changes correctly. Cart and staff for location available.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Try purchase a location when money is below required amount</td>
    <td>Error message. Location not purchase. Money not changed.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Try to purchase a location already purchased</td>
    <td>Error message. Money does not change.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase location</td>
    <td>Input 0</td>
    <td>Takes you back to game</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check.</td>
    <td>All carts should be unavailable</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check. Input '1'.</td>
    <td>Error message. No money changes. Cart stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check. Input '2'.</td>
    <td>Error message. No money changes. Cart stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check. Input '3'.</td>
    <td>Error message. No money changes. Cart stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check. Input '4'.</td>
    <td>Error message. No money changes. Cart stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Prior to any location purchase, check. Input '5'.</td>
    <td>Error message. No money changes. Cart stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 1 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 1 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 1 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 2 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 2 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 2 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 3 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 3 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 3 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 3 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 3 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 3 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 4 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 4 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 4 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>After location 5 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. Cart shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Upgrade cart 5 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. Cart shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to upgrade cart 5 pass level 5.</td>
    <td>Error message. No money changes. Cart stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Try to purchase a cart or upgrade when do not have enough cash to cover the cost.</td>
    <td>Error message, no cash change, cart is not purchased / upgraded.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Purchase Cart</td>
    <td>Input "0"</td>
    <td>Takes user back to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check.</td>
    <td>All staff should be unavailable</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check. Input '1'.</td>
    <td>Error message. No money changes. staff stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check. Input '2'.</td>
    <td>Error message. No money changes. staff stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check. Input '3'.</td>
    <td>Error message. No money changes. staff stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check. Input '4'.</td>
    <td>Error message. No money changes. staff stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Prior to any location purchase, check. Input '5'.</td>
    <td>Error message. No money changes. staff stays unavailable.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 1 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 1 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 1 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 2 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 2 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 2 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 3 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 3 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 3 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 3 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 3 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 3 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 4 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 4 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 4 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>After location 5 purchased. Input '1'.</td>
    <td>Purchase success. Money deducted as shown. staff shows as level 1.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Upgrade staff 5 to level 5.</td>
    <td>Purchase success each time. Money deducted as shown each time. staff shows as level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to upgrade staff 5 pass level 5.</td>
    <td>Error message. No money changes. staff stays at level 5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Try to purchase a staff or upgrade when do not have enough cash to cover the cost.</td>
    <td>Error message, no cash change, staff is not purchased / upgraded.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Input "1 2"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Hire Staff</td>
    <td>Input "0"</td>
    <td>Takes user back to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>On first visit</td>
    <td>All stock levels should show as 0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>Input "sda"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>Input "-6"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>Input "2 4"</td>
    <td>Error message and loops back.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>Input "0"</td>
    <td>Takes user back to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>With 0 stock, input "50"</td>
    <td>Move to check out.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>With 0 stock currently, recipe as 1 bun, 1 sausage, 2 onion, 1 sauce, and '50' input on purchase stock. Checkout should show. </td>
    <td>Checkout basket should be: 9 packs of buns, 7 packs of sausages, 10 onions, 3 jars of sauce. Sub totals of: £9, £14, £10, £15. Grand total of £48 </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "sda"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "-6"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "2 4"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "0"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Purchase basket from previous test</td>
    <td>Purchase success, and stock on purchase screen should update based on checkout quantities. Money should lower based on grand total.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>With 50 stock, input "40".</td>
    <td>Error message. Loop back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>With 50 stock, input "60".</td>
    <td>Moves to checkout.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>With 50 stock currently, recipe as 1 bun, 1 sausage, 2 onion, 1 sauce, and '60' input on purchase stock. Checkout should show. </td>
    <td>Checkout basket should be: 1 packs of buns, 1 packs of sausages, 1 onion, 0 jars of sauce. Sub totals of: £0, £0, £0, £5. Grand total of £5 </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Purchase basket from previous test</td>
    <td>Purchase success, and stock on purchase screen should update based on checkout quantities. Money should lower based on grand total.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase</td>
    <td>With 60 stock, input "2000". With not enough cash to cover the cost. </td>
    <td>Moves to checkout.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>With 60 stock, and 2000 input prior. And with not enough cash to cover the cost. </td>
    <td>Error message and loop back to stock purchase.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "N"</td>
    <td>Aborts purchase and takes you back to stock purchase</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "No"</td>
    <td>Aborts purchase and takes you back to stock purchase</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "Y"</td>
    <td>Commits purchase and takes you back to stock purchase.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "yE"</td>
    <td>Commits purchase and takes you back to stock purchase.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Stock Purchase - Checkout</td>
    <td>Input "YeS"</td>
    <td>Commits purchase and takes you back to stock purchase.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>On first visit</td>
    <td>Default values should be: 1 Bun, 1 Sausage, 2 Onion, 1 Sauce. Cost to make £0.87. Recommend retail price £3.10</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "sda"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "67.9"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "-6"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "3"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "0"</td>
    <td>Take you back to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "1 1"</td>
    <td>Success message, but recipe does not change as buns already on 1. No change to cost to make, and recommended retail cost.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "1 2"</td>
    <td>Error Message as over max for buns</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "1 0"</td>
    <td>Error Message as under min for buns</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "2 2"</td>
    <td>Success message, recipe changes sausages to 2. Cost to make and recommended retail cost also changes.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "2 3"</td>
    <td>Error Message as over max for sausages</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "2 0"</td>
    <td>Error Message as under min for sausages</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "3 1"</td>
    <td>Success message, recipe changes onions to 1. Cost to make and recommended retail cost also changes.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "3 6"</td>
    <td>Error Message as over max for onions</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "3 0"</td>
    <td>Error Message as under min for onions</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "4 2"</td>
    <td>Success message, recipe changes sauce to 2. Cost to make and recommended retail cost also changes.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "4 6"</td>
    <td>Error Message as over max for sauce</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Change Recipe</td>
    <td>Input "4 0"</td>
    <td>Error Message as under min for sauce</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>On first visit</td>
    <td>Cost to make should match Change recipe. Set Selling price should be £2.50. Profit per serving should be Selling price minus cost to make.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>Input "sda"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>Input "67.9"</td>
    <td>Selling price should update to 67.90.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>Input "-6"</td>
    <td>Error message and loops back for input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>Input "3"</td>
    <td>Selling price should update to 3.00.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Set Selling Price</td>
    <td>Input "0"</td>
    <td>Take you back to game menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Help Screen</td>
    <td>User visits from game menu</td>
    <td>Displays help messages.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Help Screen</td>
    <td>UUser press enter when prompted on help screen.</td>
    <td>After showing all messages, user is taken back to game menu</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Save and Quit</td>
    <td>On entry</td>
    <td>Game will save and show user game ID then prompt to hit enter.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Save and Quit</td>
    <td>User hits enter when prompted</td>
    <td>User is taken back to main menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "sda"</td>
    <td>Error message loops back to input</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "67.943"</td>
    <td>Error message loops back to input</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "fkfk34"</td>
    <td>Error message loops back to input</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "djtufed"</td>
    <td>Error message loops back to input.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "ZZZZZZ"</td>
    <td>Search but Error as no game found</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input known game ID of uncompleted game</td>
    <td>Loads game and takes user to game menu</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Reload browser and Input same game ID of same game</td>
    <td>Loads same game and takes user to game menu</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a Save Game</td>
    <td>Input "0"</td>
    <td>Take you back to main menu.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Trading</td>
    <td>Purchase all 5 location, purchase level 1 cart and staff for all 5, have 500 hotdogs in stock to sell. Set selling price to 2.50. Leave Recipe as buns 1, sausages 1, onions 2, sauce 1. Profit per sale should be £1.63. Make sure reputation is 0.</td>
    <td>User is taken to Sales Report</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Sales report</td>
    <td>Set up as above.</td>
    <td>Units sold at each location should match total quantity sold</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Sales report</td>
    <td>Set up as above.</td>
    <td>Cash value sold at each location should match total cash sold</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Sales report</td>
    <td>User prompted to hit enter to continue.</td>
    <td>Feedback section is shown.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Feedback</td>
    <td>Set up as above</td>
    <td>Due to low cost there should be no negative feedback.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Feedback</td>
    <td>User prompted to hit enter to continue.</td>
    <td>Reputation section is shown.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>Set up as above.</td>
    <td>As no negative feedback and product sold at low price, reputation should go up by 0.5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>Get reputation to 5 and try to increase to 5.5.</td>
    <td>Message to say reputation already at max, so no change. No actual change to reputation.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Trading</td>
    <td>Purchase all 5 location, purchase level 1 cart and staff for all 5, have 500 hotdogs in stock to sell. Set selling price to 50.00. Leave Recipe as buns 1, sausages 1, onions 2, sauce 1. Make sure reputation is 1.</td>
    <td>User is taken to Sales Report</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Sales report</td>
    <td>Set up as above.</td>
    <td>Due to high price, 0 units should be sold.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Feedback</td>
    <td>Set up as above</td>
    <td>Due to extremely high cost there should be a lot of negative feedback.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>Set up as above.</td>
    <td>As no negative feedback and product sold at low price, reputation should go up by 0.5.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>Get reputation to 0 and try to decrease to -0.5.</td>
    <td>Message to say reputation already at min, so no change. No actual change to reputation.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>User prompted to hit enter. Make sure Morning trade.</td>
    <td>User should be taken to game menu, should be same day but Afternoon. Cash, stock, reputation should have changed as advised in the sales and reputation report.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>User prompted to hit enter. Make sure Afternoon trade. And not last day.</td>
    <td>User should be taken to game menu, should be next day and Morning. Cash, stock, reputation should have changed as advised in the sales and reputation report.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Reputation</td>
    <td>User prompted to hit enter. Make sure Afternoon trade. And last day.</td>
    <td>User should be taken to end game screen.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>End Game</td>
    <td>Make sure have less cash then 10th place on leaderboard</td>
    <td>User will be shown end game summary and informed did not make leaderboard.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>End Game</td>
    <td>User to press enter when advised.</td>
    <td>User taken to main menu.</td>
    <td></td>
  </tr>
  <tr>
    <td>End Game</td>
    <td>Make sure have more cash then at least 10th place on leaderboard.</td>
    <td>User will be shown end game summary and informed placed X on leaderboard.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Leaderboard</td>
    <td>After End Game summary and making leaderboard, check leaderboard.</td>
    <td>Should see self on leaderboard at placed informed at end game summary.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retrieve a save</td>
    <td>Try to load a save that has reached end game.</td>
    <td>Error message. Game does not load.</td>
    <td></td>
    <td></td>
  </tr>
</table>

---
#### PEP8 Testing

The standard of testing [PEP8 Online](http://www.pep8online.com/) is currently down. So as a alternative option have installed a extension within VS Code to flag any errors.

1) Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.

2) In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).

3) Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.

4) Select pycodestyle from the list.

5) PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

Any styling errors would show up as a warning or critical error.\
In the image below I have highlighted a red rectangle around the results. Left to right you have critical errors, warnings and info. We do not have to worry about the info flags.
- There are 0 critical errors.
- The 3 warnings as are shown relate to .gitpod.yml. These warnings are related to the template files from Code Institute and do not reflect my coding.

![PEP8 Results](./readme-content/testing/pep8-results.png)

---

## Bugs

### Current

I am unaware of any current unresolved bugs.

### Resolved

---

## Development

The site was made using [GitHub](#GitHub) and [GitPod](#GitPod)

### GitHub - Create new repository from template

[GitHub Website](https://github.com/)

Sign in to GitHub.

I used a template created by Code Institute that can be accessed [here](https://github.com/Code-Institute-Org/python-essentials-template) and is available for public use via the use this template button.

- Click '**Use this template**'.

![Use this template](./readme-content/deployment/use-this-template.png)

- A new page will load.

- Give your project a name, 

- Provide a short description,

- Decide if it will e available publicly or private,

- There is no need to to tick 'Include all branches',

- Click 'Create repository from template'.


![Create new repository](./readme-content/deployment/create-new-repo.png)

---

### GitHub - Cloning 

To clone using GitHib:

- Go to the project you wish to clone.

- Option 1:  If you have the [Google Chrome GitPod extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki), you can just click on the Green GitPod button 

- Option 2: Click the 'Code' button. This open options for you to clone your preferred way.

![Create new repository](./readme-content/deployment/cloning.png)

### Google Sheets

#### Creating Sheets

This application uses **Google Sheets** to store data.

Assuming you have a Google account and are signed in you can go straight to your [Google Sheets here](https://docs.google.com/spreadsheets/u/0/).

Once you are on your Google Sheets dashboard you click the Google plus sign in the bottom right to create a new spreadsheet.

![Google new spreadsheet button](./readme-content/deployment/google-new-spreadsheet.png)

Once opened you can rename it by where it says 'Untitled spreadsheet' top right. Just click and give a new name.

**IMPORTANT:** The name used must match the name called in the open() method.

```python
SHEET = GSPREAD_CLIENT.open('Hotdog_Tycoon_Data')
```

![Google untitled spreadsheet](./readme-content/deployment/google-untitled.png)

![Google titled spreadsheet](./readme-content/deployment/google-titled.png)

Now make sure you have two tabs called 'leaderboard' and 'user_data'.
At the bottom of the page you will see a plus sign, a stack of lines, and a single tab named "Sheet1"
- Click the plus sign to create a 2nd tab called "Sheet2"
- Rename each tab by double clicking on its current name and name them 'leaderboard' and 'user_data'.

![Google tabs 1](./readme-content/deployment/google-tabs-1.png)

![Google tabs 2](./readme-content/deployment/google-tabs-2.png)

![Google tabs named](./readme-content/deployment/google-tabs-named.png)

On the "leaderboard" tab in cells A1 and B1 input "Company" and "score"

![Google Cells](./readme-content/deployment/google-cells.png)

**NOTE:** Google Sheets data works differently to most python objects. The 'list' of columns and rows starts at an index of 1.

---
### API Credentials
To allow access from the project to Google Sheets, credentials must be generated and provided.

Navigate to the [Google Cloud Platform](https://console.cloud.google.com/)

Click 'Select a project', this may have an existing project name in place.

![API Select](./readme-content/deployment/api-select.png)

Click 'NEW PROJECT'.

![API ](./readme-content/deployment/api-new-project.png)

Give the project a name.

![API Name](./readme-content/deployment/api-name.png)

Click 'CREATE'.

![API Create](./readme-content/deployment/api-create.png)

From the project's dashboard, select 'APIs and services' and then 'Library'.

![API Library](./readme-content/deployment/api-library.png)

Search for, and enable, Google Drive API.

![API ](./readme-content/deployment/api-google-drive.png)

![API Search](./readme-content/deployment/api-enable.png)

Click 'CREATE CREDENTIALS'.

![API ](./readme-content/deployment/api-credentials.png)

Select 'Google Drive API' from the drop down list.

![](./readme-content/deployment/api-cred-type.png)

Select 'Application data' from the first set of radio buttons.

![API ](./readme-content/deployment/api-app-data.png)

Select 'No, I', not using them' from the second set of radio buttons.

![](./readme-content/deployment/api-engine.png)

Click 'DONE' and then enter a name and description for the service account details.

![](./readme-content/deployment/api-account-details.png)

Select a role of 'Editor' from the options available.

![API ](./readme-content/deployment/api-grant.png)

Click 'DONE' to create the service account.

Click on the service account on the credentials page.

![](./readme-content/deployment/api-cred-example.png)


Select 'KEYS' from the menu bar.

![](./readme-content/deployment/api-keys-menu.png)

Select 'Create new key' from the 'ADD KEY' menu.

![API ](./readme-content/deployment/api-create-key.png)

Select 'JSON' and click 'CREATE'.

![API ](./readme-content/deployment/api-json.png)


The JSON file will be downloaded to your computer.

Copy the contents into a creds.json file within the repository. 

**EXTREMELY IMPORTANT:** Make sure to add this file to the .gitignore file. And do not share the contents of this file publicly.

---

## Deployment

---
### Heroku

Navigate to your heroku dashboard

Click "New" and select "Create new app".

![](./readme-content/deployment/heoku-create-new-app.png)

Input a meaningful name for your app and choose the region best suited to your location.

![](./readme-content/deployment/heoku-app-name.png)

Select "Settings" from the tabs.

![](./readme-content/deployment/heoku-settings-tab.png)

Click "Reveal Config Vars".

![](./readme-content/deployment/heoku-config-vars.png)

Input PORT and 8000 as one config var and click add.

Input CREDS and the content of your Google Sheet API creds file as another config var and click add.

![](./readme-content/deployment/heoku-input-creds.png)

Click "Add buildpack".

![](./readme-content/deployment/heoku-add-build-pack.png)

Add "nodejs" and "python" from the list or search if necessary, remember to click save.

![](./readme-content/deployment/heoku-select-buildpacks.png)

Python must be the first buildpack. They can be dragged into the correct position if needed.

![](./readme-content/deployment/heoku-correct-order-buildpacks.png)

Select "Deploy" from the tabs.

![](./readme-content/deployment/heroku-deploy-tab.png)

Select "GitHub - Connect to GitHub" from deployment methods.

![](./readme-content/deployment/heoku-select-github.png)

Click "Connect to GitHub" in the created section.

![](./readme-content/deployment/heoku-connect-github.png)

Search for the GitHub repository by name.

Click to connect to the relevant repo.

![](./readme-content/deployment/heoku-search-repo.png)

Either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.

![](./readme-content/deployment/heoku-branch-deploy.png)

Click View to view the deployed site.\
*Note: It may take a moment to become available.*

![](./readme-content/deployment/heoku-view.png)

---

## Credits

### Content

### Media

### Acknowledgements

