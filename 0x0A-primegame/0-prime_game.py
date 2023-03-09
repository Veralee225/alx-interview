#!/usr/bin/python3
"""
a python module to find the winner of a prime game
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number and
its multiples from the set. The player that cannot make a move loses the game.
"""


def FindPrimeNumbers(n):
    """
    FindPrimeNumbers-function to find the prime numbers
    Arguments:
        n: the given number
    Returns:
        the list of prime numbers
    """
    prm = []
    if n <= 1:
        return prm
    for i in range(2, n + 1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prm.append(i)
    return prm


def isWinner(x, nums):
    """
    isWinner- function to find the winner of a prime game
    Arguments:
        x: the number of rounds
        nums:array of n
    Returns:
        the winner of a prime game
    """
    if type(nums) is not list or type(x) is not int or x != len(nums):
        return None
    if not all(type(n) is int for n in nums) or x < 1:
        return None
    num_org = nums
    nums = sorted(nums, reverse=True)
    prime_lst = FindPrimeNumbers(nums[0])
    """
    since Maria goes first, she always wins if there are odd number of
    prime number in each round. Ben wins if there are even number of
    prime numbers. for each round
    set counters to identify the winner of the game.
    """
    Maria = 0
    Ben = 0

    for nm in num_org:
        prime_factor = 0
        for prm in prime_lst:
            if prm <= nm:
                prime_factor += 1
            else:
                break
        if prime_factor % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
