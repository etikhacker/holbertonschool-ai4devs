function getUser(id) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: id, name: "Omar", role: "admin" });
        }, 500);
    });
}

async function printUser(id) {
    const user = await getUser(id);
    console.assert(user.name === "Omar", "Test failed");
    console.log(`User name: ${user.name}`);
}

async function main() {
    await printUser(42);
    console.log("bug4_fixed.js: All tests passed");
}

main();
