# Approach 1: Sorting + For Loops
# Time: O(n log n) | Space: O(n)

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min_sum = max_sum = 0

    for i in range(len(sorted_arr) - 1):
        min_sum += sorted_arr[i]

    for i in range(len(sorted_arr) - 1, 0, -1):
        max_sum += sorted_arr[i]

    print(min_sum, max_sum)


# Approach 2: Using sum(), max() and min()
# Time: O(n) | Space: O(1)

def miniMaxSumOptimal(arr):
    total = sum(arr)

    min_sum = total - max(arr)
    max_sum = total - min(arr)

    print(min_sum, max_sum)

