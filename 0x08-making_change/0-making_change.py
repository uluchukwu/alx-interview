#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Sort coins in descending order for more efficient calculation
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    
    # If we exit the loop and total is not 0, it means we couldn't form the exact total
    if total != 0:
        return -1
    
    return count

