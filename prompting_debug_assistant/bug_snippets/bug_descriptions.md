# Bug Descriptions

## Bug 1 – bug1.py
### Intended behavior
Return the last n items from a list.

### Issue type
Off-by-one error / IndexError

### Explanation
The loop accesses an invalid index because it uses len(items) + 1.

### Fix
Replace len(items) + 1 with len(items).

---

## Bug 2 – bug2.py
### Intended behavior
Calculate the average of positive numbers.

### Issue type
Logical error

### Explanation
The code counts all elements instead of only positive numbers.

### Fix
Replace count = len(numbers) with count += 1.

---

## Bug 3 – bug3.js
### Intended behavior
Multiply all numbers in an array.

### Issue type
Incorrect initialization and loop boundary error

### Explanation
The product variable starts at 0 and the loop accesses an invalid index.

### Fix
Initialize product with 1 and replace <= with <.

### Second issue type
Type coercion

### Second explanation
A string causes concatenation instead of numeric addition.

### Second fix
Convert values to numbers before addition.

---

## Bug 4 – bug4.js
### Intended behavior
Fetch user data and print the username.

### Issue type
Missing await in asynchronous code

### Explanation
The Promise is used before it is resolved.

### Fix
Use async/await.

---

## Bug 5 – bug5.cpp
### Intended behavior
Reverse an array in-place.

### Issue type
Off-by-one error and syntax error

### Explanation
The code accesses an invalid array index and also misses a semicolon.

### Fix
Use size - 1 - i and add the missing semicolon.

---

## Bug 6 – bug6.py
### Intended behavior
Count word frequencies and return the top-N words.

### Issue type
KeyError and TypeError

### Explanation
The dictionary key may not exist and a float is used instead of an integer.

### Fix
Use freq.get(word, 0) + 1 and use an integer value.