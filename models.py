from sqlalchemy import create_engine,Column,Integer,String,Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



engine = create_engine('postgresql://postgres:jlindgren@localhost:5432/ozanimais')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




class Administrador(Base):
   __tablename__ = 'administrador'
   id_administrador = Column(Integer,primary_key=True,autoincrement=True)
   nome_administrador = Column(String(30),nullable=False)    
   senha_administrador = Column(String(15),nullable=False)

   def validarNome(nome):
      if nome == '':
         raise ValueError('O Campo "nome" não pode ser nulo!')
       
      tamanho = len(nome)

      if tamanho < 1 or tamanho > 30:
         raise ValueError('O tamanho do nome deve conter entre 1 a 30 Character!')
       
      for i in nome:
         if not i.isalpha() and not i.isspace():
            raise ValueError('O campo nome deve conter apenas character válidos!')
          
    
   def validarSenha(senha):
      if senha == '':
         raise ValueError('O campo "senha" não pode ser nula')
       
      tamanho = len(senha)
  
      if tamanho < 8 or tamanho > 15:
         raise ValueError('A senha deve conter entre 8 a 15 character!')
       
      for i in senha:
         if not i.isalpha():
            raise ValueError('a senha deve conter apenas character válidos!')

   def __str__(self):
     return f'nome: {self.nome_administrador}, senha: {self.senha_administrador}'



class Cachorro(Base):
   __tablename__= 'cachorro'
   id_cachorro = Column(Integer,primary_key=True,autoincrement=True)
   nome_cachorro = Column(String(20),nullable=False)
   sexo_cachorro = Column(String(1), nullable=False)
   raca_cachorro = Column(String(20))
   descricao_cachorro = Column(String(255))


   def validarNomeCachorro(nome_cachorro):
      if nome_cachorro == '':
         raise ValueError('O Campo "nome" não pode ser nulo!')
       
      tamanho = len(nome_cachorro)

      if tamanho < 1 or tamanho > 20:
         raise ValueError('O tamanho do nome tem que ter entre 1 a 20 character!')
       
      for i in nome_cachorro:
         if not i.isalpha() and not i.isspace():
            raise ValueError('O campo nome deve conter apenas character válidos!')

   def validarSexoCachorro(sexo_cachorro):
      if sexo_cachorro == '':
         raise ValueError('O Campo "sexo" não pode ser nulo!')

      sexo_cachorro = sexo_cachorro.upper()

      tamanho = len(sexo_cachorro)

      if tamanho != 1:
         raise ValueError('Deve conter apenas 1 character!')
        
      if sexo_cachorro not in 'MF':
         raise ValueError('Sexo deve ser apenas masculino ou feminino!')
  
    

   def validarRacaCachorro(raca_cachorro):
                 
      for i in raca_cachorro:
         if not i.isalpha():
            raise ValueError('o nome da raça deve conter apenas characters válidos!')




   def validarDescricaoCachorro(descricao_cachorro):
              
      tamanho = len(descricao_cachorro)

      if tamanho < 0 or tamanho > 255:
         raise ValueError('O tamanho da descrição tem que ter entre 1 a 255 character!')
   
   def __str__(self):
     return f'nome: {self.nome_cachorro}, sexo: {self.sexo_cachorro}, raça: {self.raca_cachorro}, Descrição {self.descricao_cachorro}'





class Despesas(Base):
   __tablename__ = 'despesas'
   id_despesas = Column(Integer,primary_key=True,autoincrement=True)
   data_despesas = Column(Date)
   valor_despesas = Column(Integer,nullable=False)
   descricao_despesas = Column(String(255))


   def validarValor(valor):
      if valor == '':
         raise ValueError('O valor não pode ser nulo!')
      
      for i in str(valor):
          if not i.isdigit():
             raise ValueError('No campo valor só pode ser digitado numeros!')

   def validarDescricaoDespesas(descricao_despesas):
              
       tamanho = len(descricao_despesas)

       if tamanho < 0 or tamanho > 255:
          raise ValueError('O tamanho da descrição tem que ter entre 0 a 255 character!')
   
   def __str__(self):
     return f'Valor: {self.valor_despesas}, Descrição: {self.descricao_despesas}'



Base.metadata.create_all(bind=engine)



