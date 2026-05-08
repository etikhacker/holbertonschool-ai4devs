function productOfArray(arr) {
    let product = 0;
    for (let i = 0; i <= arr.length; i++) {
        product *= arr[i];
    }
    return product;
}

function sumItems(items) {
    return items.reduce((acc, val) => acc + val);
}

const nums = [2, 3, 4, 5];
console.log(productOfArray(nums));

const mixed = [1, "2", 3];
console.log(sumItems(mixed));