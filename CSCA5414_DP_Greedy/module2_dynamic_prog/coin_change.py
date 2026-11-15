import matplotlib.pyplot as plt
import time
lst0 = [1, 5, 10, 25, 50, 100]
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

#print(minCoins_recursive(18, lst0))


def minCoin_memoize(amount, denominations):
    table = [0] * (amount + 1)
    for i in range(1, amount+1):
        options = [1 + table[i - cj] for cj in denominations if (i - cj >= 0)]
        options.append(1000000)
        table[i] = min(options)

    return table[amount]

def minCoin_memoize_recover(amount, denominations):
    table = [0] * (amount + 1)
    solution = [-1] * (amount + 1) # best current / immediate decision
    coins_used = []
    print("   i | coins needed  | first coin     | options (count, coin)")
    print("-"*100)
    for i in range(1, amount+1):
        # options = [(1 + table[i - cj], cj) for cj in denominations if (i - cj >= 0)]
        options = []
        for cj in denominations:
            if i - cj >= 0:
                options.append((1 + table[i - cj], cj))
        options.append((1000000, -1))
        table[i], solution[i] = min(options)
        print(f"{i:>4} | table={table[i]:>3} | first coin={solution[i]:>3} | options={options}")
    # NOW RECOVER the list of coins by using the S table.
    value_left = amount
    while value_left > 0:
        coins_used.append(solution[value_left])
        value_left = value_left - solution[value_left]
    assert value_left == 0
    
    return table[amount], coins_used

# for amounts in [20, 25, 30, 35, 40, 45]:
#     start = time.perf_counter()
#     # result = minCoins_recursive(amounts, lst0)
#     result = minCoin_memoize_recover(amounts, lst0)
#     elapsed = time.perf_counter() - start
#     print(f"amount: {amounts}\nminimum coins:{result[0]}\ncoins denom: {result[1]} ")

minCoin_memoize_recover(20, lst0)
# run  python coin_change.py > trace.txt