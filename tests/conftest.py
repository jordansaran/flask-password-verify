import pytest

from src.app import App


@pytest.fixture
def app():
    """""Criando e configurando um nova instancia doo app para cada test."""
    app = App().get_app()
    yield app


@pytest.fixture
def client(app):
    """Um client test para o app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Um test runner para o comandos click do app."""
    return app.test_cli_runner()
