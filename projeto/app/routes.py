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