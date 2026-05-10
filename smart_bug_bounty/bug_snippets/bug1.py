"""
bug1.py
Intended behavior: Binary search — return the index of target in a sorted list,
or -1 if not found.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr)          # BUG: should be len(arr) - 1 (off-by-one)

    while low < high:        # BUG: should be low <= high (misses single-element check)
        mid = (low + high) / 2   # BUG: integer division required: (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))   # expected: 3
    print(binary_search(data, 1))   # expected: 0
    print(binary_search(data, 13))  # expected: 6
    print(binary_search(data, 4))   # expected: -1
