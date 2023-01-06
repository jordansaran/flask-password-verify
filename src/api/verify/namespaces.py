from flask_restx import Namespace


class NsVerify:

    __ns: Namespace

    def __init__(self):
        self.__ns = Namespace(name='verify', validate=True)

    def get_namespace(self):
        return self.__ns
