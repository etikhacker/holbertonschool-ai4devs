## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop range uses len(items)+1 instead of len(items), causing an IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 – bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list.
**Issue Type**: Logical error.
**Notes**: count is assigned len(numbers) instead of counting only positive values, producing a wrong average. Fix by incrementing count inside the if num > 0 block.

## Bug 3 – bug3.js
**Intended Behavior**: Multiply every number in an array and return the product.
**Issue Type**: Logical error and data type misuse.
**Notes**: product is initialized to 0 instead of 1, making the result always 0. The loop uses <= instead of <, causing an out-of-bounds access that returns NaN. Fix by initializing product to 1 and changing <= to <.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Runtime error due to missing await.
**Notes**: getUser() returns a Promise but await is missing, so user holds an unresolved Promise and user.name is undefined. Fix by declaring printUser as async and adding await before getUser(id).

## Bug 5 – bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Notes**: A missing semicolon after the size declaration prevents compilation. The swap uses arr[size-i] instead of arr[size-1-i], causing out-of-bounds memory access. Fix by adding the semicolon and correcting the index.

## Bug 6 – bug6.py
**Intended Behavior**: Count word frequency in a sentence and return the top N most frequent words.
**Issue Type**: Runtime KeyError and TypeError.
**Notes**: freq[word]+1 raises a KeyError on first occurrence of any word. Passing float 3.0 instead of int to string repetition raises TypeError. Fix by using freq.get(word, 0)+1 and casting times to int.