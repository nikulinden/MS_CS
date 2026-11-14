import matplotlib.pyplot as plt
import time
lst0 = [1, 4, 7, 9, 16, 43]
x0 = 33

def minCoins_recursive(amount, denominations):
    # returns minimum number of coins to make up the collection
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    options = [ 1 + minCoins_recursive(amount - coin, denominations) for coin in denominations ]
    collection = min(options)

    return collection

print(minCoins_recursive(x0, lst0))