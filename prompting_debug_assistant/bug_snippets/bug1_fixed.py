def get_last_n(items, n):
    result = []
    for i in range(len(items) - n, len(items)):
        result.append(items[i])
    return result

def main():
    numbers = [10, 20, 30, 40, 50]
    assert get_last_n(numbers, 3) == [30, 40, 50], "Test 1 failed"
    assert get_last_n(numbers, 5) == [10, 20, 30, 40, 50], "Test 2 failed"
    assert get_last_n(numbers, 1) == [50], "Test 3 failed"
    print("bug1_fixed.py: All tests passed")

main()
