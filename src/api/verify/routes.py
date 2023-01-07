"""
API endpoint definido para /verify namespace.
"""
from http import HTTPStatus
from flask_restx import Resource, marshal

from src.api.verify.controllers import VerificationController
from src.api.verify.namespaces import NsVerify

ns_verify = NsVerify().get_namespace()


@ns_verify.route("", endpoint='verify')
@ns_verify.response(int(HTTPStatus.BAD_REQUEST), 'Erro na requisição de validação do password.')
@ns_verify.response(int(HTTPStatus.NOT_FOUND), 'Pagina não encontrada.')
@ns_verify.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), 'Erro interno no servidor.')
class Verify(Resource):
    """ Handles HTTP requests to URL: /verify """

    @ns_verify.doc(body=ns_verify.models.get("Verify"))
    @ns_verify.response(int(HTTPStatus.OK), 'Retorna se o password é válido, caso não, '
                                            'retorna as regras que não foram válidas para o password',
                        ns_verify.models.get("Match"))
    def post(self):
        """ Verificar password. """
        ns_verify.logger.info("Verificação de password executado com sucesso.")
        return marshal(VerificationController(payload=ns_verify.payload).execute(), ns_verify.models.get("Match")),\
            int(HTTPStatus.OK)
