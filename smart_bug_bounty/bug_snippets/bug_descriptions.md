# Bug Descriptions

## bug1.py
- **Intended Behavior**: Binary search — return the index of `target` in a sorted list, or `-1` if not found.
- **Current Issue**: `high = len(arr)` causes off-by-one; `(low + high) / 2` uses float division instead of `//`; `while low < high` misses the equal-boundary check.

## bug2.js
- **Intended Behavior**: Fetch user data by ID from an API and return `{ name, email }`, or `null` on failure.
- **Current Issue**: Missing `await` before `response.json()` so `data` is a Promise; `for (id in ids)` iterates over indices not values; missing `await` before `getUserInfo(id)`.

## bug3.java
- **Intended Behavior**: A singly linked list with `append`, `printList`, and `length` methods.
- **Current Issue**: `while (current != null);` in `length()` has a rogue semicolon that creates an infinite loop; `printList()` prints digits with no separator.

## bug4.py
- **Intended Behavior**: A `Stack` class supporting `push`, `pop`, `peek`, `is_empty`, `size`, and `clear`.
- **Current Issue**: `len(self.items - 1)` in `size()` raises `TypeError`; `self.items == []` in `clear()` uses comparison instead of assignment so the stack is never cleared.

## bug5.js
- **Intended Behavior**: Create 5 buttons each alerting their own index; `sumArray` returns the sum of a numeric array.
- **Current Issue**: `var i` in the loop is function-scoped so all handlers alert `5`; `total =+ num` resets total to `+num` each iteration instead of accumulating.

## bug6.java
- **Intended Behavior**: Return `true` if a string is a palindrome, ignoring case and non-alphanumeric characters.
- **Current Issue**: `right = cleaned.length()` is out of bounds by 1 (should be `length() - 1`); `right++` moves the pointer outward instead of inward (`right--`); regex strips digits that should be kept.