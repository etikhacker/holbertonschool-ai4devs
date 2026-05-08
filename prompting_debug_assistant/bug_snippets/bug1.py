def get_last_n(items, n):
    result = []
    for i in range(len(items) - n, len(items) + 1):
        result.append(items[i])
    return result

numbers = [10, 20, 30, 40, 50]
print(get_last_n(numbers, 3))
print(get_last_n(numbers, 5))