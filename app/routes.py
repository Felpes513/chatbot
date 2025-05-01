from flask import Flask, render_template, request
from services import buscar_exame

app = Flask(__name__)

@app.route('/')
def main():
    return '''
        <h1>Bem vindo ao MobileChat!</h1>
        <ul>
            <li><a href="/ buscar exame"> Buscar Exame</a></li>
            # <li><a href= "/></a> </li>
            # <li><a href= "/></a> </li>
        </ul>
    '''

@app.route('/buscar-exame', methods=['GET', 'POST'])
def buscar_exame_route():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        resultados = buscar_exame(nome_paciente)
        if resultados:
            resposta = "<h2>Exames encontrados:</h2><ul>"
            for exame in resultados:
                resposta += f"<li>ID: {exame[0]}, Nome: {exame[1]}, Data: {exame[2]}, Unidade: {exame[3]}, Accession: {exame[4]}, Status: {exame[5]}</li>"
            resposta += "</ul>"
            return resposta
        else:
            return f"<p>Nenhum exame encontrado para {nome_paciente}</p>"
    return '''
        <form method="post">
            Nome do paciente: <input type="text" name="nome_paciente">
            <input type="submit" value="Buscar">
        </form>
    '''