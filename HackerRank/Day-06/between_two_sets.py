# Time Complexity: O(R * (A + B))
# Space Complexity: O(R)
# A = Length of array a
# B = Length of array b
# R = Number of integers in the candidate range

def getTotalX(a, b):
    possible_candidates = []

    # First condition: Every element in a must divide i
    for i in range(min(a), min(b) + 1):
        possible = True

        for element in a:
            if i % element != 0:
                possible = False
                break

        if possible:
            possible_candidates.append(i)

    # Second condition: i must divide every element in b
    valid_candidates = []

    for num in possible_candidates:
        valid = True

        for element in b:
            if element % num != 0:
                valid = False
                break

        if valid:
            valid_candidates.append(num)

    return len(valid_candidates)


a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))