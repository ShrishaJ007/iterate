# Approach 1: Manual Counting
# Time: O(n) | Space: O(1)

def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0

    for candle in candles:
        if candle == tallest:
            count += 1

    return count

    
# Approach 2: Using count()
# Time: O(n) | Space: O(1)

def birthdayCakeCandlesCount(candles):
    return candles.count(max(candles))
