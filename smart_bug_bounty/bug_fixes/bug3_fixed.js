function productOfArray(arr) {
    let product = 1;
    for (let i = 0; i < arr.length; i++) {
        product *= arr[i];
    }
    return product;
}

function sumItems(items) {
    return items.reduce((acc, val) => acc + Number(val), 0);
}

function main() {
    console.assert(productOfArray([2, 3, 4, 5]) === 120, "Test 1 failed");
    console.assert(sumItems([1, "2", 3]) === 6, "Test 2 failed");
    console.assert(productOfArray([1]) === 1, "Test 3 failed");
    console.log("bug3_fixed.js: All tests passed");
}

main();
