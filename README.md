# 💱 Cotação de Moedas com Python e MySQL

Este é um projeto em Python que consulta a cotação atual de moedas (como **Dólar**, **Euro** e **Bitcoin**) usando a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) e armazena essas informações em um banco de dados **MySQL**.

---

## 📌 Funcionalidades

- Consulta de cotações em tempo real (USD-BRL, EUR-BRL, BTC-BRL)
- Armazenamento das cotações no banco MySQL com data e hora
- Menu simples via terminal para executar as ações
- Código estruturado em módulos (organização por pastas)

---

## 🛠 Tecnologias utilizadas

- Python 3.x
- MySQL
- Biblioteca `requests`
- Biblioteca `mysql-connector-python`
- API pública [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)

---

## 📁 Estrutura do Projeto

cotacao_moedas/
├── config/
│ └── db_config.py # Configuração da conexão com o MySQL
├── services/
│ └── cotacao_service.py # Funções para buscar e salvar cotações
├── database/
│ └── schema.sql # Script SQL para criar banco e tabela
├── main.py # Menu principal via terminal
├── requirements.txt # Dependências do projeto
└── README.md # Documentação



---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```
git clone https://github.com/gleydson-silv/cotacao_de_moedas.git
cd cotacao_de_moedas
2. Configure o banco de dados MySQL
Acesse o phpMyAdmin ou seu cliente MySQL

Execute o conteúdo de database/schema.sql:

CREATE DATABASE IF NOT EXISTS cotacoes_db;

USE cotacoes_db;

CREATE TABLE IF NOT EXISTS cotacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    moeda VARCHAR(10) NOT NULL,
    valor DECIMAL(15, 6) NOT NULL,
    data_hora DATETIME NOT NULL
);

```

---
3. Instale as dependências
pip install -r requirements.txt

4. Execute o programa
python main.py
💡 Exemplo de uso no terminal

---
=== COTAÇÃO DE MOEDAS ===
1 - Buscar e salvar cotações
0 - Sair

---
🔒 .gitignore recomendado
gitignore
Copiar
Editar
__pycache__/
*.pyc
*.pyo
.env
*.log

---
📄 Licença
Este projeto é de uso livre para fins de estudo.
Desenvolvido por Gleydson Luidy