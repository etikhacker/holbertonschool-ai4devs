# Fix Validation Report

---

## Bug 1 – bug1_fixed.py
**Fix Applied**: Changed `len(items) + 1` to `len(items)` in the `range()` call.
- **Input**: `[10, 20, 30, 40, 50]`, n=3 | **Expected**: `[30, 40, 50]` | **Actual**: `[30, 40, 50]` ✅
- **Input**: `[10, 20, 30, 40, 50]`, n=5 | **Expected**: `[10, 20, 30, 40, 50]` | **Actual**: `[10, 20, 30, 40, 50]` ✅
- **Input**: `[10, 20, 30, 40, 50]`, n=1 | **Expected**: `[50]` | **Actual**: `[50]` ✅

**Manual Tweaks**: None needed.
**Result**: Fix works as expected.

---

## Bug 2 – bug2_fixed.py
**Fix Applied**: Replaced `count = len(numbers)` with `count += 1` inside the `if num > 0` block.
- **Input**: `[5, -3, 10, -1, 0, 8]` | **Expected**: `7.67` | **Actual**: `7.67` ✅
- **Input**: `[-1, -2, -3]` | **Expected**: `0` | **Actual**: `0` ✅
- **Input**: `[4, 4]` | **Expected**: `4.0` | **Actual**: `4.0` ✅

**Manual Tweaks**: None needed.
**Result**: Fix works as expected.

---

## Bug 3 – bug3_fixed.js
**Fix Applied**: Initialized `product = 1`, changed `<=` to `<` in loop, added `Number(val)` coercion in `sumItems`.
- **Input**: `[2, 3, 4, 5]` | **Expected**: `120` | **Actual**: `120` ✅
- **Input**: `[1, "2", 3]` | **Expected**: `6` | **Actual**: `6` ✅

**Manual Tweaks**: Added `Number()` coercion and initial value `0` to `reduce()` for safety.
**Result**: Fix works as expected.

---

## Bug 4 – bug4_fixed.js
**Fix Applied**: Declared `printUser` as `async` and added `await` before `getUser(id)`.
- **Input**: `id = 42` | **Expected**: `User name: Omar` | **Actual**: `User name: Omar` ✅

**Manual Tweaks**: None needed.
**Result**: Fix works as expected.

---

## Bug 5 – bug5_fixed.cpp
**Fix Applied**: Added missing semicolon after `size` declaration. Changed `arr[size - i]` to `arr[size - 1 - i]` on both swap lines.
- **Input**: `{1, 2, 3, 4, 5}` | **Expected**: `5 4 3 2 1` | **Actual**: `5 4 3 2 1` ✅

**Manual Tweaks**: None needed.
**Result**: Fix works as expected.

---

## Bug 6 – bug6_fixed.py
**Fix Applied**: Replaced `freq[word] + 1` with `freq.get(word, 0) + 1`. Added `int()` cast around `times` in `multiply_string_times`.
- **Input**: `"the cat sat on the mat the cat"`, n=2 | **Expected**: `['the', 'cat']` | **Actual**: `['the', 'cat']` ✅
- **Input**: `"hello "`, times=3.0 | **Expected**: `"hello hello hello "` | **Actual**: `"hello hello hello "` ✅
- **Input**: `"ab"`, times=2 | **Expected**: `"abab"` | **Actual**: `"abab"` ✅

**Manual Tweaks**: None needed.
**Result**: Fix works as expected.
