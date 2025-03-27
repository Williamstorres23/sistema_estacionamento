const API_RESERVAS = "http://localhost:8000/reservas";

// Registrar uma nova reserva
document.getElementById("form-reserva").addEventListener("submit", async (event) => {
    event.preventDefault();

    const nome = document.getElementById("cliente-nome").value;
    const placa = document.getElementById("placa-veiculo").value;
    const data = document.getElementById("data-reserva").value;

    const response = await fetch(`${API_RESERVAS}/nova`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, placa, data })
    });

    if (response.ok) {
        alert("Reserva realizada com sucesso!");
        carregarReservas();
    } else {
        alert("Erro ao realizar reserva.");
    }
});

// Carregar reservas ativas
async function carregarReservas() {
    const response = await fetch(`${API_RESERVAS}/ativas`);
    const reservas = await response.json();

    const lista = document.getElementById("lista-reservas");
    lista.innerHTML = "";

    reservas.forEach(reserva => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${reserva.nome}</td>
            <td>${reserva.placa}</td>
            <td>${reserva.data}</td>
            <td><button onclick="cancelarReserva('${reserva.placa}')">Cancelar</button></td>
        `;
        lista.appendChild(row);
    });
}

// Cancelar reserva
async function cancelarReserva(placa) {
    const response = await fetch(`${API_RESERVAS}/cancelar/${placa}`, { method: "DELETE" });

    if (response.ok) {
        alert("Reserva cancelada.");
        carregarReservas();
    } else {
        alert("Erro ao cancelar reserva.");
    }
}

// Atualizar reservas ao carregar a página
document.addEventListener("DOMContentLoaded", carregarReservas);
