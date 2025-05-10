from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuração da chave secreta para sessões
    app.config['SECRET_KEY'] = 'uma_chave_secreta_super_segura'

    # Registro do blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app

# Executar servidor
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
