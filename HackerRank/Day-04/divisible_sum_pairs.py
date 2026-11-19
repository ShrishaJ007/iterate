# Approach 1: Nested Loops
# Time: O(n²) | Space: O(1)

def divisibleSumPairs(n, k, ar):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count


# Approach 2: Frequency Counting (Remainder)
# Time: O(n + k) | Space: O(k)

def divisibleSumPairsOptimized(n, k, ar):
    count = 0
    freq = [0] * k

    for num in ar:
        remainder = num % k
        required = (k - remainder) % k

        count += freq[required]
        freq[remainder] += 1

    return count
