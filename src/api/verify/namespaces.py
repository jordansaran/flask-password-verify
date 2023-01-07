from flask_restx import Namespace

from src.api.verify.models import MdMatch, MdRule, MdVerify
from src.utils import Logger


class NsVerify(Logger):
    """
    Namespace Verify
    Contém o objeto namespace e seus respectivos modelos
    """

    __ns: Namespace

    def __init__(self):
        Logger.__init__(self, name=self.__class__.__name__)
        self.logger.info("Namespace verify criado com sucesso.")
        self.__ns = Namespace(name='verify', validate=True)
        self.__set_models()

    def get_namespace(self):
        self.logger.info(f"get objeto namespace {self.__class__.__name__}")
        return self.__ns

    def __set_models(self):
        self.logger.info(f"Setting models no ns({self.__class__.__name__})")
        list_models = [MdMatch, MdRule, MdVerify]
        for model in list_models:
            self.__ns = model().set_model_to_ns(ns=self.__ns)
