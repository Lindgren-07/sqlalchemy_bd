import models
from models import session

def validarCachorro(n,s,r,d):

    try:
        models.Cachorro.validarNomeCachorro(n)
        models.Cachorro.validarSexoCachorro(s)
        models.Cachorro.validarRacaCachorro(r)
        models.Cachorro.validarDescricaoCachorro(d)
        novo_cachorro = models.Cachorro(nome_cachorro=n,sexo_cachorro=s,raca_cachorro=r,descricao_cachorro=d)
        session.add(novo_cachorro)
        session.commit()
    except ValueError as v:
        raise ValueError(v)
  
        

def excluirC(id):
    session.query(models.Cachorro).filter(models.Cachorro.id_cachorro == id).delete()
    session.commit()


def validarDespesas(d,v,de):

    try:
        models.Despesas.validarValor(v)
        models.Despesas.validarDescricaoDespesas(de)
        nova_despesa = models.Despesas(data_despesas=d,valor_despesas=v,descricao_despesas=de)
        session.add(nova_despesa)
        session.commit()
    except ValueError as v:
        raise ValueError(v)
    
def excluirDespesas(id):
    session.query(models.Despesas).filter(models.Despesas.id_despesas == id).delete()
    session.commit()
