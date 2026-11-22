# Time Complexity: O((A + B) * log M + G/L)
# Space Complexity: O(1)

def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def getTotalX(a, b):

    # Step 1: Find LCM of array a
    lcm_a = a[0]

    for i in range(1, len(a)):
        lcm_a = (lcm_a * a[i]) // find_gcd(lcm_a, a[i])

    # Step 2: Find GCD of array b
    gcd_b = b[0]

    for i in range(1, len(b)):
        gcd_b = find_gcd(gcd_b, b[i])

    # Step 3: Count valid candidates
    count = 0

    for num in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % num == 0:
            count += 1

    return count


a = [4, 6, 8, 12, 16]
b = [240, 480, 720, 960, 1200]

print(getTotalX(a, b))