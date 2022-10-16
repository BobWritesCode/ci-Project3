'''
Shared functions
'''
from math import floor
import constants


def cost_to_make(stats):
    '''
    Works out the cost of making each hotdog
    '''
    bun = (
        stats['recipe']['bun'] *
        constants.STOCK_COSTS['bun'][2] /
        constants.STOCK_COSTS['bun'][1]
    )

    sausage = (
        stats['recipe']['sausage'] *
        constants.STOCK_COSTS['sausage'][2] /
        constants.STOCK_COSTS['sausage'][1]
    )

    onion = (
        stats['recipe']['onion'] *
        constants.STOCK_COSTS['onion'][2] /
        constants.STOCK_COSTS['onion'][1]
    )

    sauce = (
        stats['recipe']['sauce'] *
        constants.STOCK_COSTS['sauce'][2] /
        constants.STOCK_COSTS['sauce'][1]
    )

    return floor((bun + sausage + onion + sauce) * 100) / 100


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
