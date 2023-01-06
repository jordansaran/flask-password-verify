"""Configuração do aplicação Flask."""
from typing import Type

from dotenv import load_dotenv
from src.utils import BASE_DIR, Singleton
import os

# Para manipulação de variáveis ambiente.
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))


class Setting(metaclass=Singleton):
    """Set Flask configurações o arquivo .env."""

    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 1)
    FLASK_APP = os.getenv('FLASK_APP')


class SettingTest(metaclass=Singleton):
    """Set Flask configuration from .env file."""
    """""TESTING"""
    TESTING = "testing"

    # General Config
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 1)
    SECRET_KEY = os.getenv("SECRET_KEY", TESTING)
    FLASK_APP = os.getenv('FLASK_APP', "app.py")


def get_config(testing: bool = False) -> Type[SettingTest | Setting]:
    """Retorna o ambiente de configuração para o Flask."""
    return SettingTest if testing else Setting
