function getUser(id) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: id, name: "Omar", role: "admin" });
        }, 500);
    });
}

function printUser(id) {
    const user = getUser(id);
    console.log(`User name: ${user.name}`);
}

function main() {
    printUser(42);
    printUser(99);
}

main();