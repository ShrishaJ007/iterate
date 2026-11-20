"""
Genesis and Destruction
Digit-manipulation practice set
Date: 20 November 2026

"""


def remove_even_digits(n):
    """Return the number after removing all even digits."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d), where d is the number of digits.
# Space Complexity: O(1).


def remove_digits_less_than_five(n):
    """Return the number after removing digits smaller than 5."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit >= 5:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


def keep_digits_greater_than_five(n):
    """Return a number containing only digits greater than 5."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit > 5:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


def remove_zeros(n):
    """Remove every zero digit from the number."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit != 0:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


def replace_fives_with_nines(n):
    """Replace every digit 5 with 9."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit == 5:
            digit = 9
        result += digit * multiplier
        multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


def replace_even_digits_with_zero(n):
    """Replace every even digit with 0."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            digit = 0
        result += digit * multiplier
        multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


def remove_consecutive_duplicates(n):
    """Keep one digit from each consecutive run of equal digits."""
    digits = []
    previous = None

    for char in str(abs(n)):
        digit = int(char)
        if digit != previous:
            digits.append(char)
        previous = digit

    return int("".join(digits)) if digits else 0

# Time Complexity: O(d).
# Space Complexity: O(d), for the output digit list.


def remove_duplicate_digits_preserve_order(n):
    """Keep the first occurrence of each digit, preserving left-to-right order."""
    seen = set()
    result_digits = []

    for char in str(abs(n)):
        if char not in seen:
            seen.add(char)
            result_digits.append(char)

    return int("".join(result_digits)) if result_digits else 0

# Time Complexity: O(d) average, using set membership.
# Space Complexity: O(d), for the set and output list.


def extract_digits_divisible_by_three(n):
    """Return the digits divisible by 3, in their original order."""
    result = []
    for char in str(abs(n)):
        digit = int(char)
        if digit % 3 == 0:
            result.append(char)

    return int("".join(result)) if result else 0

# Time Complexity: O(d).
# Space Complexity: O(d), for the output digit list.


def reverse_number(n):
    """Return the number with its digits reversed."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    result = 0

    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n //= 10

    return sign * result

# Time Complexity: O(d).
# Space Complexity: O(1).


def sum_of_digits(n):
    """Return the sum of all digits."""
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

# Time Complexity: O(d).
# Space Complexity: O(1).


def product_of_digits(n):
    """Return the product of all digits."""
    n = abs(n)
    product = 1

    if n == 0:
        return 0

    while n > 0:
        product *= n % 10
        n //= 10

    return product

# Time Complexity: O(d).
# Space Complexity: O(1).


def difference_of_product_and_sum(n):
    """Return the product of digits minus the sum of digits."""
    return product_of_digits(n) - sum_of_digits(n)

# Time Complexity: O(d), from two digit traversals.
# Space Complexity: O(1).


def largest_digit(n):
    """Return the largest digit in the number."""
    n = abs(n)
    largest = 0

    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n //= 10

    return largest

# Time Complexity: O(d).
# Space Complexity: O(1).


def count_largest_digit(n):
    """Return (largest_digit, its_frequency)."""
    n = abs(n)

    if n == 0:
        return 0, 1

    largest = -1
    count = 0

    while n > 0:
        digit = n % 10

        if digit > largest:
            largest = digit
            count = 1
        elif digit == largest:
            count += 1

        n //= 10

    return largest, count

# Time Complexity: O(d).
# Space Complexity: O(1).


def second_largest_digit(n):
    """Return the second-largest distinct digit, or None if it doesn't exist."""
    n = abs(n)
    largest = -1
    second = -1

    while n > 0:
        digit = n % 10

        if digit > largest:
            second = largest
            largest = digit
        elif largest > digit > second:
            second = digit

        n //= 10

    return second if second != -1 else None

# Time Complexity: O(d).
# Space Complexity: O(1).


def second_smallest_digit(n):
    """Return the second-smallest distinct digit, or None if it doesn't exist."""
    n = abs(n)
    smallest = 10
    second = 10

    while n > 0:
        digit = n % 10

        if digit < smallest:
            second = smallest
            smallest = digit
        elif smallest < digit < second:
            second = digit

        n //= 10

    return second if second != 10 else None

# Time Complexity: O(d).
# Space Complexity: O(1).


def is_palindrome_number(n):
    """Return True if the number reads the same forwards and backwards."""
    if n < 0:
        return False

    return n == reverse_number(n)

# Time Complexity: O(d).
# Space Complexity: O(1).


def remove_digits_greater_than_five(n):
    """Return the number after removing all digits greater than 5."""
    n = abs(n)
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit <= 5:
            result += digit * multiplier
            multiplier *= 10
        n //= 10

    return result

# Time Complexity: O(d).
# Space Complexity: O(1).


if __name__ == "__main__":
    number = 5838251

    print("Genesis and Destruction")
    print("Remove even digits:", remove_even_digits(number))
    print("Remove digits less than 5:", remove_digits_less_than_five(number))
    print("Keep digits greater than 5:", keep_digits_greater_than_five(number))
    print("Remove zeros:", remove_zeros(number))
    print("Replace 5 with 9:", replace_fives_with_nines(number))
    print("Replace even digits with 0:", replace_even_digits_with_zero(number))
    print("Remove consecutive duplicates:", remove_consecutive_duplicates(number))
    print("Remove duplicate digits:", remove_duplicate_digits_preserve_order(number))
    print("Digits divisible by 3:", extract_digits_divisible_by_three(number))
    print("Reverse:", reverse_number(number))
    print("Sum of digits:", sum_of_digits(number))
    print("Product of digits:", product_of_digits(number))
    print("Product minus sum:", difference_of_product_and_sum(number))
    print("Largest digit:", largest_digit(number))
    print("Largest digit and count:", count_largest_digit(number))
    print("Second-largest digit:", second_largest_digit(number))
    print("Second-smallest digit:", second_smallest_digit(number))
    print("Is palindrome:", is_palindrome_number(number))
    print("Remove digits greater than 5:", remove_digits_greater_than_five(number))
