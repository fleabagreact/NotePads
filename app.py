from flask import Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERDIFICIL2'

# Inicializa o gerenciador de login
login_manager.init_app(app)


# Carrega o usuário pelo ID (matrícula)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        user = User.select_get_by_email(email)
        if user:
            # Verifica a senha do usuário
            hash = user.senha
            if check_password_hash(hash, senha):
                login_user(user)
                
                return redirect(url_for('dash'))
            else:
                return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        # Gera hash para senha e email
        hash = generate_password_hash(senha)
      

        # Insere o novo usuário e faz login automático
        User.insert_data_user(email, hash)
        

        return redirect(url_for("index"))
    
    return render_template('register.html')

@app.route('/dash')
def dash():
    return render_template('dash.html')