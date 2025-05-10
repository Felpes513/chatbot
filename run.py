from dotenv import load_dotenv
load_dotenv()  # <-- Adicione esta linha antes de qualquer uso do banco

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)