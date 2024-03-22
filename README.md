# Agradecimentos e observações
Primeiro quero agradecer muito pela oportunidade!!!!
Caso queira ler esse arquivo formatado corretamente, o projeto se encontra no GitHUB
[Link](https://github.com/01Dri/ProjetoEstagio)

# Projeto de Cadastro de Produtos
O projeto consiste em duas partes distintas: o front-end e o back-end.

## Front-end
No front-end, foram utilizadas as seguintes tecnologias:

- HTML
- CSS
- JavaScript puro

## Back-end
No back-end, foram utilizadas as seguintes tecnologias:

- Python
- FastAPI (Framework para criação de APIs/Rest com Python)
- SQLITE3 (Banco de dados SQL)

## Modelo do Banco de Dados
O banco de dados possui apenas uma tabela, com o seguinte modelo:

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    value REAL NOT NULL,
    isAvailable BOOLEAN NOT NULL

)
```
![Ilustração](https://i.ibb.co/QkXvrbF/Screenshot-from-2024-03-22-19-27-06.png)

## Fluxo do projeto
Preparei um diagrama simples que pode ilustrar o fluxo de processamento do projeto.

![Fluxo](https://i.ibb.co/d4Tx1nh/Screenshot-from-2024-03-22-19-51-20.png)

## Como Iniciar

### LINUX
Para inicializar a aplicação no Linux, basta seguir os comandos abaixo:

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

### WINDOWS
Para inicializar a aplicação no Windows, você primeiro precisará instalar o Python em sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
Após a instalação, basta rodar o comando abaixo:

```bash
install_dependencies.bat
```

## Endpoints

O projeto possui 4 endpoints principais, sendo 2 para o frontend e 2 para o backend, conforme descrito abaixo:

- **Interface de Cadastro de Produtos (Frontend) (GET):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interface de Listagem de Produtos (Frontend) (GET):** [http://127.0.0.1:8000/listagem](http://127.0.0.1:8000/listagem)
- **Endpoint para Retornar os Produtos em JSON (Backend) (GET):** [http://127.0.0.1:8000/products](http://127.0.0.1:8000/products)
- **Endpoint para Salvar os Produtos (Backend) (POST):** [http://127.0.0.1:8000/products/save](http://127.0.0.1:8000/products/save)


