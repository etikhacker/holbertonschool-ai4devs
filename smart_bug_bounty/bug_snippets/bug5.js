function createButtons() {
    for (var i = 0; i < 5; i++) {
        const btn = document.createElement("button")
        btn.textContent = `Button ${i}`
        btn.addEventListener("click", function () {
            alert(`You clicked button ${i}`)
        })
        document.body.appendChild(btn)
    }
}

function sumArray(arr) {
    let total = 0
    arr.forEach(function(num) {
        total =+ num
    })
    return total
}

createButtons()
console.log(sumArray([1, 2, 3, 4, 5]))