stock_price_changes = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_sum = float('-inf')
max_left = 0
max_right = 0

for i in range(len(stock_price_changes)):
    sum = 0
    for j in range(len(stock_price_changes)):
        if j < i:
            continue;
        sum = sum + stock_price_changes[j]
        if sum > max_sum:
            max_sum = sum
            max_left = i
            max_right = j

print(max_sum, max_left, max_right)