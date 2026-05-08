def average_positives(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

data = [5, -3, 10, -1, 0, 8]
result = average_positives(data)
print(f"Average of positives: {result}")