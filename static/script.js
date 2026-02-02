async function createUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    
    const response = await fetch("/api/users", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email})
    });
    
    const data = await response.json();
    document.getElementById("result").textContent = 
        JSON.stringify(data, null, 2);
    
    // Clear inputs
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
}

async function getUsers() {
    const response = await fetch("/api/users");
    const data = await response.json();
    document.getElementById("result").textContent = 
        JSON.stringify(data, null, 2);
}

// Load users on page load
getUsers();