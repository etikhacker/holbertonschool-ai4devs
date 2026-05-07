FILE: bug1.py

Bug 1 – bug1.py

Intended behavior:
Return the last n items from a list.

Issue type:
Off-by-one error / IndexError

Explanation:
The loop uses len(items) + 1, which causes the code to access
items[len(items)], an invalid index. This produces an IndexError.

Fix:
Change:
for i in range(len(items) - n, len(items) + 1)

To:
for i in range(len(items) - n, len(items))


FILE: bug2.py

Bug 2 – bug2.py

Intended behavior:
Calculate the average of all positive numbers in a list.

Issue type:
Logical error

Explanation:
The variable count is assigned len(numbers), which counts all
elements in the list instead of only positive numbers.
This gives an incorrect average.

Fix:
Change:
count = len(numbers)

To:
count += 1


FILE: bug3.js

Bug 3 – bug3.js

Intended behavior:
Multiply every number in an array and return the product.

Issue type:
Incorrect initialization and out-of-bounds loop

Explanation:
The product variable starts at 0, but multiplication should start
with 1 because 1 is the identity value for multiplication.

The loop condition uses <= arr.length, which accesses an undefined
element at the end of the array.

Fix:
Change:
let product = 0;

To:
let product = 1;

Change:
for (let i = 0; i <= arr.length; i++)

To:
for (let i = 0; i < arr.length; i++)

Also change:
product = arr[i];

To:
product *= arr[i];


Second Bug – Type Misuse

Intended behavior:
Sum all items in an array numerically.

Issue type:
Type coercion / String concatenation

Explanation:
The array contains a string value ("2"), so JavaScript performs
string concatenation instead of numeric addition.

Fix:
Convert values to numbers before addition:
return items.reduce((acc, val) => acc + Number(val), 0);


FILE: bug4.js

Bug 4 – bug4.js

Intended behavior:
Fetch user data and print the username.

Issue type:
Missing await in asynchronous code

Explanation:
getUser(id) returns a Promise, but the code tries to access
user.name before the Promise is resolved.
As a result, undefined is printed.

Fix:
Use async/await:

async function printUser(id) {
    const user = await getUser(id);
    console.log(`User name: ${user.name}`);
}


FILE: bug5.cpp

Bug 5 – bug5.cpp

Intended behavior:
Reverse an array in-place and print it.

Issue type:
Off-by-one error and syntax error

Explanation:
The code accesses arr[size - i], which is outside the valid array
range. Array indices go from 0 to size - 1.

There is also a missing semicolon after calculating the array size,
which causes a compilation error.

Fix:
Change:
arr[i] = arr[size - i];

To:
arr[i] = arr[size - 1 - i];

Change:
arr[size - i] = temp;

To:
arr[size - 1 - i] = temp;

Add missing semicolon:
int size = sizeof(nums) / sizeof(nums[0]);


FILE: bug6.py

Bug 6 – bug6.py

Intended behavior:
Count word frequency in a sentence and return the top-N words.

Issue type:
KeyError and TypeError

Explanation:
The line:
freq[word] = freq[word] + 1

causes a KeyError when a word appears for the first time because
the dictionary key does not yet exist.

The second bug happens because string multiplication expects an
integer, but a float value is passed instead.

Fix:
Change:
freq[word] = freq[word] + 1

To:
freq[word] = freq.get(word, 0) + 1

Also change:
times = 3.0

To:
times = 3