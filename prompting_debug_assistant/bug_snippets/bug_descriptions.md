## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Bug Description**: The range() call uses len(items)+1 instead of len(items), causing an IndexError when accessing items[len(items)].

## Bug 2 – bug2.py
**Intended Behavior**: Calculate the average of all positive numbers in a list, ignoring zeros and negatives.
**Issue Type**: Logical error.
**Bug Description**: The variable count is set to len(numbers) instead of counting only positive elements, producing a wrong average.

## Bug 3 – bug3.js
**Intended Behavior**: Multiply every number in an array and return the product.
**Issue Type**: Logical error and data type misuse.
**Bug Description**: The product variable is initialized to 0 instead of 1, and the loop condition uses <= causing an out-of-bounds access that returns NaN.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch user data asynchronously and print the username.
**Issue Type**: Runtime error due to missing await.
**Bug Description**: The getUser() function returns a Promise, but await is missing, so user holds a Promise object and user.name is undefined.

## Bug 5 – bug5.cpp
**Intended Behavior**: Reverse an integer array in-place and print the result.
**Issue Type**: Syntax error and off-by-one error.
**Bug Description**: A missing semicolon prevents compilation. Additionally, arr[size-i] should be arr[size-1-i], causing out-of-bounds memory access.

## Bug 6 – bug6.py
**Intended Behavior**: Count word frequency in a sentence and return the top N most frequent words.
**Issue Type**: Runtime KeyError and TypeError.
**Bug Description**: Using freq[word]+1 raises a KeyError on the first occurrence of any word. A float value passed to string repetition causes a TypeError.