# prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]    
prices = [5, 1, 9]

def min_element (arr, low, high):
    # helper function to find the smallest element in the arr 
    smallest = float('inf')
    for element in range(low, high+1):
        smallest = min (smallest, arr[element])
    return smallest


def max_element (arr, low, high):
    # helper function to find the largest element in the arr 
    largest = float('-inf')
    for element in range(low, high+1):
        largest = max (largest, arr[element])
    return largest


def max_subarray(arr, low, high):
    # finds the max subarray recursively using divide and conquer algorithm

    if high == low:
        return 0
    elif high == low + 1:
        return max(arr[high] - arr[low], 0)
    
    mid_point = (high + low) // 2
    max_left = max_subarray(arr, low, mid_point)
    max_right = max_subarray(arr, mid_point + 1, high)
    min_left_half = min_element(arr, low, mid_point)
    max_right_half = max_element(arr, mid_point+1, high)

    return max(max_left, max_right, max_right_half - min_left_half)

print (max_subarray(prices, 0, len(prices)-1))
