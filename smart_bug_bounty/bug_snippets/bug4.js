// bug4.js
// Intended behavior: Create 5 buttons. When each button is clicked,
// it should alert its own index (0 through 4).

function createButtons() {
    for (var i = 0; i < 5; i++) {         // BUG: `var` is function-scoped, not block-scoped
                                           // all closures share the same `i`
        const btn = document.createElement("button")
        btn.textContent = `Button ${i}`
        btn.addEventListener("click", function () {
            alert(`You clicked button ${i}`) // BUG: always alerts 5 (final value of i)
        })
        document.body.appendChild(btn)
    }
}

// Intended fix: use `let` instead of `var`, or wrap in an IIFE.

function sumArray(arr) {
    let total = 0
    arr.forEach(function(num) {
        total =+ num    // BUG: `=+` is assignment of unary plus, not `+=`
                        // resets total to +num each iteration
    })
    return total
}

createButtons()
console.log(sumArray([1, 2, 3, 4, 5]))  // expected: 15, actual: 5
