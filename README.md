# 📦 Catálogo de Produtos com Streamlit + Azure Blob Storage

Este projeto foi desenvolvido como parte do desafio da DIO - Microsoft Application Platform. A proposta foi criar um sistema funcional de cadastro e exibição de produtos utilizando **Streamlit**, **Azure Blob Storage** para armazenar imagens e **SQL Server** para gerenciar os dados dos produtos.

---

## 🚀 Funcionalidades

- 📥 Cadastro de novos produtos com nome, descrição, preço e imagem
- 🖼️ Armazenamento de imagens no Azure Blob Storage
- 🗃️ Armazenamento de dados em banco SQL Server via pyodbc
- 🧾 Listagem visual dos produtos cadastrados em cards organizados em colunas

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Azure Blob Storage
- SQL Server
- PyODBC
- dotenv (para segurança nas variáveis de ambiente)

---

## 🧠 Aprendizados e Insights
Utilização real de serviços em nuvem (Azure) integrados com Python

Estruturação de um sistema simples de cadastro com visual moderno

Uso de uuid para evitar conflitos em nomes de arquivos

Implementação de boas práticas com feedback visual para o usuário (mensagens de sucesso e erro)

## 🎯 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/alx-8914/catalogo-produtos-streamlit.git
   cd catalogo-produtos-streamlit

2. Execute a aplicação:

   ```bash
      streamlit run main.py

📸 Prints do Projeto:
   <div class=align-item=left'>
      <p>Tela Inicial</p>
      <img src="Captura de tela 2025-04-21 004833.png" width="300" height="250">
      <p>Tela de sucesso com efeito Balões</p>
      <img src="Cadastro sucess.png" width="500" height="250">
      <p>Lista dos Produtos</p>
      <img src="lista ok.png" width="500" height="250">   
   </div>
  

<br>
 👨‍💻 Autor
Alexsandro da Silva
