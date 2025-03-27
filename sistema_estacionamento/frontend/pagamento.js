document.getElementById("form-pagamento").addEventListener("submit", async function (event) {
    event.preventDefault();

    const client_id = document.getElementById("client_id").value;
    const vehicle_id = document.getElementById("vehicle_id").value;
    const amount = document.getElementById("amount").value;
    const payment_method = document.getElementById("payment_method").value;

    const response = await fetch("http://localhost:8000/payments/processar/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ client_id, vehicle_id, amount, payment_method })
    });

    const resultado = await response.json();
    document.getElementById("mensagem").textContent = resultado.status;
});
