import sys,select
import json
import Pyro4

from time import  sleep
class Ponto_de_acesso:
    def __init__(self,local,mestre,id):
        self.local = local
        self.mestre = mestre
        self.id = id
        self.liberado=False

    def solicita_passagem(self,id_pessoa,sentido):
        print("solicita acesso ao mestre para pessoa {} ao local".format(id_pessoa))
        return True

    def libera_passagem(self):
        print("libera passagem por 5s")
        self.liberado = True
        i,o,e = select.select([sys.stdin],[],[],5)
        self.liberado = False
        if (i):
            return True
        else:
            return False


    def registra_passgem(self,id_pessoa,sentido):
        print("informa ao mestre a passagem da pessoa {} no sentido {}".format(id_pessoa,sentido))

def Main():
    mestre = Pyro4.Proxy("PYRONAME:mestre")
    print(mestre.consulta_pessoa("1"))
    config={}
    with open("config.cfg") as arquivo_de_configuracao:
        config = json.load(arquivo_de_configuracao)
        print()
        ip_mestre=config.get("mestre").get("host")
        porta_mestre=config.get("mestre").get("port")
        id=config.get("ponto_de_acesso").get("id")
        local=config.get("ponto_de_acesso").get("local")
    '''ip_mestre = input("digite o endereco ip do mestre")
    porta_mestre= input ("digite a porta de acesso no mestre")
    local=input("digite local")
    id = "12345"'''
    mestre=ip_mestre+':'+porta_mestre
    ponto_de_acesso = Ponto_de_acesso(local=local,mestre=mestre,id=id)
    while (True):
        id_pessoa = input("identificador da pessoa")
        sentido = input("sentido :")
        resposta = ""
        if (ponto_de_acesso.solicita_passagem(id_pessoa,sentido)):
            if (ponto_de_acesso.libera_passagem()):
                ponto_de_acesso.registra_passgem(id_pessoa,sentido)
            else:
                print("passagem canselada")
        sleep(1)
if __name__ == "__main__":

    # print("dp")
    Main()