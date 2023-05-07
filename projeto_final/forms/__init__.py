from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, email

class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(6)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(8, 30)])
    btn_entrar = SubmitField('Entrar')

class FormCadastro(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(6)])
    email = StringField('E-mail', validators=[DataRequired(), email()])
    telefone = StringField('Telefone', validators=[DataRequired(), length(11, 20)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(8, 30)])
    confirmarSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), length(8, 30)])
    btn_cadastrar_usuario = SubmitField('Cadastrar')

class FormRecado(FlaskForm):
    nomeCompleto = StringField('Nome Completo', validators=[DataRequired(), length(2)])
    emailRecado = StringField('E-mail', validators=[DataRequired(), email()])
    menssagem = StringField('Menssagem', validators=[DataRequired(), length(1)])
    btn_mandar_recado = SubmitField('Enviar')