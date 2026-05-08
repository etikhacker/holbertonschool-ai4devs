## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Expected Output**: [30, 40, 50] for n=3 and [10, 20, 30, 40, 50] for n=5.
**Notes**: The loop uses len(items)+1 causing IndexError when n equals len(items). Fix by using len(items).

## Bug 2 - bug2.py
**Intended Behavior**: Calculate the average of only positive numbers in a list.
**Issue Type**: Logical error.
**Expected Output**: 7.67 for input [5, -3, 10, -1, 0, 8].
**Notes**: count uses len(numbers) instead of counting only positives. Fix by incrementing count inside if num > 0.

## Bug 3 - bug3.js
**Intended Behavior**: Multiply all numbers in an array and return the product.
**Issue Type**: Logical error and type coercion.
**Expected Output**: 120 for [2, 3, 4, 5] and 6 for [1, 2, 3].
**Notes**: product initialized to 0 instead of 1. Loop uses <= causing out-of-bounds. Fix by setting product=1 and using <.

## Bug 4 - bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Missing await.
**Expected Output**: User name: Omar
**Notes**: getUser() returns a Promise without await so user.name is undefined. Fix by using async/await.

## Bug 5 - bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Expected Output**: 5 4 3 2 1
**Notes**: Missing semicolon prevents compilation. arr[size-i] should be arr[size-1-i]. Fix both issues.

## Bug 6 - bug6.py
**Intended Behavior**: Count word frequency and return top N most frequent words.
**Issue Type**: KeyError and TypeError.
**Expected Output**: ['the', 'cat'] for top 2 words.
**Notes**: freq[word]+1 raises KeyError on first use. Float passed instead of int raises TypeError. Fix with freq.get(word,0)+1 and int cast.