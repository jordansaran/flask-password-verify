"""
Criação da aplicaçãoFlask
"""
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from src.settings import get_config


def create_app(testing: bool = False):
    """"
    Criação da aplicação para deploy, testing ou production
    :param testing: bool = False
    """
    app = Flask('api')
    config_env = get_config(testing)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config_env)

    if config_env.FLASK_DEBUG:
        # Para ambiente deploy permitir a criação do Swagger
        from src.api import api_bp
        app.register_blueprint(api_bp)

    return app
