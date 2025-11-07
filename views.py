from app import app
from flask import render_template, redirect, request, flash
from flask_mail import Message
from contato import Contato
from dotenv import load_dotenv
import os


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/projetos/risco-credito')
def risco_credito():
    return render_template('projetos/risco-credito.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )

        msg = Message(
            subject = f'Mensagem de {formContato.nome} enviada pelo site do portifólio',
            sender = app.config.get('MAIL_USERNAME'),
            recipients = [app.config.get('MAIL_USERNAME'), os.getenv("EMAIL_PESSOAL")],
            body = f'''Mensagem recebida de {formContato.nome} por meio do email: "{formContato.email}"
            
{formContato.mensagem}
            
            '''
        )
        from app import mail
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/#contato')