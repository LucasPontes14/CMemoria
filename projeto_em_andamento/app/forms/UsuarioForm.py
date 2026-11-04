from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from app.services.UsuarioService import UsuarioService


class UsuarioForm(FlaskForm):
    username = StringField('Nome Completo', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', 
                             validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Entrar')
    
    
    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado.')
    
        if not UsuarioService.checar_unicidade(field.data.strip(), 'username'):
            raise ValidationError('Nome de usuário já cadastrado.')
        
    def validate_email(self, field):
        if not UsuarioService.checar_unicidade(field.data.strip().lower(), 'email'):
            raise ValidationError('Email já cadastrado.')