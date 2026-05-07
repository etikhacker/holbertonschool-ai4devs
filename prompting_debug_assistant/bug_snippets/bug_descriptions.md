# Bug Descriptions

---

## Bug 1 – bug1.py

### Intended behavior
Return the last n items from a list.

### Issue type
Off-by-one error / IndexError

### Explanation
The loop uses `len(items) + 1`, which causes the program to access an invalid list index. This results in an `IndexError`.

### Fix
Replace `len(items) + 1` with `len(items)` in the loop range.

---

## Bug 2 – bug2.py

### Intended behavior
Calculate the average of positive numbers in a list.

### Issue type
Logical error

### Explanation
The program counts all elements in the list instead of counting only positive numbers. Because of this, the average is calculated incorrectly.

### Fix
Replace `count = len(numbers)` with `count += 1`.

---

## Bug 3 – bug3.js

### Intended behavior
Multiply all numbers in an array and return the product.

### Issue type
Incorrect initialization and loop boundary error

### Explanation
The variable `product` starts at `0` instead of `1`. The loop also uses `<=`, which accesses an invalid array index.

### Fix
Initialize `product` with `1` and replace `<=` with `<` in the loop condition.

### Second issue type
Type coercion

### Second explanation
A string value inside the array causes string concatenation instead of numeric addition.

### Second fix
Convert all values to numbers before addition.

---

## Bug 4 – bug4.js

### Intended behavior
Fetch user data and print the username.

### Issue type
Missing await in asynchronous code

### Explanation
`getUser()` returns a Promise, but the code tries to use the result before the Promise is resolved.

### Fix
Use `async/await` when calling `getUser()`.

---

## Bug 5 – bug5.cpp

### Intended behavior
Reverse an array in-place and print it.

### Issue type
Off-by-one error and syntax error

### Explanation
The code accesses `arr[size - i]`, which is outside the valid array range. There is also a missing semicolon after the size calculation.

### Fix
Replace `arr[size - i]` with `arr[size - 1 - i]` and add the missing semicolon.

---

## Bug 6 – bug6.py

### Intended behavior
Count word frequencies and return the top-N words.

### Issue type
KeyError and TypeError

### Explanation
The dictionary key may not exist when a word appears for the first time. A float value is also used where an integer is expected for string multiplication.

### Fix
Use `freq.get(word, 0) + 1` and replace the float value with an integer.