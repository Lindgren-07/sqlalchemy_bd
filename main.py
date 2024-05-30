from flask import Flask,request,redirect,render_template,flash
import validacao
import models 
app = Flask(__name__)
app.secret_key = 'joao07'


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/despesas')
def despesas():
   return render_template('despesas.html')

@app.route('/cachorro')
def cachorro():
   cachorros = models.session.query(models.Cachorro).all()
   return render_template('cachorro.html', cachorros = cachorros)

@app.route('/cadastrar_cachorro',methods=['POST'])
def cadastrar_cachorro():
   nome = request.form.get('nome_cachorro')
   sexo = request.form.get('sexo_cachorro')
   raca = request.form.get('raca_cachorro')
   descricao = request.form.get('descricao_cachorro')

   if raca == '':
      raca = 'null'

   if descricao == '':
      descricao = 'null'


   try:
      validacao.validarCachorro(nome,sexo,raca,descricao)
      flash('cadastrado com sucesso')
      return redirect('/cachorro')
   except ValueError as v:
      flash(str(v))
      return redirect('/cachorro')
   

@app.route('/excluir_cachorro', methods=['POST'])
def excluir_cachorro():
   nome = request.form.get('nome')
   id = request.form.get('idCachorro')

   try:
      validacao.excluirC(id)
      flash(f'Cachorro "{nome}" excluido com sucesso')
      return redirect('/cachorro')
   except:
      flash(f'erro ao excluir cachorro')
      
   return redirect('/cachorro')


@app.route('/cadastrar_despesas', methods=['POST'])
def cadastrar_despesas():
   data = request.form.get('data_despesas')
   valor = request.form.get('valor_despesas')
   descricao = request.form.get('descricao_despesas')
   
   if data == '':
      data = 'null'

   try:
      validacao.validarDespesas(data,valor,descricao)
      flash('Despesa cadastrada!')
      return redirect('/despesas')
   
   except ValueError as v:
      flash(str(v))
      return redirect('/despesas')
   
if __name__ == '__main__':
   app.run(debug=True)


