async function getUserInfo(userId) {
    const response = await fetch(`https://api.example.com/users/${userId}`)

    const data = response.json()

    const result = {
        name: data.name,
        email: data.email,
    }

    return result
}

async function printUsers(ids) {
    for (id in ids) {
        const info = getUserInfo(id)
        if (info !== null) {
            console.log(`User: ${info.name}, Email: ${info.email}`)
        }
    }
}

printUsers([1, 2, 3])