#!/bin/bash

# Instalação das dependências
echo "Instalando as dependências..."
sudo apt update
pip install fastapi uvicorn

# Iniciar o servidor FastAPI em segundo plano
echo "Iniciando o servidor..."
uvicorn main:app --reload &

# Mensagem indicando que o servidor foi iniciado
echo "O servidor FastAPI foi iniciado. Você pode acessar em http://localhost:8000"

# Script concluído
echo "Script concluído."
