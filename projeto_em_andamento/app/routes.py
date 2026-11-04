from app import app
from flask import render_template, redirect, flash, request, url_for
from flask_wtf import FlaskForm
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField
import markdown
import bleach

from .models.conteudo import Conteudo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login.html')
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
            if AuthenticationService.login(formulario):
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for("home"))
            else:
                flash("Usuário ou senha inválidos.", "error")
    return render_template('login.html', title='Login', form=formulario) 

@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

@app.route('/periodos.html')
def santuario():
    return render_template('periodos.html')

@app.route('/lugares.html')
def verde_nasce():
    return render_template('lugares.html')

@app.route('/pesquisadores.html')
def solar_antunes():
    return render_template('pesquisadores.html')

@app.route('/visitas.html')
def sao_francisco():
    return render_template('visitas.html')

@app.route('/mercado-publico.html')
def mercado_publico():
    return render_template('mercado-publico.html')

@app.route('/biblioteca-municipal.html')
def biblioteca_municipal():
    return render_template('biblioteca-municipal.html')

@app.route('/museu-nilo-pereira.html')
def museu_nilo_pereira():
    return render_template('museu-nilo-pereira.html')

@app.route('/estacao-ferroviaria.html')
def estacao_ferroviaria():
    return render_template('estacao-ferroviaria.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        sucesso = UsuarioService.salvar(formulario)
        if sucesso:
            flash("Usuário cadastrado com sucesso!", category='success')
            return redirect("/url_for('login')")
        else:       
            flash("Erro ao cadastrar o novo usuário.", category='error')
            return render_template("cadastro.html", form = formulario)
    return render_template("cadastro.html", form = formulario)

@app.route('/listar', methods = ['GET'])
def listar():
    lista_usuarios = UsuarioService.listar()
    return render_template("listar.html", usuarios = lista_usuarios)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = UsuarioService.buscar_por_id(id)

    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        sucesso = UsuarioService.atualizar(usuario, form)
        if sucesso:
            flash("Usuário atualizado com sucesso!", category='success')
            return render_template('index.html')
        else:
            flash("Usuário não atualizado. Tente novamente mais tarde.",category='error')
            return render_template("cadastro.html", form=form, editar=True)

    return render_template("cadastro.html", form=form, editar=True)

@app.route('/remover/<int:id>', methods=['GET'])
def remover(id):
    usuario = UsuarioService.buscar_por_id(id)
    if usuario:
        removeu = UsuarioService.remover(usuario)
        if removeu:
            flash("Usuário removido com sucesso!", category="success")
        else:
            flash("Erro ao remover usuário.", category="error")
    else:
        flash("Usuário não encontrado.", category="error")
    return render_template("index.html")    


