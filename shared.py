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

    return bun + sausage + onion + sauce


def get_portions_avaliable(stats):
    '''
    Return how many portions of hotdogs are avaliable to sell
    based on current stock and recipe.
    '''
    # Max portions that can be sold in 1 part of the day
    max_por = 9999999
    for key in constants.STOCK_OPTIONS:
        if stats["recipe"][key] > 0:
            # First, see make portions of hotdog from each ingredient
            ing_max = stats[key] / stats["recipe"][key]
            # Next, see if ing_max is smallest out of all ingredient, mearning
            # max hotdogs
            max_por = ing_max if ing_max < max_por else max_por
    return floor(max_por)