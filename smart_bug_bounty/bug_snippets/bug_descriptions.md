# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error — range uses len(items)+1 causing an IndexError when n equals len(items).

## bug2.py
- **Intended Behavior**: Calculate the average of only positive numbers in a list.
- **Current Issue**: Logical error — count is assigned len(numbers) instead of counting only positive values, producing a wrong average.

## bug3.js
- **Intended Behavior**: Multiply all numbers in an array and return the product. Sum array values numerically.
- **Current Issue**: product initialized to 0 instead of 1; loop uses <= causing out-of-bounds access; string in array causes concatenation instead of addition.

## bug4.js
- **Intended Behavior**: Fetch user data asynchronously and print the username.
- **Current Issue**: Missing await keyword — getUser() returns a Promise and user.name is undefined.

## bug5.java
- **Intended Behavior**: Sum all elements of an integer array. Repeat a string a given number of times.
- **Current Issue**: Loop condition uses <= arr.length causing ArrayIndexOutOfBoundsException; repeat loop starts at i=1 instead of i=0, producing one fewer repetition than expected.

## bug6.py
- **Intended Behavior**: Count word frequency and return the top N most frequent words. Repeat a string a given number of times.
- **Current Issue**: freq[word]+1 raises KeyError on first occurrence; float passed to string repetition raises TypeError.