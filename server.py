import Pyro4
pessoas = {"1":{"vinculo":"funcionario"},"2":{"vinculo":"visitante"}}
print(pessoas.get("1"))
locais= {"bloco5,andar3":{"limite":1,"atual":0}}

@Pyro4.expose
class mestre(object):
    def consulta_pessoa(self,id_pessoa):
        return pessoas.get(id_pessoa)






def Main():
    print("servidor central")
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(mestre)
    ns.register("mestre",uri)
    print(uri)
    print("pronto")
    daemon.requestLoop()
if __name__ == "__main__":
    Main()