def binary_search(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))
    print(binary_search(data, 1))
    print(binary_search(data, 13))
    print(binary_search(data, 4))
