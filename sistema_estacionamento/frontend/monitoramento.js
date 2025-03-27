const API_VAGAS = "http://localhost:8000/vagas";

// Função para atualizar o status das vagas em tempo real
async function atualizarVagas() {
    const response = await fetch(API_VAGAS);
    const dados = await response.json();

    document.getElementById("vagas-disponiveis").textContent = dados.vagas_disponiveis;
    document.getElementById("vagas-ocupadas").textContent = dados.vagas_ocupadas;

    const mapa = document.getElementById("mapa-estacionamento");
    mapa.innerHTML = "";

    for (let i = 1; i <= dados.total_vagas; i++) {
        const vaga = document.createElement("div");
        vaga.classList.add("vaga");
        vaga.textContent = `Vaga ${i}`;

        if (dados.vagas_ocupadas_lista.includes(i)) {
            vaga.classList.add("ocupada");
        } else {
            vaga.classList.add("disponivel");
        }

        mapa.appendChild(vaga);
    }
}

// Atualizar a cada 5 segundos
setInterval(atualizarVagas, 5000);
document.addEventListener("DOMContentLoaded", atualizarVagas);
