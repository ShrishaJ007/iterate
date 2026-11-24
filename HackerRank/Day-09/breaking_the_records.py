# Time Complexity: O(n)
# Space Complexity: O(1)

def breakingRecords(scores):
    highest = lowest = scores[0]
    best = worst = 0

    for score in scores:
        if score > highest:
            highest = score
            best += 1
        elif score < lowest:
            lowest = score
            worst += 1

    return [best, worst]