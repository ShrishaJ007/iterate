# Time Complexity: O(n)
# Space Complexity: O(1)

def migratoryBirds(arr):
    frequency = [0] * 6

    for i in range(len(arr)):
        frequency[arr[i]] += 1

    max_frequency = 0
    bird_type = 0

    for i in range(1, 6):
        if frequency[i] > max_frequency:
            max_frequency = frequency[i]
            bird_type = i

    return bird_type


arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))