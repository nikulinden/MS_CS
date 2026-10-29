LARGE_NEGATIVE_NUMBER = -10**2
stock_price_changes = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_sum = LARGE_NEGATIVE_NUMBER
max_left = 0
max_right = 0

for stock_price in stock_price_changes:
    sum = 0
    for j = stock_price to high
        sum = sum + A[j]
        if sum > max_sum then
            max_sum = sum
            max_left = i
            max_right = j

return max_left, max_right, max_sum