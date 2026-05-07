# Bug 1 – bug1.py
# Intended: Return the last n items from a list.

def get_last_n(items, n):
    result = []
    for i in range(len(items) - n, len(items) + 1):  # BUG: should be len(items), not len(items)+1
        result.append(items[i])                        # IndexError when i == len(items)
    return result


# Test
numbers = [10, 20, 30, 40, 50]
print(get_last_n(numbers, 3))   # Expected: [30, 40, 50]
print(get_last_n(numbers, 5))   # Expected: [10, 20, 30, 40, 50] — crashes here