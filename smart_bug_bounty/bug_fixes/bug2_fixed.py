def average_positives(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1
    if count == 0:
        return 0
    return total / count

def main():
    assert round(average_positives([5, -3, 10, -1, 0, 8]), 2) == 7.67, "Test 1 failed"
    assert average_positives([-1, -2, -3]) == 0, "Test 2 failed"
    assert average_positives([4, 4]) == 4.0, "Test 3 failed"
    print("bug2_fixed.py: All tests passed")

main()
