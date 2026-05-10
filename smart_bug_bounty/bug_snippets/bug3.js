// bug3.js
// Intended behavior: Fetch user data from an API, extract the name and email
// fields, and return them as an object. If the request fails, return null.

async function getUserInfo(userId) {
    const response = await fetch(`https://api.example.com/users/${userId}`)

    // BUG: missing check for response.ok — a 404 or 500 still "succeeds" here
    const data = response.json()   // BUG: missing await; data is a Promise, not the parsed object

    const result = {
        name: data.name,           // BUG: data is a Promise, so data.name === undefined
        email: data.email,
    }

    return result
}

async function printUsers(ids) {
    for (id in ids) {              // BUG: `for...in` on an array gives string indices "0","1",...
                                   //      should be `for (const id of ids)`
        const info = getUserInfo(id)   // BUG: missing await; info is a Promise
        if (info !== null) {
            console.log(`User: ${info.name}, Email: ${info.email}`)
        }
    }
}

printUsers([1, 2, 3])
