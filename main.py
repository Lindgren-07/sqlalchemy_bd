from flask import Flask,request,redirect,render_template
from sqlalchemy import create_engine,Column,Integer,String,Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

app = Flask(__name__)


engine = create_engine('postgresql://postgres:jlindgren@localhost:5432/ozanimais')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




class Administrador(Base):
    __tablename__ = 'administrador'
    id_administrador = Column(Integer,primary_key=True,autoincrement=True)
    nome_administrador = Column(String(30),nullable=False)    
    senha_administrador = Column(String(15),nullable=False)

    def validarNome(self,nome):
       if nome == '':
        raise ValueError('o nome não pode ser nulo')
       
       tamanho = len(nome)

       if tamanho < 1 or tamanho > 30:
          raise ValueError('tamanho do nome invalido')
       
       for i in nome:
          if not i.isalpha():
             raise ValueError('o nome deve ser um caracter valido')
          
    
    def validarSenha(self,senha):
       if senha == '':
        raise ValueError('A senha não pode ser nula!!!')
       
       tamanho = len(senha)

       if tamanho < 1 or tamanho > 15:
          raise ValueError('tamanho da senha invalida')
       
       for i in senha:
          if not i.isalpha():
             raise ValueError('a senha deve ser um caracter valido')

    def __str__(self):
     return f'nome: {self.nome_administrador}, senha: {self.senha_administrador}'



class Cachorro(Base):
    __tablename__= 'cachorro'
    id_cachorro = Column(Integer,primary_key=True,autoincrement=True)
    nome_cachorro = Column(String(20),nullable=False)
    sexo_cachorro = Column(String(1), nullable=False)
    raca_cachorro = Column(String(20))
    descricao_cachorro = Column(String(255))


    def validarNome(self,nome):
       if nome == '':
        raise ValueError('o nome não pode ser nulo')
       
       tamanho = len(nome)

       if tamanho < 1 or tamanho > 30:
          raise ValueError('tamanho do nome invalido')
       
       for i in nome:
          if not i.isalpha():
             raise ValueError('o nome deve ser um caracter valido')


class Despesas(Base):
    __tablename__ = 'despesas'
    id_despesas = Column(Integer,primary_key=True,autoincrement=True)
    data_despesas = Column(Date)
    valor_despesas = Column(Integer,nullable=False)
    descricao_despesas = Column(String(255))


"""novo_cachorro = Cachorro(nome_cachorro='dib',sexo_cachorro='M',raca_cachorro='pastor alemão')
session.add(novo_cachorro)
session.commit()
"""

"""session.query(Cachorro).filter(Cachorro.id_cachorro==1).delete()
session.commit()"""


"""
novo_adm = Administrador(nome_administrador='Ozana',senha_administrador='Vagabunda')
session.add(novo_adm)
session.commit()"""


"""session.query(Administrador).filter(Administrador.id_administrador==1).update({'senha_administrador':'Ozana123'})
session.commit()
"""

"""novo_adm = Administrador(nome_administrador='jp',senha_administrador='jp123')
session.add(novo_adm)
session.commit()
"""



"""consultar_adms = session.query(Administrador).all()
for adms in consultar_adms:
    print(adms)
"""


"""try:
   admin = Administrador()
   admin.validarNome('4445´´[]')
   admin.validarSenha('234lpç=')
   novo_administrador = Administrador(nome_administrador='4445´´[]',senha_administrador='234lpç=')
   session.add(novo_administrador)
   session.commit()
   print('Validado com sucesso!)
except ValueError as v:
   print(v)"""




if __name__ == '__main__':
   Base.metadata.create_all(bind=engine)
   app.run()


