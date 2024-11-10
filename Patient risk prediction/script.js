document.getElementById("healthForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Capture user inputs
    const age = document.getElementById("age").value;
    const sex = document.getElementById("sex").value;
    const cp = document.getElementById("cp").value;
    const trestbps = document.getElementById("trestbps").value;
    const chol = document.getElementById("chol").value;

    // Basic input validation
    if (!age || !sex || cp === "" || !trestbps || !chol) {
        document.getElementById("result").innerText = "Please fill in all fields.";
        return;
    }

    // Prepare the data payload
    const payload = { age, sex, cp, trestbps, chol };

    try {
        // Send data to backend
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorData = await response.json();
            document.getElementById("result").innerText = `Error: ${errorData.error}`;
            return;
        }

        // Process the response
        const result = await response.json();
        document.getElementById("result").innerText = `Predicted Heart Health Risk: ${result.risk_level}`;
    } catch (error) {
        document.getElementById("result").innerText = `Error: ${error.message}`;
    }
});
