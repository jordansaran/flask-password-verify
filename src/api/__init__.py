"""
Configuração da API blueprint do Flask-RESTX.
"""
from flask import Blueprint
from flask_restx import Api

from src.api.verify.routes import ns_verify

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(
    api_bp,
    version='1.0',
    title='Validação de password - API',
    description='Bem vindo a UI documentação da API de validação de password com Swagger.',
    doc='/ui',
    validate=True,
)

api.add_namespace(ns_verify, path='/verify')
