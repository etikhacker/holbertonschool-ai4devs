# Bug Analysis Report

---

## Bug 1 – bug1.py

### Intended Behavior
Return the last n items from a list.

### Issue Type
Off-by-one error / IndexError

### Explanation
The loop uses `len(items) + 1`, which accesses an invalid index and causes an `IndexError`.

### Recommended Fix
Replace `len(items) + 1` with `len(items)`.

---

## Bug 2 – bug2.py

### Intended Behavior
Calculate the average of positive numbers in a list.

### Issue Type
Logical error

### Explanation
The program counts all list elements instead of counting only positive numbers.

### Recommended Fix
Replace `count = len(numbers)` with `count += 1`.

---

## Bug 3 – bug3.js

### Intended Behavior
Multiply all numbers in an array and return the product.

### Issue Type
Incorrect initialization and loop boundary error

### Explanation
The product variable starts at `0` instead of `1`. The loop also accesses an invalid array index because it uses `<=`.

### Recommended Fix
Initialize `product` with `1` and replace `<=` with `<`.

### Second Issue Type
Type coercion

### Second Explanation
A string inside the array causes string concatenation instead of numeric addition.

### Second Recommended Fix
Convert values to numbers before addition.

---

## Bug 4 – bug4.js

### Intended Behavior
Fetch user data and print the username.

### Issue Type
Missing await in asynchronous code

### Explanation
The Promise returned by `getUser()` is used before it is resolved.

### Recommended Fix
Use `async/await` when calling `getUser()`.

---

## Bug 5 – bug5.cpp

### Intended Behavior
Reverse an array in-place and print it.

### Issue Type
Off-by-one error and syntax error

### Explanation
The code accesses an invalid array index and also contains a missing semicolon.

### Recommended Fix
Use `size - 1 - i` and add the missing semicolon.

---

## Bug 6 – bug6.py

### Intended Behavior
Count word frequencies and return the top-N words.

### Issue Type
KeyError and TypeError

### Explanation
The dictionary key may not exist on first access, and a float is used where an integer is required.

### Recommended Fix
Use `freq.get(word, 0) + 1` and replace the float value with an integer.