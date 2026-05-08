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
    const nums = [2, 3, 4, 5];
    console.assert(productOfArray(nums) === 120, "Test 1 failed");

    const mixed = [1, "2", 3];
    console.assert(sumItems(mixed) === 6, "Test 2 failed");

    console.log("bug3_fixed.js: All tests passed");
}

main();
