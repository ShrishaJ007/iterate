# Approach 1: Manual Iteration
# Time: O(n) | Space: O(1)

def aVeryBigSum(ar):
    total = 0

    for element in ar:
        total += element

    return total


# Approach 2: Built-in sum()
# Time: O(n) | Space: O(1)

def aVeryBigSumOptimal(ar):
    return sum(ar)