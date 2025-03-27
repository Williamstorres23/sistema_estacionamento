async function carregarRelatorioFinanceiro() {
    const response = await fetch("http://localhost:8000/reports/financeiro/");
    const dados = await response.json();

    document.getElementById("total-receita").textContent = dados.total_receita.toFixed(2);

    const lista = document.getElementById("lista-pagamentos");
    lista.innerHTML = "";

    for (const metodo in dados.pagamentos_por_metodo) {
        const item = document.createElement("li");
        item.textContent = `${metodo}: R$ ${dados.pagamentos_por_metodo[metodo].toFixed(2)}`;
        lista.appendChild(item);
    }
}

document.addEventListener("DOMContentLoaded", carregarRelatorioFinanceiro);
