# Bug Descriptions

## bug1.py
- **Intended Behavior**: Binary search — return the index of `target` in a sorted list, or `-1` if not found.
- **Current Issues**:
  1. `high = len(arr)` — off-by-one; should be `len(arr) - 1`, otherwise the last element is never reachable.
  2. `while low < high` — should be `low <= high` so a single-element array is checked correctly.
  3. `mid = (low + high) / 2` — float division in Python 3; should use `//` for integer index.

---

## bug2.py
- **Intended Behavior**: A `Stack` class supporting `push`, `pop`, `peek`, `is_empty`, `size`, and `clear`.
- **Current Issues**:
  1. `len(self.items - 1)` in `size()` — subtracting an integer from a list raises `TypeError`; should be `len(self.items)`.
  2. `self.items == []` in `clear()` — comparison operator `==` instead of assignment `=`; the list is never actually cleared.

---

## bug3.js
- **Intended Behavior**: Async function that fetches user data by ID from an API and returns `{ name, email }`, or `null` on failure.
- **Current Issues**:
  1. Missing `response.ok` check — HTTP errors (404, 500) are not detected and execution continues with invalid data.
  2. `response.json()` missing `await` — `data` is a `Promise` object, so `data.name` and `data.email` are both `undefined`.
  3. `for (id in ids)` — iterates over array **indices** as strings (`"0"`, `"1"`, …) instead of values; should be `for (const id of ids)`.
  4. `getUserInfo(id)` missing `await` inside `printUsers` — `info` is always a `Promise`, never `null`, so the null-check is useless.

---

## bug4.js
- **Intended Behavior**: Create 5 buttons that each alert their own index when clicked; a helper `sumArray` correctly sums a numeric array.
- **Current Issues**:
  1. `var i` in the `for` loop — `var` is function-scoped, so all click handlers close over the same final value (`5`); should use `let`.
  2. `total =+ num` inside `forEach` — unary `+` operator resets `total` to `+num` on every iteration instead of accumulating; should be `total += num`.

---

## bug5.java
- **Intended Behavior**: A singly linked list with `append`, `delete` (by value), `printList`, and `length` methods.
- **Current Issues**:
  1. `while (current != null);` in `length()` — the semicolon terminates the loop body immediately, creating an infinite loop; the block `{ count++; current = current.next; }` is unreachable.
  2. `System.out.print(current.data)` in `printList()` — no separator printed between nodes; output is a run-on string like `1234` instead of `1 -> 2 -> 3 -> 4 -> null`.
  3. `delete()` silently does nothing when the value is not found — no exception or return signal to the caller.

---

## bug6.java
- **Intended Behavior**: Return `true` if a string is a palindrome, ignoring case and non-alphanumeric characters (e.g. `"A man, a plan, a canal: Panama"` → `true`).
- **Current Issues**:
  1. `replaceAll("[^a-zA-Z]", "")` — strips digits too; pattern should be `[^a-zA-Z0-9]` to keep alphanumeric characters.
  2. `int right = cleaned.length()` — index is out of bounds by 1; should be `cleaned.length() - 1`.
  3. `right++` in the while loop — moves the right pointer **outward** instead of inward; should be `right--`, causing an `StringIndexOutOfBoundsException` immediately.
