from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User, Nota, Tarefa
from werkzeug.security import generate_password_hash, check_password_hash

import smtplib
import email.message

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERDIFICIL2'

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        hash = generate_password_hash(senha)
        User.insert_data_user(email, hash)

        user = User.select_get_by_email(email)
        login_user(user)

        corpo = f"""
        <p>Bem vindo , email enviado</p>

        """
        assunto = "Cadastro"
        destinatario = current_user.email

        User.enviar_email(corpo, assunto, destinatario)

        return redirect(url_for('dash')) 
    return render_template('register.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        user = User.select_get_by_email(email)
        if user:
            hash = user.senha
            if check_password_hash(hash, senha):
                login_user(user)
                return redirect(url_for('dash'))
            else:
                return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/ver_nota')
@login_required
def ver_nota():
    notas = Nota.get_all_by_user_id(current_user.id)
    return render_template('ver_nota.html', notas=notas)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_note():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        Nota.add(titulo, descricao, current_user.id)
        flash('Nota criada com sucesso!', 'success')
        return redirect(url_for('dash'))
    return render_template('nota.html', nota=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    nota = Nota.get_by_id(id)
    if nota.user_id != current_user.id:
        flash('Você não tem permissão para editar esta nota.', 'danger')
        return redirect(url_for('dash'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        Nota.update(id, titulo, descricao)
        flash('Nota atualizada com sucesso!', 'success')
        return redirect(url_for('dash'))
    return render_template('nota.html', nota=nota)

@app.route('/delete/<int:id>')
@login_required
def delete_note(id):
    nota = Nota.get_by_id(id)
    if nota.user_id != current_user.id:
        flash('Você não tem permissão para excluir esta nota.', 'danger')
        return redirect(url_for('dash'))

    Nota.delete(id)
    flash('Nota excluída com sucesso!', 'success')
    return redirect(url_for('dash'))

@app.route('/tarefa')
@login_required
def tarefa():
    user_id =current_user.id
    tarefas = Tarefa.get_all_by_user_id(user_id)
    return render_template('tarefa.html', tarefas=tarefas)

@app.route('/add_tarefa',methods=['GET','POST'])
@login_required
def add_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        user_id = current_user.id 
        Tarefa.add_tarefa(titulo, descricao, user_id)
        return redirect(url_for("tarefa"))
    return render_template('add_tarefa.html')

@app.route('/delete_tarefa/<int:id>')
@login_required
def delete_tarefa(id):
    Tarefa.delete_tarefa(id)
    return redirect(url_for('tarefa'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('index'))