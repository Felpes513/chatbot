from flask import Blueprint, request, render_template, redirect, url_for
from app.services.buscar_exame import buscar_exame_por_nome
from app.services.videos_tutoriais import buscar_videos_por_email
from app.services.cadastrar_pre_usuario import cadastrar_pre_usuario
import os
from flask import flash

main = Blueprint('main', __name__)

# Página principal
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

# Funções de rota
@main.route('/buscar_exame', methods=['GET', 'POST'])
def buscar_exame_route():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        data_exame = request.form.get('data_exame')
        cpf = request.form.get('cpf')

        from app.services.buscar_exame import buscar_exame_por_nome
        resultados, erro = buscar_exame_por_nome(nome_paciente, data_exame, cpf)

        if resultados:
            return render_template('buscar_exame.html', resultados=resultados, nome_paciente=nome_paciente)
        else:
            # Se já tentou com dados extras e mesmo assim falhou, mostrar link do suporte
            solicitar_mais_dados = bool(data_exame or cpf)
            return render_template('buscar_exame.html',
                                   nome_paciente=nome_paciente,
                                   erro=erro,
                                   solicitar_mais_dados=not solicitar_mais_dados)
    
    return render_template('buscar_exame.html')


@main.route('/videos_tutoriais', methods=['GET', 'POST'])
def videos():
    if request.method == 'POST':
        email = request.form.get('email')
        videos, erro = buscar_videos_por_email(email)

        return render_template('videos_tutoriais.html', videos=videos, erro=erro)
    
    return render_template('videos_tutoriais.html', videos=None, erro=None)

@main.route('/email_solicitacao', methods=['GET', 'POST'])
def solicitar_novo_usuario():
    if request.method == 'POST':
        permissao = request.form.get('permissao')
        nome = request.form.get('nome')
        email = request.form.get('email')
        crm = request.form.get('crm')
        estado_crm = request.form.get('estado_crm')

        assinatura = request.files.get('assinatura')
        if assinatura:
            caminho_assinatura = os.path.join('uploads', assinatura.filename)
            assinatura.save(caminho_assinatura)
        else:
            caminho_assinatura = None

        
        cadastrar_pre_usuario(nome, email)

        print(f'Permissão: {permissao}')
        print(f'Nome: {nome}, Email: {email}')
        print(f'CRM: {crm}, Estado CRM: {estado_crm}')
        print(f'Caminho Assinatura: {caminho_assinatura}')

        flash('Solicitação enviada com sucesso!', 'success')
        return redirect(url_for('main.solicitar_novo_usuario'))

    return render_template('email_solicitacao.html')
