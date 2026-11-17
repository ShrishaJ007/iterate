
# Approach 1: Manual Counting
# Time: O(n) | Space: O(1)

def plusMinus(arr):
    positive = negative = zero = 0
    n = len(arr)

    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    print(f"{positive / n:.6f}")
    print(f"{negative / n:.6f}")
    print(f"{zero / n:.6f}")


# Approach 2: Using Generator expression with built-in sum()
# Time: O(n) | Space: O(1)

def plusMinusOptimal(arr):
    n = len(arr)

    print(f"{sum(x > 0 for x in arr) / n:.6f}")
    print(f"{sum(x < 0 for x in arr) / n:.6f}")
    print(f"{sum(x == 0 for x in arr) / n:.6f}")
