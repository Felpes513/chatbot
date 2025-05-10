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
# Vídeos tutoriais por e-mail
@main.route('/videos_tutoriais', methods=['GET', 'POST'])
def videos_tutoriais_route():
    if request.method == 'POST':
        email = request.form.get('email')

        videos, erro = buscar_videos_por_email(email)

        if erro:
            flash(erro, 'error')
            return render_template('videos_tutoriais.html', email=email)

        return render_template('videos_tutoriais.html', videos=videos, email=email)

    return render_template('videos_tutoriais.html')

@main.route('/email_solicitacao', methods=['GET', 'POST'])
def email_solicitacao_route():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        permissao = request.form.get('permissao')
        crm = request.form.get('crm')
        estado_crm = request.form.get('estado_crm')
        assinatura = request.files.get('assinatura')

        caminho_assinatura = None
        if assinatura and assinatura.filename:
            caminho_assinatura = os.path.join('uploads', assinatura.filename)
            assinatura.save(caminho_assinatura)

        sucesso, mensagem = cadastrar_pre_usuario(
        nome=nome,
        email=email,
        permissao=permissao,
        crm=crm,
        estado_crm=estado_crm,
        caminho_assinatura=caminho_assinatura
)

        if sucesso:
            flash("Solicitação enviada com sucesso!", "success")
            return redirect(url_for('main.email_solicitacao_route'))
        else:
            flash(mensagem, "error")

    return render_template('email_solicitacao.html')