async function checkAPI() {
    const box = document.getElementById("apiResponse");
    box.innerHTML = "Connecting to backend...";

    try {
        const res = await fetch("http://localhost:5000/");
        const text = await res.text();
        box.innerHTML = "Backend Response: " + text;
    } catch (error) {
        box.innerHTML = "❌ Backend not reachable (Prasad & Tarun will fix it 😎)";
    }
}
