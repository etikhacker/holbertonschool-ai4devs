## Bug 1 – bug1.py
**AI Diagnosis**: The range() call uses len(items)+1 as the upper bound, which causes the loop to access items[len(items)] on the final iteration. Since valid indexes end at len(items)-1, this raises an IndexError.
**Suggested Fix**: Change len(items)+1 to len(items) in the range() call.
**Alternative Fixes Tested**: Using items[-n:] slice instead of the loop — works correctly and is more Pythonic.
**Result**: Both fixes work. The slice approach is simpler.

## Bug 2 – bug2.py
**AI Diagnosis**: The variable count is assigned len(numbers) after the loop, which counts all elements including negatives and zeros. This produces a wrong denominator for the average calculation.
**Suggested Fix**: Remove count = len(numbers) and instead increment count += 1 inside the if num > 0 block.
**Alternative Fixes Tested**: Using list comprehension: positives = [n for n in numbers if n > 0] then sum(positives)/len(positives) — also works.
**Result**: Both fixes work as expected.

## Bug 3 – bug3.js
**AI Diagnosis**: Two bugs exist. First, product is initialized to 0 instead of 1, making any multiplication result 0. Second, the loop condition i <= arr.length accesses arr[arr.length] which is undefined, causing NaN. Additionally, sumItems fails on mixed arrays because JavaScript uses + for both addition and concatenation.
**Suggested Fix**: Initialize product = 1, change <= to <, and use Number(val) to coerce types in sumItems.
**Alternative Fixes Tested**: Using arr.reduce((acc, val) => acc * val, 1) for productOfArray — cleaner and avoids the loop bug entirely.
**Result**: Both approaches work correctly.

## Bug 4 – bug4.js
**AI Diagnosis**: getUser() is an async function that returns a Promise. Without await, the variable user holds an unresolved Promise object. Accessing user.name on a Promise returns undefined without throwing an error, making this a silent bug.
**Suggested Fix**: Declare printUser as async and add await before getUser(id).
**Alternative Fixes Tested**: Using .then() chain: getUser(id).then(user => console.log(User name: ${user.name})) — also works.
**Result**: Both async/await and .then() approaches work correctly.

## Bug 5 – bug5.cpp
**AI Diagnosis**: Two bugs exist. First, a missing semicolon after int size = sizeof(nums)/sizeof(nums[0]) causes a compilation error. Second, the swap uses arr[size-i] instead of arr[size-1-i], which accesses memory one position beyond the array boundary on the first iteration.
**Suggested Fix**: Add the missing semicolon and replace arr[size-i] with arr[size-1-i] on both swap lines.
**Alternative Fixes Tested**: Using std::reverse(nums, nums+size) from the algorithm header — eliminates the manual swap entirely.
**Result**: Both fixes work. std::reverse is the safest approach.

## Bug 6 – bug6.py
**AI Diagnosis**: Two bugs exist. First, freq[word]+1 raises a KeyError when a word appears for the first time because the key does not yet exist in the dictionary. Second, multiply_string_times receives a float value 3.0 instead of an integer, and Python does not allow string repetition with floats, raising a TypeError.
**Suggested Fix**: Replace freq[word]+1 with freq.get(word, 0)+1 and cast times to int before the multiplication operator.
**Alternative Fixes Tested**: Using collections.Counter(words) instead of the manual dictionary — handles all counting automatically without KeyError.
**Result**: Both fixes work. Counter is the more Pythonic solution.