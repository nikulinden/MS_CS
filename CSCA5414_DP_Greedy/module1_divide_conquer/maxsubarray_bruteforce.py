stock_price_changes = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

def max_subarray_bruteforce(arr):
    max_sum = float('-inf')
    max_left = 0
    max_right = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum = current_sum + arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_left = i
                max_right = j
    return max_sum, max_left, max_right
max_sum, max_left, max_right = max_subarray_bruteforce(stock_price_changes)
print(max_sum, max_left, max_right)