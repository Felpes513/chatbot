from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import datetime
from app.services.buscar_exame import buscar_exame_por_nome
from app.services.videos_tutoriais import buscar_videos_por_email
from app.services.cadastrar_pre_usuario import cadastrar_pre_usuario
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '''
        <h1>Bem-vindo ao MobileChat!</h1>
        <ul>
            <li><a href="/buscar_exame">Buscar Exame</a></li>
            <li><a href="/videos_tutoriais">Vídeos Tutoriais</a></li>
            <li><a href="/email_solicitacao">Solicitar Cadastro</a></li>
        </ul>
    '''

@main.route('/buscar_exame', methods=['GET', 'POST'])
def buscar_exame_route():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        data_exame = request.form.get('data_exame')
        cpf = request.form.get('cpf')

        # Validação e conversão da data
        if data_exame:
            try:
                data_exame = datetime.strptime(data_exame, "%Y-%m-%d").date()
            except ValueError:
                flash("Formato de data inválido. Use o formato AAAA-MM-DD.", "error")
                return render_template('buscar_exame.html', nome_paciente=nome_paciente)

        resultados, erro = buscar_exame_por_nome(nome_paciente, data_exame, cpf)

        if resultados:
            return render_template('buscar_exame.html', resultados=resultados, nome_paciente=nome_paciente)
        else:
            solicitar_mais_dados = bool(data_exame or cpf)
            return render_template('buscar_exame.html',
                                   nome_paciente=nome_paciente,
                                   erro=erro,
                                   solicitar_mais_dados=not solicitar_mais_dados)
    
    return render_template('buscar_exame.html')
