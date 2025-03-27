# Sistema de Estacionamento

Este é um sistema de gerenciamento de estacionamento, desenvolvido para gerenciar o controle de vagas, entradas e saídas de veículos em um estacionamento. Ele foi projetado para otimizar o controle de vagas, calcular valores de permanência e gerar relatórios das atividades diárias.

## Funcionalidades

- **Controle de Vagas**: Gerenciamento do número de vagas ocupadas e disponíveis.
- **Entrada e Saída de Veículos**: Registra o momento de entrada e saída dos veículos.
- **Cálculo de Tarifa**: Calcula o valor a ser pago com base no tempo de permanência do veículo.
- **Relatórios**: Geração de relatórios diários de entradas, saídas e valores arrecadados.
- **Gerenciamento de Veículos**: Cadastra informações sobre os veículos que entram no estacionamento (placa, modelo, etc.).

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Banco de Dados**: SQLite 
- **Interface**: Console 
- **Bibliotecas**: 
  - `datetime` para controle de tempo
  - `sqlite3` para interação com o banco de dados

## Como Rodar

### Requisitos

Antes de executar o sistema, certifique-se de ter o Python 3.x instalado em seu computador.

1. Clone este repositório:
   ```bash
   git clone https://github.com/Williamstorres23/sistema_estacionamento.git
   cd sistema-estacionamento
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o sistema:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

- `main.py`: Arquivo principal que executa o sistema.
- `models.py`: Define as classes e interações com o banco de dados.
- `controllers.py`: Contém a lógica de controle das funcionalidades do sistema.
- `reports.py`: Geração de relatórios do estacionamento.
- `requirements.txt`: Lista de dependências do projeto.

## Exemplo de Uso

### Cadastrar Veículo

Ao registrar a entrada de um veículo, forneça as informações como placa e modelo:

```bash
Informe a placa do veículo: ABC1234
Informe o modelo do veículo: Honda Civic
```

### Gerar Relatório

Para gerar um relatório de movimentações, execute a função de relatório:

```bash
Informe a data para o relatório: 2025-03-25
```

## Contribuições

Sinta-se à vontade para contribuir para o projeto! Se você encontrar bugs ou tiver sugestões de melhorias, crie uma *issue* ou envie um *pull request*.

## Licença

Projeto feito por Wesley Santos e Williams Torres

```
