// Bug 3 – bug3.js
// Intended: Multiply every number in an array and return the product.

function productOfArray(arr) {
  let product = 0;  // BUG: should be 1 (identity for multiplication)

  for (let i = 0; i <= arr.length; i++) {   // BUG: <= causes out-of-bounds (undefined * n = NaN)
    product *= arr[i];
  }

  return product;
}

// Test
const nums = [2, 3, 4, 5];
console.log(productOfArray(nums));
// Expected: 120
// Actual:   0  (because 0 * anything = 0, and last iteration gives NaN)

// Second scenario – type misuse
function sumItems(items) {
  return items.reduce((acc, val) => acc + val);
}

const mixed = [1, "2", 3];
console.log(sumItems(mixed));
// Expected: 6
// Actual:   "12" + 3 = "123"  ← string concatenation instead of addition