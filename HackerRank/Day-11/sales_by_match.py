# Time Complexity: O(n²)
# Space Complexity: O(1)

def sockMerchant(n, ar):
    pair_count = 0

    for i in range(len(ar)):
        seen = False

        for j in range(i):
            if ar[i] == ar[j]:
                seen = True
                break

        if seen:
            continue

        frequency = 0

        for j in range(len(ar)):
            if ar[i] == ar[j]:
                frequency += 1

        pair_count += frequency // 2

    return pair_count


# Time Complexity: O(n) average
# Space Complexity: O(n)

def sockMerchant(n, ar):
    frequency = {}
    pair_count = 0

    for i in range(n):
        color = ar[i]

        if color in frequency:
            frequency[color] += 1
        else:
            frequency[color] = 1

    for color in frequency:
        pair_count += frequency[color] // 2

    return pair_count


n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

print(sockMerchant(n, ar))