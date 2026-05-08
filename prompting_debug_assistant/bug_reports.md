# Bug Reports

---

## Bug Report – bug1.py
- **File**: `bug_snippets/bug1.py`
- **Summary**: Off-by-one error causes an IndexError when retrieving the last n items of a list.
- **Root Cause**: The `range()` call used `len(items) + 1` as the upper bound, causing the loop to access `items[len(items)]` which is out of range.
- **Before**: `for i in range(len(items) - n, len(items) + 1):`
- **After**: `for i in range(len(items) - n, len(items)):`
- **Resolution**: AI identified the off-by-one immediately. Fix was applied directly with no manual edits needed.
- **Lesson Learned**: Always verify that loop upper bounds do not exceed the last valid index. Test edge cases where `n == len(items)`.

---

## Bug Report – bug2.py
- **File**: `bug_snippets/bug2.py`
- **Summary**: Logical error causes the average of positive numbers to be calculated incorrectly.
- **Root Cause**: `count` was assigned `len(numbers)` after the loop, counting all elements including negatives and zeros instead of only positive ones.
- **Before**: `count = len(numbers)`
- **After**: `count += 1` inside `if num > 0` block
- **Resolution**: AI correctly identified that the counter must be incremented conditionally. No manual edits needed.
- **Lesson Learned**: When filtering data before aggregating, ensure that all related variables (sum, count) are updated under the same condition.

---

## Bug Report – bug3.js
- **File**: `bug_snippets/bug3.js`
- **Summary**: Two bugs: incorrect initial value for product and loop boundary error. A third issue involves implicit type coercion during array summation.
- **Root Cause**: `product` was initialized to `0` instead of `1`, making all multiplication results `0`. The loop condition `i <= arr.length` accessed `arr[arr.length]` which is `undefined`. String in mixed array caused `+` to concatenate instead of add.
- **Before**: `let product = 0;` / `i <= arr.length` / `acc + val`
- **After**: `let product = 1;` / `i < arr.length` / `acc + Number(val)`
- **Resolution**: AI identified all three bugs. Manual addition of `Number()` coercion and initial value `0` in `reduce()` was added for extra safety.
- **Lesson Learned**: Always initialize accumulators to their identity value (1 for multiplication, 0 for addition). Never use `<=` with array length. Validate types when mixing data.

---

## Bug Report – bug4.js
- **File**: `bug_snippets/bug4.js`
- **Summary**: Missing `await` keyword causes an unresolved Promise to be used as a user object.
- **Root Cause**: `getUser()` returns a Promise but `printUser()` was not declared `async` and did not `await` the result. Accessing `.name` on a Promise returns `undefined` silently.
- **Before**: `function printUser(id) { const user = getUser(id); ... }`
- **After**: `async function printUser(id) { const user = await getUser(id); ... }`
- **Resolution**: AI identified the missing `async/await` pattern immediately. No manual edits needed.
- **Lesson Learned**: Any function that calls an async function must itself be `async` and must `await` the result. Silent `undefined` returns make async bugs hard to detect without careful testing.

---

## Bug Report – bug5.cpp
- **File**: `bug_snippets/bug5.cpp`
- **Summary**: Two bugs: a missing semicolon prevents compilation, and an incorrect array index causes out-of-bounds memory access during the swap.
- **Root Cause**: Missing `;` after `int size = sizeof(nums) / sizeof(nums[0])` is a syntax error. Using `arr[size - i]` instead of `arr[size - 1 - i]` accesses memory beyond the array boundary on the first swap iteration.
- **Before**: `int size = sizeof(nums) / sizeof(nums[0])` / `arr[size - i]`
- **After**: `int size = sizeof(nums) / sizeof(nums[0]);` / `arr[size - 1 - i]`
- **Resolution**: AI identified both bugs. Fix was applied directly with no manual edits needed.
- **Lesson Learned**: C++ does not protect against out-of-bounds array access. Always use `size - 1 - i` when mirroring array indexes. Enable compiler warnings to catch missing semicolons early.

---

## Bug Report – bug6.py
- **File**: `bug_snippets/bug6.py`
- **Summary**: Two bugs: a `KeyError` when accessing a dictionary key that does not yet exist, and a `TypeError` when passing a float to string repetition.
- **Root Cause**: `freq[word] + 1` fails on the first occurrence of any word because the key has not been initialized. Python's `*` operator for strings requires an integer, but `3.0` (a float) was passed.
- **Before**: `freq[word] = freq[word] + 1` / `return text * times`
- **After**: `freq[word] = freq.get(word, 0) + 1` / `return text * int(times)`
- **Resolution**: AI identified both bugs and suggested `dict.get()` with a default value. Manual addition of `int()` cast was confirmed by testing.
- **Lesson Learned**: Always use `dict.get(key, default)` when building frequency maps. Python is strongly typed — always ensure numeric types match the expected operation.
