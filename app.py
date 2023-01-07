"""
Executa aplicação Flask
OBS: Este arquivo serve de referência para o arquivo .env
"""
from src.app import App

if __name__ == "__main__":
    app = App()
    app.run()
