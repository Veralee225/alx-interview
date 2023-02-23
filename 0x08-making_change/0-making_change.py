#!/usr/bin/python3
"""
a python module to make a change
"""


def makeChange(coins, total):
    """
    makeChange-function to find fewest number of coins needed to meet total
    Arguments:
        coins: the given coins
        total: the given total we need to acheive
    Returns:
        the fewest number of coins to meet total
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    coins_nbr = {}
    for cn in sorted_coins:
        if total % cn == 0:
            coins_nbr[cn] = total / cn
            rslt = sum(coins_nbr.values())
            return int(rslt)
        else:
            coins_nbr[cn] = total // cn
            total = total % cn
    return -1
