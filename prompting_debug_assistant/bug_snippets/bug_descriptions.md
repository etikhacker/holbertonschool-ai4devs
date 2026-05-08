## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 causing IndexError. Fix by using len(items).

## Bug 2 - bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list.
**Issue Type**: Logical error.
**Notes**: count uses len(numbers) instead of positive count only. Fix by incrementing count inside if num > 0.

## Bug 3 - bug3.js
**Intended Behavior**: Multiply all numbers in an array and return the product.
**Issue Type**: Logical error and type coercion.
**Notes**: product initialized to 0 instead of 1. Loop uses <= causing out-of-bounds. Fix by setting product=1 and using <.

## Bug 4 - bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Missing await.
**Notes**: getUser() returns a Promise without await so user.name is undefined. Fix by using async/await.

## Bug 5 - bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Notes**: Missing semicolon prevents compilation. arr[size-i] should be arr[size-1-i]. Fix both issues.

## Bug 6 - bug6.py
**Intended Behavior**: Count word frequency and return top N words.
**Issue Type**: KeyError and TypeError.
**Notes**: freq[word]+1 raises KeyError on first use. Float passed instead of int raises TypeError. Fix with freq.get(word,0)+1 and int cast.