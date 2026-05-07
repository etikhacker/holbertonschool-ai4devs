# Bug 2 – bug2.py
# Intended: Calculate the average of all positive numbers in a list.

def average_positives(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
    count = len(numbers)  # BUG: should count only positives, not all elements
    if count == 0:
        return 0
    return total / count


# Test
data = [5, -3, 10, -1, 0, 8]
result = average_positives(data)
print(f"Average of positives: {result}")
# Expected: (5 + 10 + 8) / 3 = 7.67
# Actual:   (5 + 10 + 8) / 6 = 3.83  ← WRONG