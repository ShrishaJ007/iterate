# Time Complexity: O(n)
# Space Complexity: O(1)

def bonAppetit(bill, k, b_charged):
    total = 0

    for i in range(len(bill)):
        if i != k:
            total += bill[i]

    b_actual = total // 2

    if b_actual == b_charged:
        print("Bon Appetit")
    else:
        print(b_charged - b_actual)