from flask import Flask,request,redirect,render_template,flash
import validacao
import models 

app = Flask(__name__)
app.secret_key = 'joao07'


@app.route('/assinante')
def assinante():
   assinantes = models.session.query(models.Assinante).all()
   return render_template('assinante.html', assinantes=assinantes)

@app.route('/padrinho')
def padrinho():
   padrinhos = models.session.query(models.Padrinho).all()
   return render_template('padrinho.html', padrinhos = padrinhos)

@app.route('/tabelas')
def home():
   return render_template('tabelas.html')

@app.route('/despesas')
def despesas():
   despesas = models.session.query(models.Despesas).all()
   return render_template('despesas.html', despesas = despesas)

@app.route('/cachorro')
def cachorro():
   cachorros = models.session.query(models.Cachorro).all()
   return render_template('cachorro.html', cachorros = cachorros)

@app.route('/')
def adm():
   usuarios = models.session.query(models.Administrador).all()
   return render_template('adm.html', usuarios = usuarios)

@app.route('/cadastrar_cachorro',methods=['POST'])
def cadastrar_cachorro():
   nome = request.form.get('nome_cachorro')
   sexo = request.form.get('sexo_cachorro')
   raca = request.form.get('raca_cachorro')
   descricao = request.form.get('descricao_cachorro')

   if raca == '':
      raca = 'vazia'

   if descricao == '':
      descricao = 'vazia'


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
      data = 'vazia'

   try:
      validacao.validarDespesas(data,valor,descricao)
      flash('Despesa cadastrada!')
      return redirect('/despesas')
   except ValueError as v:
      flash(str(v))
      return redirect('/despesas')
   

@app.route('/excluir_despesas',methods=['POST'])
def excluir_despesas():
   id = request.form.get('idDespesas')

   try:
      validacao.excluirDespesas(id)
      flash(f'Despesa excluida com sucesso')
      return redirect('/despesas')
   except:
      flash(f'erro ao excluir despesas')
      
   return redirect('/despesas')


@app.route('/cadastrar_adm', methods=['POST'])
def cadastrar_adm():
   email = request.form.get('email_adm')
   senha = request.form.get('senha_adm')
   btn = request.form.get('btn_adm')

   if btn == 'cadastrar':
      try:
         validacao.cadastrarUsuario(email,senha)
         flash('Usuário cadastrado com sucesso')
         return redirect('/')
      except ValueError as v:
         flash(str(v))

      return redirect('/')
   else:
      usuarios = models.session.query(models.Administrador).all()
      if usuarios:
         for i in usuarios:
            if i.email_administrador == email and i.senha_administrador == senha:
               return redirect('/tabelas')
         flash('email ou senha inválidos')
         return redirect('/')
      else:
         flash('Nenhum usuário cadastrado')
         return redirect('/')

@app.route('/cadastrar_padrinho', methods=['POST'])
def cadastrar_padrinho():
   nome = request.form.get('nome_padrinho')
   sobrenome = request.form.get('sobrenome_padrinho')
   telefone = request.form.get('telefone_padrinho')
   email = request.form.get('email_padrinho')

   try:
      validacao.validarPadrinho(nome,sobrenome,telefone,email)
      flash('Padrinho cadastrado!')
      return redirect('/padrinho')
   except ValueError as v:
      flash(str(v))
      return redirect('/padrinho')
   
@app.route('/cadastrar_assinante', methods=['POST'])
def cadastrar_assinante():
    nome = request.form.get('nome_assinante')
    email = request.form.get('email_assinante')

    try:
        validacao.validarAssinante(nome, email)
        flash('Assinante cadastrado!')
        return redirect('/assinante')
    except ValueError as v:
        flash(str(v))
        return redirect('/assinante')


@app.route('/excluir_padrinho', methods=['POST'])
def excluir_padrinho():
   id = request.form.get('id_padrinho')
   nome = request.form.get('nome_padrinho')
   email = request.form.get('email_padrinho')

   try:
      validacao.excluirPadrinho(id)
      flash('padrinho excluido')
      return redirect('/padrinho')
   except ValueError as v:
      flash(str(v))
      return redirect('/padrinho')


@app.route('/excluir_assinante', methods=['POST'])
def excluir_assinante():
   id = request.form.get('id_assinante')
   nome = request.form.get('nome_assinante')
   email = request.form.get('email_assinante')

   try:
      validacao.excluirAssinante(id)
      flash('assinante excluido')
      return redirect('/assinante')
   except ValueError as v:
      flash(str(v))
      return redirect('/assinante')

   
if __name__ == '__main__':
   app.run(debug=True)


