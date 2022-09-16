# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize (SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hotdog_Tycoon_Data')
GAMETITLE = 'Hotdog Tycoon' #Name change pending


def get_leaderboard_data():
    '''
    Gets leaderbaord data from Google sheet
    '''
    highscore = SHEET.worksheet('leaderboard')
    data = highscore.get_all_values()
    print('\n************************************')
    print('Top 10 Highscores for classic mode')
    print('************************************\n')
    print(f"{data[0][0]:<30}{data[0][1]:<40}")
    print('------------------------------------')
    for x in data[1:10]:
      print(f"{x[0]:<30}{x[1]:<40}")



def main():
    '''
    Main functions to run once code has loaded
    '''
    get_leaderboard_data()


print(f'Preparing to start {GAMETITLE}.')
main()