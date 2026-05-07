# Bug Descriptions

A collection of intentionally flawed code snippets for debugging practice.
Each snippet has a clear intended behavior and contains one or more deliberate bugs.

---

## Bug 1 – `bug1.py`

**Language**: Python  
**Intended Behavior**: Return the last `n` items from a list.  
**Issue Type**: Off-by-one error → Runtime `IndexError`.  
**Notes**:  
The `range()` call uses `len(items) + 1` as the upper bound instead of `len(items)`.
On the final iteration, `items[len(items)]` is accessed, which is out of range.
The crash only occurs when `n == len(items)` (full list requested), making it easy to miss in partial tests.

**Fix**: Change `len(items) + 1` → `len(items)` in the `range()` call.

---

## Bug 2 – `bug2.py`

**Language**: Python  
**Intended Behavior**: Compute the average of all positive numbers in a list (ignoring zeros and negatives).  
**Issue Type**: Logical error — wrong denominator.  
**Notes**:  
`count` is assigned `len(numbers)` (total elements) instead of counting only the positive ones.
The result is silently wrong — no crash occurs — making this bug harder to spot.
For `[5, -3, 10, -1, 0, 8]`, expected output is `7.67` but actual is `3.83`.

**Fix**: Increment a `count` variable inside the `if num > 0` block.

---

## Bug 3 – `bug3.js`

**Language**: JavaScript  
**Intended Behavior**:  
1. Multiply all numbers in an array and return the product.  
2. Sum items in an array regardless of mixed types.  

**Issue Type**: Logical error (wrong initial value) + Loop out-of-bounds + Data type misuse.  
**Notes**:  
- `product` is initialized to `0` instead of `1` — any multiplication by `0` stays `0`.  
- The loop condition `i <= arr.length` accesses `arr[arr.length]` which is `undefined`, producing `NaN`.  
- `sumItems` uses `+` on a mixed array — when a string is encountered, JS switches to string concatenation silently.

**Fix**: Initialize `product = 1`, use `i < arr.length`, and validate/coerce types before summing.

---

## Bug 4 – `bug4.js`

**Language**: JavaScript  
**Intended Behavior**: Fetch a user object asynchronously and print the user's name.  
**Issue Type**: Async/Promise misuse — missing `await`.  
**Notes**:  
`getUser(id)` returns a `Promise`. Without `await`, the variable `user` holds the unresolved `Promise` object.
Accessing `user.name` on a Promise returns `undefined` — no error is thrown, making this a silent bug.
This is one of the most common real-world JavaScript mistakes.

**Fix**: Make `printUser` an `async` function and add `await` before `getUser(id)`.

---

## Bug 5 – `bug5.cpp`

**Language**: C++  
**Intended Behavior**: Reverse an integer array in-place and print the result.  
**Issue Type**: Syntax error (missing semicolon) + Off-by-one error (out-of-bounds memory access).  
**Notes**:  
- Missing `;` after `int size = sizeof(nums) / sizeof(nums[0])` — the program won't compile at all.  
- Even after fixing the semicolon, `arr[size - i]` instead of `arr[size - 1 - i]` causes an out-of-bounds write, leading to undefined behavior (possible crash or corrupted output).  

**Fix**: Add the missing semicolon; replace `arr[size - i]` with `arr[size - 1 - i]` on both swap lines.

---

## Bug 6 – `bug6.py`

**Language**: Python  
**Intended Behavior**:  
1. Count word frequency in a sentence and return the top-N most frequent words.  
2. Repeat a string a given number of times.  

**Issue Type**: Runtime `KeyError` (missing dict default) + `TypeError` from wrong data type.  
**Notes**:  
- `freq[word] + 1` raises `KeyError` on the first occurrence of any word since the key doesn't exist yet.  
- `multiply_string_times` is called with `3.0` (float) instead of `3` (int) — Python does not allow string repetition with a float.  
Both bugs cause crashes at runtime; neither is detectable at a glance.

**Fix**: Use `freq.get(word, 0) + 1`; cast `times` to `int` before the `*` operator.
