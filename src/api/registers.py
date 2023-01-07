"""
Registros da API blueprint do Flask-RESTX.
"""
from src.settings import Settings
from src.utils import Logger
from flask import Blueprint
from flask_restx import Api
from src.api.verify.routes import ns_verify


class Register(Logger):
    """
    Registra APIs para app Flask
    """
    __settings: Settings = Settings()
    __debug_enabled: bool = __settings.debug_is_enabled()
    _api_bp: Blueprint | None = None
    _api: Api | None = None

    def __init__(self):
        Logger.__init__(self, name=self.__class__.__name__)
        self.logger.info("Criado Blueprint")
        self._api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
        self.logger.debug(f"Blueprint -> {self._api_bp}")
        if self._set_api():
            self._set_namespaces()

    def _set_api(self) -> bool:
        """
        Set API com suas configurações
        :return: bool
        """
        if self._api_bp is not None:
            self.logger.info("Set API(RESTX) com configs")
            self._api = Api(
                self._api_bp,
                version='1.0',
                title='Validação de password - API',
                description='Bem vindo a UI documentação da API de validação de password com Swagger.',
                # Se DEBUG está habilitado ele gera interface Swagger 2.0
                doc='/ui' if self.__debug_enabled else False,
                validate=True,
            )
            self.logger.info("Setting init API")
            self.__init_api()
            return True
        return False

    def __init_api(self):
        """
        Set configs especificas para API
        """
        if not self.__debug_enabled:
            self.logger.info("Habilitando specs em env DEBUG(swagger.json)")
            self._api.init_app(self._api_bp, add_specs=False)

    def _set_namespaces(self):
        """
        Set namepaces que a API irá comportar
        """
        self._api.add_namespace(ns_verify, path='/verify')

    def get_blueprint(self) -> Blueprint:
        """
        Get blueprint para APP(Flask)
        :return: Blueprint
        """
        return self._api_bp
