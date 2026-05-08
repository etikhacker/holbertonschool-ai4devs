# Bug Analysis Report

## Bug 1 – bug1.py

### Intended Behavior
The function should safely return the last `n` elements from a list.

### Expected Behavior Example
- Input: `[10, 20, 30, 40, 50], n = 3`
- Output: `[30, 40, 50]`

### Issue Type
Off-by-one error / IndexError

### Explanation
The loop accesses an invalid index because it uses `len(items) + 1`.

### Recommended Fix
Replace `len(items) + 1` with `len(items)`.

---

## Bug 2 – bug2.py

### Intended Behavior
The function should calculate the average of only positive numbers.

### Expected Behavior Example
- Input: `[5, -3, 10, -1, 0, 8]`
- Output: `7.67`

### Issue Type
Logical error

### Explanation
The code counts all numbers instead of only positive numbers.

### Recommended Fix
Replace `count = len(numbers)` with `count += 1`.

---

## Bug 3 – bug3.js

### Intended Behavior
The function should multiply all numbers in an array and return the final product.

### Expected Behavior Example
- Input: `[2, 3, 4, 5]`
- Output: `120`

### Issue Type
Incorrect initialization and loop boundary error

### Explanation
The variable `product` starts at `0` instead of `1`. The loop also accesses an invalid array index.

### Recommended Fix
Initialize `product` with `1` and replace `<=` with `<`.

#### Second Bug

### Intended Behavior
The function should add all array values numerically.

### Expected Behavior Example
- Input: `[1, "2", 3]`
- Output: `6`

### Issue Type
Type coercion

### Explanation
A string value causes concatenation instead of numeric addition.

### Recommended Fix
Convert all values to numbers before addition.

---

## Bug 4 – bug4.js

### Intended Behavior
The function should fetch user data asynchronously and display the username correctly.

### Expected Behavior Example
- Input: `42`
- Output: `User name: Omar`

### Issue Type
Missing await in asynchronous code

### Explanation
The Promise returned by `getUser()` is accessed before it resolves.

### Recommended Fix
Use `async/await` when calling `getUser()`.

---

## Bug 5 – bug5.cpp

### Intended Behavior
The function should reverse an array in-place and print the reversed result correctly.

### Expected Behavior Example
- Input: `[1, 2, 3, 4, 5]`
- Output: `5 4 3 2 1`

### Issue Type
Off-by-one error and syntax error

### Explanation
The code accesses an invalid array index and also contains a missing semicolon.

### Recommended Fix
Replace `arr[size - i]` with `arr[size - 1 - i]` and add the missing semicolon.

---

## Bug 6 – bug6.py

### Intended Behavior
The function should count word frequencies and return the top-N most common words.

### Expected Behavior Example
- Input: `"hello world hello", n = 1`
- Output: `["hello"]`

### Issue Type
KeyError and TypeError

### Explanation
The dictionary key may not exist during the first occurrence of a word. A float value is also used where an integer is required.

### Recommended Fix
Use `freq.get(word, 0) + 1` and replace the float value with an integer.