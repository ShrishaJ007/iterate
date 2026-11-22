
# ==========================================
# NUMBER THEORY PRACTICE
# ==========================================


# 1. FIND ALL DIVISORS

def all_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


# 2. COUNT COMMON DIVISORS

def count_common_divisors(a, b):
    common_divisors = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)

    return len(common_divisors)


# 3. GCD - BRUTE FORCE

def brute_gcd(a, b):
    common_divisors = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)

    return max(common_divisors)


# 4. GCD - EUCLIDEAN ALGORITHM

def calculate_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


# 5. LCM - BRUTE FORCE

def brute_lcm(a, b):
    common_divisors = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)

    gcd = max(common_divisors)

    return (a * b) // gcd


# 6. LCM - USING EUCLIDEAN GCD

def calculate_lcm(a, b):
    return (a * b) // calculate_gcd(a, b)


# 7. GCD OF AN ARRAY

def gcd_arr(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        result = calculate_gcd(result, arr[i])

    return result


# 8. LCM OF AN ARRAY

def lcm_arr(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        result = result * arr[i] // calculate_gcd(result, arr[i])

    return result


# 9. COMMON MULTIPLES WITHIN A LIMIT

def common_multiples(a, b, limit):
    lcm = calculate_lcm(a, b)

    result = []

    for num in range(lcm, limit + 1, lcm):
        result.append(num)

    return result


# 10. PERFECT NUMBER

def perfect_number(n):
    result = 0

    for i in range(1, n):
        if n % i == 0:
            result += i

    return n == result


# 11. COPRIME NUMBERS

def are_coprime(a, b):
    return calculate_gcd(a, b) == 1


# 12. EULER'S TOTIENT FUNCTION - BRUTE FORCE

def euler_totient(n):
    count = 0

    for i in range(1, n + 1):
        if calculate_gcd(i, n) == 1:
            count += 1

    return count


# ==========================================
# TEST CASES
# ==========================================

print("All divisors:", all_divisors(12))

print("Common divisors:", count_common_divisors(12, 18))

print("Brute GCD:", brute_gcd(48, 36))

print("Euclidean GCD:", calculate_gcd(48, 36))

print("Brute LCM:", brute_lcm(12, 18))

print("Euclidean LCM:", calculate_lcm(12, 18))

print("GCD of array:", gcd_arr([4, 6, 8, 12, 16]))

print("LCM of array:", lcm_arr([4, 6, 8, 12, 16]))

print("Common multiples:", common_multiples(4, 6, 50))

print("Perfect number:", perfect_number(6))

print("Are coprime:", are_coprime(2, 3))

print("Euler Totient:", euler_totient(9))
