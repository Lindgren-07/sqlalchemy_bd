from flask import Flask,request,redirect,render_template,flash
import validacao
app = Flask(__name__)
app.secret_key = 'joao07'


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/cadastrar_cachorro',methods=['POST'])
def cadastrar_cachorro():
   nome = request.form.get('nome_cachorro')
   sexo = request.form.get('sexo_cachorro')
   raca = request.form.get('raca_cachorro')
   descricao = request.form.get('descricao_cachorro')

   try:
      validacao.validarCachorro(nome,sexo,raca,descricao)
      flash('cadastrado com sucesso')
      return redirect('/')
   except ValueError as v:
      flash(str(v))
      return redirect('/')
  
   
   
if __name__ == '__main__':
   app.run(debug=True)


