# Important, Run this cell below
W = 200 # weight limit is 200
weights = [1, 5, 20, 35, 90] # These are the weights of individual items
values = [15, 14.5, 19.2, 19.8, 195.2] # These are the values of individual items

def maxStealZero(capacity_left, item_index, item_weights, item_values):
    assert item_index >= 0
    assert len(item_weights) == len(item_values)

    if capacity_left == 0:
        return 0
    if capacity_left < 0:
        return float('-inf')
    if item_index >= len(item_weights):
        return 0

    result = max(values[item_index] + maxStealZero(capacity_left - item_weights[item_index], item_index+1, item_weights, item_values),
             maxStealZero(capacity_left, item_index+1, item_weights, item_values))

    return result

print(maxStealZero(W, 0, weights, values))


def memoizedMaxStealZeroOne(capacity_left, weights, values): 
    n = len(weights)
    assert (len(values) == n), 'Weights and Values list must be of same size'
    assert (capacity_left >= 0)
    if capacity_left == 0: 
        return 0, []# nothing to steal and 0 value derived.
    
    # Initialize the memo table as a list of lists
    # fill in all entries with a zero
    T = [ [0 for j in range(n)] for w in range(capacity_left+1)]
    S = [ [0 for j in range(n)] for w in range(capacity_left+1)]

    # we will use this helper method to access our memo table.
    # it will save us a lot of code later.
    def getTblEntry(w, j): 
        if w == 0: 
            return 0
        if w < 0: 
            return -float('inf')
        if j >= n:
            return 0
        return T[w][j]

    for w in range(1, capacity_left+1): # w in ascending order from 1 to W.
        for j in range(n-1, -1, -1):  # this is a descending order loop from n-1 to 0.
            # this allows us to simultaneously fill T, S without using if-then-else loop
            take = (values[j] + getTblEntry(w - weights[j], j + 1), 1)
            skip = (getTblEntry(w, j + 1), 0)
            T[w][j], S[w][j] = max(take, skip)

    itemsToSteal = [] 
    # recover solution
    weightOfKnapsack = capacity_left  
    for j in range(n): 
        if (S[weightOfKnapsack][j] == 1):
            itemsToSteal.append(j)
            weightOfKnapsack = weightOfKnapsack - weights[j]
            print(f'Steal Item {j}: Weight = {weights[j]}, Value = {values[j]}')
    print(f'Total weight stolen: {capacity_left - weightOfKnapsack}, value = {T[capacity_left][0]}')
    return (T[capacity_left][0], itemsToSteal)

