// Bug 5 – bug5.cpp
// Intended: Reverse an array in-place and print it.

#include <iostream>
using namespace std;

void reverseArray(int arr[], int size) {
    for (int i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - i];    // BUG: should be arr[size - 1 - i] (off-by-one → out of bounds)
        arr[size - i] = temp;      // BUG: same issue on write
    }
}

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int size = sizeof(nums) / sizeof(nums[0])

    // BUG: missing semicolon on the line above → syntax error, won't compile

    reverseArray(nums, size);

    for (int i = 0; i < size; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
    // Expected output: 5 4 3 2 1
}