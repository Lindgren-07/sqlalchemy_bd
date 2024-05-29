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
    else:
        print('funcionou')
        

def excluirC(id):
    session.query(models.Cachorro).filter(models.Cachorro.id_cachorro == id).delete()
    session.commit()
