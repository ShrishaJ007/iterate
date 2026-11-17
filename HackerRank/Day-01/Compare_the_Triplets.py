# Approach 1: Manual Indexing
# Time: O(n) | Space: O(1)

def compareTriplets(a, b):
    alice = bob = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]


# Approach 2: Using zip()
# Time: O(n) | Space: O(1)

def compareTripletsOptimal(a, b):
    alice = bob = 0

    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1

    return [alice, bob]