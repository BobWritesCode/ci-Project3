[<< Back to main ReadMe](README.md)

# Manual Application Testing

Below is reasonable test I could imagine to check every validation and all results came back as expected.

<table>
  <tr>
    <th>What is being tested</th>
    <th>How</th>
    <th>Expected Response</th>
    <th>Actual Response</th>
    <th>Outcome</th>
  </tr>
  <tr>
    <td>Run program</td>
    <td>n/a</td>
    <td>Loads main menu</td>
    <td>Program runs and loads main menu</td>
    <td>PASS</td>
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

[<< Back to ReadMe](README.md)