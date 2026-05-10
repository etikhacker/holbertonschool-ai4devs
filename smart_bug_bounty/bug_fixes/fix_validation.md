# Fix Validation

## bug1.py
- **Original Issue**: Off-by-one error in range() upper bound causing IndexError
- **Fix Applied**: Changed `len(items) + 1` to `len(items)` in the range() call
- **Test Results**: All 3 test cases passed ✅
  - `get_last_n([10,20,30,40,50], 3)` → `[30, 40, 50]`
  - `get_last_n([10,20,30,40,50], 5)` → `[10, 20, 30, 40, 50]`
  - `get_last_n([10,20,30,40,50], 1)` → `[50]`

## bug2.py
- **Original Issue**: Logical error — count used len(numbers) instead of counting only positives
- **Fix Applied**: Moved `count += 1` inside the `if num > 0` block
- **Test Results**: All 3 test cases passed ✅
  - `average_positives([5, -3, 10, -1, 0, 8])` → `7.67`
  - `average_positives([-1, -2, -3])` → `0`
  - `average_positives([4, 4])` → `4.0`

## bug3.js
- **Original Issue**: product initialized to 0, loop out-of-bounds, type coercion in sumItems
- **Fix Applied**: Set `product = 1`, changed `<=` to `<`, added `Number(val)` in reduce
- **Test Results**: All 3 test cases passed ✅
  - `productOfArray([2, 3, 4, 5])` → `120`
  - `sumItems([1, "2", 3])` → `6`
  - `productOfArray([1])` → `1`

## bug4.js
- **Original Issue**: Missing await caused user to hold unresolved Promise
- **Fix Applied**: Added `async` to printUser and `await` before getUser(id)
- **Test Results**: All test cases passed ✅
  - `printUser(42)` → `User name: Omar`
  - `printUser(99)` → `User name: Omar`

## bug5.java
- **Original Issue**: Loop used `<=` causing ArrayIndexOutOfBoundsException; repeatString started at i=1
- **Fix Applied**: Changed `i <= arr.length` to `i < arr.length`; changed `i = 1` to `i = 0`
- **Test Results**: All 4 test cases passed ✅
  - `sumArray([1,2,3,4,5])` → `15`
  - `sumArray([])` → `0`
  - `repeatString("hello ", 3)` → `"hello hello hello "`
  - `repeatString("ab", 2)` → `"abab"`

## bug6.py
- **Original Issue**: KeyError on first word occurrence; TypeError from float passed to string repetition
- **Fix Applied**: Used `freq.get(word, 0) + 1`; added `int()` cast in multiply_string_times
- **Test Results**: All 3 test cases passed ✅
  - `top_n_words("the cat sat on the mat the cat", 2)` → `['the', 'cat']`
  - `multiply_string_times("hello ", 3.0)` → `"hello hello hello "`
  - `multiply_string_times("ab", 2)` → `"abab"`
