from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuração da chave secreta para sessões
    app.config['SECRET_KEY'] = 'uma_chave_secreta_super_segura'  # Use uma chave secreta real e segura

    # Registra o blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
