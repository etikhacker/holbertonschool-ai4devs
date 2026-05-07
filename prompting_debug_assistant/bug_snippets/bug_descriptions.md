## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 causing an IndexError when n equals len(items).

## Bug 2 – bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list.
**Issue Type**: Logical error.
**Notes**: count uses len(numbers) instead of counting only positive elements.

## Bug 3 – bug3.js
**Intended Behavior**: Multiply every number in an array and return the product.
**Issue Type**: Logical error and data type misuse.
**Notes**: product initialized to 0 instead of 1; loop bound uses <= causing undefined access.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Runtime error due to missing await.
**Notes**: getUser returns a Promise; without await, user.name is undefined.

## Bug 5 – bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Notes**: Missing semicolon prevents compilation; arr[size-i] should be arr[size-1-i].

## Bug 6 – bug6.py
**Intended Behavior**: Count word frequency in a sentence and return the top N words.
**Issue Type**: Runtime KeyError and TypeError.
**Notes**: freq[word]+1 raises KeyError on first occurrence; float passed instead of int.