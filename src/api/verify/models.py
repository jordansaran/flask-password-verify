from abc import ABC, abstractmethod

from flask_restx import Namespace, fields, Model


class MixinModel(ABC):

    @abstractmethod
    def set_model_to_ns(self, ns: Namespace):
        pass

    @abstractmethod
    def _create_model(self):
        pass

    @abstractmethod
    def get_model(self):
        pass


class CreateModel(MixinModel):
    _structure: dict = {}
    __name_model: str = None
    __model: Model

    def __init__(self, name_model: str, structure: dict):
        self.__name_model = name_model.title()
        self._structure = structure
        self._create_model()

    def set_model_to_ns(self, ns: Namespace):
        ns.model(self.__class__.__name__ if self.__name_model is None else self.__name_model, self._structure)
        return ns

    def _create_model(self):
        self.__model = Model(self.__name_model, self._structure)

    def get_model(self):
        return self.__model


class MdMatch(CreateModel):

    def __init__(self):
        CreateModel.__init__(self,
                             name_model="Match",
                             structure={
                                 'verify': fields.String(required=True),
                                 'noMatch': fields.List(fields.String, required=True)
                             })


class MdRule(CreateModel):

    def __init__(self):
        CreateModel.__init__(self,
                             name_model="Rule",
                             structure={
                                 'rule': fields.String(required=True),
                                 'value': fields.Integer(min=0, required=True)
                             })


class MdVerify(CreateModel):

    def __init__(self):
        CreateModel.__init__(self,
                             name_model="Verify",
                             structure={
                                 'password': fields.String(required=True),
                                 'rules': fields.List(fields.Nested(MdRule().get_model()))
                             })
