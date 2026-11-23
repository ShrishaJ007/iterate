# Time Complexity: O(m + n)
# Space Complexity: O(1)

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0

    for distance in apples:
        position = a + distance

        if s <= position <= t:
            count_apples += 1

    for distance in oranges:
        position = b + distance

        if s <= position <= t:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)


s = 7
t = 11
a = 5
b = 15

apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)