# Time Complexity: O(n * m)
# Space Complexity: O(1)

def getMoneySpent(keyboards, drives, b):
    max_spent = -1

    for i in range(len(keyboards)):
        for j in range(len(drives)):
            total = keyboards[i] + drives[j]

            if total <= b and total > max_spent:
                max_spent = total

    return max_spent


keyboards = [40, 50, 60]
drives = [5, 8, 12]
b = 60

print(getMoneySpent(keyboards, drives, b))