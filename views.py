from app import app
from flask import render_template, redirect, request, flash
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