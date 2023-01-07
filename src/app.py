"""
Criação da aplicaçãoFlask
"""
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from src.api.registers import Register
from src.settings import Settings
from src.utils import Logger


class App(Logger):

    __PORT: int = 5001
    __APP_NAME: str = 'api'
    __app_settings: Settings
    __app: Flask

    def __init__(self):
        Logger.__init__(self, name=self.__class__.__name__)
        self.__app = Flask(self.__APP_NAME)
        self.__app_settings = Settings()
        self.__create_app()

    def __create_app(self):
        """"
        Criação da aplicação para deploy, testing ou production
        """
        self.__app.wsgi_app = ProxyFix(self.__app.wsgi_app)
        self.__app.config.from_object(self.__app_settings)
        # Para o ambiente deploy permitir a criação do Swagger
        self.__app.register_blueprint(Register().get_blueprint())

    def run(self):
        if self.__app_settings.debug_is_enabled():
            self.__app.run(host="0.0.0.0", debug=self.__app_settings.debug_is_enabled(),
                           port=self.__PORT)
        else:
            self.__app.run(host="0.0.0.0", port=self.__PORT)
