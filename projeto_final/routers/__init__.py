from flask import render_template, url_for, redirect, flash
from projeto_final.forms import FormLogin, FormCadastro, FormRecado
from projeto_final import app, banco, bcrypt
from projeto_final.models import Conta, Recado
from flask_login import login_required, logout_user, login_user, current_user

usuario = 'admsupremo'
senha = 'senhafraca'

@app.route("/", methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
            user = Conta.query.filter_by(usuario=formLogin.usuario.data).first()
            if formLogin.usuario.data == usuario and formLogin.senha.data == senha:
                login_user(user)
                return redirect(url_for('usuarios'))

            else:
                if user and bcrypt.check_password_hash(user.senha, formLogin.senha.data):
                    login_user(user)
                    flash('Login feito com sucesso', 'sucesso')
                    return redirect(url_for('gamezone'))

                else:
                    flash('Usuário ou senha incorreto', 'falha')
                    return redirect(url_for('login'))

    return render_template('login.html', formLogin=formLogin)

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    formCadastro = FormCadastro()
    if formCadastro.validate_on_submit():
        try:
            userV = Conta.query.filter_by(usuario=formCadastro.usuario.data).first()
            emailV = Conta.query.filter_by(email=formCadastro.email.data).first()

            if not userV and not emailV:
                if formCadastro.senha.data == formCadastro.confirmarSenha.data:
                    criptoSenha = bcrypt.generate_password_hash(formCadastro.senha.data)
                    user = Conta(usuario=formCadastro.usuario.data, email=formCadastro.email.data, telefone=formCadastro.telefone.data, senha=criptoSenha)
                    banco.session.add(user)
                    banco.session.commit()
                    flash('Usuário cadastrado com sucesso', 'sucesso')
                    return redirect(url_for('login'))

                else:
                    flash('Senhas não correspondentes', 'falha')

            else:
                flash('Usuário ou e-mail já existente', 'falha')

        except:
            flash('Houve um erro no cadastro', 'falha')

        return redirect(url_for('cadastro'))

    return render_template("cadastro.html", formCadastro=formCadastro)

@app.route("/gamezone", methods=['GET', 'POST'])
@login_required
def gamezone():
    formRecado = FormRecado()
    if formRecado.validate_on_submit():
        try:
            msg = Recado(nomeCompleto=formRecado.nomeCompleto.data, emailRecado=formRecado.emailRecado.data, menssagem=formRecado.menssagem.data)
            banco.session.add(msg)
            banco.session.commit()
            flash('Menssagem enviada com sucesso', 'sucesso')
            return redirect(url_for('gamezone'))

        except:
            flash('Não foi possível enviar a menssagem', 'falha')

        return redirect(url_for('gamezone'))

    return render_template('tela_main.html', formRecado=formRecado)

@app.route('/usuarios')
@login_required
def usuarios():
    if current_user.usuario == usuario:
        users = Conta.query.all()
        return render_template('excluir_usuarios.html', usuarios=users)

    else:
        logout_user()
        flash('Acesso restrito', 'falha')
        return redirect(url_for('login'))

@app.route('/excluir_usuario/<int:id>', methods=['POST'])
@login_required
def excluir_usuario(id):
    user = Conta.query.get_or_404(id)
    banco.session.delete(user)
    banco.session.commit()
    return redirect(url_for('usuarios'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout bem sucedido', 'sucesso')
    return redirect(url_for('login'))