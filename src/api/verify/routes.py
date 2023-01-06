"""
API endpoint definido para /verify namespace.
"""
from http import HTTPStatus
from flask_restx import Resource, fields

from src.api.verify.controllers import VerificationController
from src.api.verify.namespaces import NsVerify

ns_verify = NsVerify().get_namespace()

match_model = ns_verify.model('Match', {
    'verify': fields.String(required=True),
    'noMatch': fields.List(fields.String)
})
rule_model = ns_verify.model('Rule', {
            'rule': fields.String(required=True),
            'value': fields.Integer(min=0, required=True)
        })
validation_model = ns_verify.model('Validation', {
    'password': fields.String(required=True),
    'rules': fields.List(fields.Nested(rule_model))
})


@ns_verify.route("", endpoint='verify')
@ns_verify.response(int(HTTPStatus.BAD_REQUEST), 'Erro na requisição de validação do password.')
@ns_verify.response(int(HTTPStatus.NOT_FOUND), 'Pagina não encontrada.')
@ns_verify.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), 'Erro interno no servidor.')
class Verify(Resource):
    """ Handles HTTP requests to URL: /verify """

    @ns_verify.doc(body=validation_model)
    @ns_verify.response(int(HTTPStatus.OK), 'Retorna se o password é válido, caso não, '
                                            'retorna as regras que não foram válidas para o password', match_model)
    def post(self):
        """ Verificar password. """
        return VerificationController(payload=ns_verify.payload).execute()
