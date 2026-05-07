// Bug 4 – bug4.js
// Intended: Fetch user data and print the username.

function getUser(id) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ id: id, name: "Omar", role: "admin" });
    }, 500);
  });
}

function printUser(id) {
  const user = getUser(id);   // BUG: missing await — user is a Promise object, not the resolved value
  console.log(`User name: ${user.name}`);  // Prints: undefined
}

// Correct version would be:
// async function printUser(id) {
//   const user = await getUser(id);
//   console.log(`User name: ${user.name}`);
// }

printUser(42);
// Expected: User name: Omar
// Actual:   User name: undefined