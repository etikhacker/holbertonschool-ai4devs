$content = @"
# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and C++.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function average_positives should iterate over a list and compute the mean of only the positive numbers, ignoring zeros and negatives.
**Issue Type**: Logical error.
**Notes**: count is set to len(numbers) which includes all elements. Fix by incrementing count only inside the if num > 0 block.

## Bug 3 - bug3.js
**Intended Behavior**: The function productOfArray should multiply all numbers in an array and return the total product. The function sumItems should return the numeric sum of all array elements.
**Issue Type**: Logical error and type coercion.
**Notes**: product initialized to 0 instead of 1 so result is always 0. Loop uses <= causing undefined access. String in array causes concatenation. Fix by setting product=1, using <, and coercing types.

## Bug 4 - bug4.js
**Intended Behavior**: The function printUser should asynchronously fetch a user object by ID and print the user name to the console.
**Issue Type**: Missing await in asynchronous code.
**Notes**: getUser() returns a Promise but await is missing so user holds an unresolved Promise and user.name is undefined. Fix by declaring printUser as async and adding await before getUser(id).

## Bug 5 - bug5.cpp
**Intended Behavior**: The function reverseArray should reverse all elements of an integer array in-place. The result should then be printed to the console in reversed order.
**Issue Type**: Syntax error and off-by-one error.
**Notes**: Missing semicolon after size declaration prevents compilation. arr[size-i] causes out-of-bounds access and should be arr[size-1-i] on both swap lines.

## Bug 6 - bug6.py
**Intended Behavior**: The function top_n_words should count how many times each word appears in a sentence and return the top N most frequent words as a list. The function multiply_string_times should repeat a string a given number of integer times.
**Issue Type**: Runtime KeyError and TypeError.
**Notes**: freq[word]+1 raises KeyError on first occurrence of any word. Float 3.0 passed instead of int raises TypeError for string repetition. Fix with freq.get(word,0)+1 and cast times to int.
"@
[System.IO.File]::WriteAllText("D:\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)