from flask import Blueprint, request, render_template, redirect, url_for
from application.models import obter_produtos, add_produto, deletar_produto

main = Blueprint('main', __name__)

@main.route('/')
def home():
    produtos = obter_produtos()
    return render_template('index.html', produtos=produtos)

@main.route('/add', methods=['GET', 'POST'])
def rota_adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        codigo_produto = request.form['codigo_produto']
        descricao = request.form['descricao']
        preco = request.form['preco']
        
        add_produto(nome, codigo_produto, descricao, preco)
        
        return redirect(url_for('main.home'))
    
    return render_template('add_produto.html')


@main.route('/delete/<int:id>', methods=['POST'])
def rota_deletar_produto(id):
    deletar_produto(id)
    return redirect(url_for('main.home'))
