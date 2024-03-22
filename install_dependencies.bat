@echo off

rem Instalação das dependências
echo Instalando as dependências...
pip install fastapi uvicorn

rem Iniciar o servidor FastAPI
echo Iniciando o servidor...
uvicorn main:app --reload
