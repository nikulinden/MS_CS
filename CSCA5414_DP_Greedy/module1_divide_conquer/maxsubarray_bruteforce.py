max_sum = negative infinity
max_left = 0
max_right = 0

for i = low to high
    sum = 0
        for j = i to high
            sum = sum + A[j]
            if sum > max_sum then
                max_sum = sum
                max_left = i
                max_right = j
end

return max_left, max_right, max_sum