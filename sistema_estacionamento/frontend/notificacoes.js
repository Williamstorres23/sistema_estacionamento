document.getElementById("form-notificacao").addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const placa = document.getElementById("placa").value;
    const tempo = document.getElementById("tempo").value;

    const response = await fetch("http://localhost:8000/notifications/notificar-tempo-excedido/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, placa, tempo })
    });

    const resultado = await response.json();
    document.getElementById("mensagem").textContent = resultado.status;
});
