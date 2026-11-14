L = 30
sizes =  [ 1, 3, 5, 10, 30, 50, 75]
prices = [ 0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]

def maxRevenue(L, sizes, prices):
    k = len(sizes)
    max_value = []
    if L == 0:
        return 0
    if L < 0:
        return (-10000000000)
    
    max_value = [(maxRevenue(L-sizes[i], sizes, prices)+prices[i]) for i in range(k)]
    # for i in range(k):
    #     value = maxRevenue(L-sizes[i], sizes, prices) + prices[i]
    #     print(f"L={L}, cut={sizes[i]}, value={value}")
    #     max_value.append(value)
    max_value.append(0)
    max_value_sofar = max(max_value)
    print(f"max revenue = {max_value_sofar}")
    return max_value_sofar

print(maxRevenue(L, sizes, prices))