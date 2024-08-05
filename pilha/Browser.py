from pilha_sequencial import Pilha

class DNS:
    __urls={"ifpb":"192.168", "google": "10.10", "g1": "19.17", "uol":"1.10"}

    def add(cls, url:str, ip:str):
        cls.__urls[url] = ip

    def existsURL(cls, url:str)->bool:
        return url in cls.__urls.keys()
    
class Browser:
    def __init__(self):
        self.__historico = Pilha()
        self.__home = None

    def request(self, url:str):
        dns = DNS()

        if not dns.existsURL(url):
            return
        
        if self.__home != None:
            self.__historico.empilha(self.__home)
        self.__home = url
    
    def back(self):
        if not self.__historico.esta_vazia():
            self.__home = self.__historico.topo()
            self.__historico.desempilha()
    
    def __str__(self):
        tam = len(self.__historico)
        resultado = '[ '
        for i in range(tam):
            resultado += self.__historico.elemento(i+1)
            if tam > i+1:
                resultado += ' > '
        resultado += f' ]\nhome: {self.__home}'
        return resultado