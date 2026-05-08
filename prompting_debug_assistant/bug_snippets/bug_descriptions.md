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
**Intended Behavior**: The function should take an integer array, reverse all its elements in-place, and print the reversed array to the console.
**Issue Type**: Syntax error and off-by-one error.
**Expected Output**: 5 4 3 2 1
**Notes**: Missing semicolon after size declaration prevents compilation. arr[size-i] should be arr[size-1-i] to avoid out-of-bounds memory access. Fix by adding the semicolon and correcting the index on both swap lines.

## Bug 6 - bug6.py
**Intended Behavior**: The function should count how many times each word appears in a sentence and return the top N most frequent words as a list. A second function should repeat a string a given number of times using an integer.
**Issue Type**: Runtime KeyError and TypeError.
**Expected Output**: ['the', 'cat'] for top 2 words. 'hello hello hello ' for string repetition.
**Notes**: freq[word]+1 raises KeyError on first occurrence of any word. Float 3.0 passed instead of int raises TypeError. Fix with freq.get(word,0)+1 and cast times to int.