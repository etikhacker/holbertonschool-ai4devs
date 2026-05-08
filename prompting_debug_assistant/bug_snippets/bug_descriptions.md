## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Bug Description**: The loop range uses len(items)+1 instead of len(items), causing an IndexError on the last iteration.
**Fix**: Replace len(items)+1 with len(items) in the range() call.

## Bug 2 – bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list.
**Issue Type**: Logical error.
**Bug Description**: count is assigned len(numbers) instead of only counting positive values, resulting in a wrong average.
**Fix**: Increment count inside the if num > 0 block.

## Bug 3 – bug3.js
**Intended Behavior**: Multiply every number in an array and return the product.
**Issue Type**: Logical error and data type misuse.
**Bug Description**: product is initialized to 0 instead of 1, so the result is always 0. The loop uses <= causing an out-of-bounds undefined access.
**Fix**: Initialize product to 1 and change <= to < in the loop condition.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Runtime error.
**Bug Description**: getUser() returns a Promise but await is missing, so user is a Promise object and user.name is undefined.
**Fix**: Declare printUser as async and add await before getUser(id).

## Bug 5 – bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Bug Description**: A missing semicolon prevents compilation. The index arr[size-i] causes out-of-bounds access instead of arr[size-1-i].
**Fix**: Add the missing semicolon and replace arr[size-i] with arr[size-1-i] on both swap lines.

## Bug 6 – bug6.py
**Intended Behavior**: Count word frequency in a sentence and return the top N most frequent words.
**Issue Type**: Runtime KeyError and TypeError.
**Bug Description**: freq[word]+1 raises KeyError on first occurrence. Passing a float to string repetition raises TypeError.
**Fix**: Use freq.get(word, 0)+1 instead of freq[word]+1 and cast times to int.