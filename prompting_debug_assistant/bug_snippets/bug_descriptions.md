## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Bug Description**: The loop range uses len(items)+1 instead of len(items), causing an IndexError when accessing an index beyond the list boundary.
**Fix**: Replace len(items)+1 with len(items) in the range() call.

## Bug 2 – bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list.
**Issue Type**: Logical error.
**Bug Description**: count is assigned len(numbers) which includes all elements instead of only the positive ones, resulting in a wrong average.
**Fix**: Increment count inside the if num > 0 block instead of using len(numbers).

## Bug 3 – bug3.js
**Intended Behavior**: Multiply every number in an array and return the product.
**Issue Type**: Logical error and data type misuse.
**Bug Description**: product is initialized to 0 instead of 1, making the result always 0. The loop condition uses <= instead of <, causing an out-of-bounds access that produces NaN.
**Fix**: Initialize product to 1 and change <= to < in the loop condition.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Runtime error due to missing await.
**Bug Description**: getUser() returns a Promise but await is missing, so user holds an unresolved Promise object and user.name returns undefined.
**Fix**: Declare printUser as async and add await before getUser(id).

## Bug 5 – bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Bug Description**: A missing semicolon after the size declaration prevents compilation. The swap uses arr[size-i] instead of arr[size-1-i], causing out-of-bounds memory access.
**Fix**: Add the missing semicolon and replace arr[size-i] with arr[size-1-i] on both swap lines.

## Bug 6 – bug6.py
**Intended Behavior**: Count word frequency in a sentence and return the top N most frequent words.
**Issue Type**: Runtime KeyError and TypeError.
**Bug Description**: freq[word]+1 raises a KeyError on the first occurrence of any word. Passing a float value of 3.0 instead of int to string repetition raises a TypeError.
**Fix**: Use freq.get(word, 0)+1 instead of freq[word]+1 and cast times to int before multiplication.