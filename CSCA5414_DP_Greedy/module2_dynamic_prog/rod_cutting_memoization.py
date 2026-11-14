L = 300
sizes =  [ 1, 3, 5, 10, 30, 50, 75]
prices = [ 0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]
memo = {}

def maxRevenueMemoizeTopDown(L, sizes, prices, memo):
    if L == 0:
        return 0
    if L < 0:
        return -100000
    if L in memo:
        return memo[L]

    max_value = [(maxRevenueMemoizeTopDown(L-sizes[i], sizes, prices, memo) + prices[i]) for i in range(len(sizes))]
    max_value.append(0)
    max_value_sofar = max(max_value)
    memo[L] = max_value_sofar
    
    return max_value_sofar    


def best_table(length, sizes, prices):
    # bottom up no recursion using T table
    table = [0]*(length + 1)

    for l in range(1, length + 1):
        options = [0]
        for i in range(len(sizes)):
            if l - sizes[i] >= 0:
                options.append(prices[i] + table[l - sizes[i]])
        table[l] = max(options)
    
    return table[l]

print(f"This is top down: {maxRevenueMemoizeTopDown(L, sizes, prices, memo)}")
print(f"This is bottom up: {best_table(L, sizes, prices)}")
