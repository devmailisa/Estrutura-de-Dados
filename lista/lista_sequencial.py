import numpy as np

class ListaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Lista:
    """
    operacoes fundamentais: inicialização, inserção, remoção, elemento, busca e percurso
    """
    def __init__(self, tamanho:int=10):
        try:
            assert tamanho > 0
        except AssertionError:
            raise  ListaException("Tamanho do array deve ser um número maior do que zero.")
        
        self.__array = np.full(tamanho, None)
        self.__ultimo = -1
    
    def __len__(self) -> int:
        return self.__ultimo+1
    
    def esta_vazia(self)->bool:
        return self.__ultimo==-1
    
    def esta_cheia(self)->bool:
        return self.__ultimo+1 == len(self.__array)
    
    def elemento(self, posicao: int)->any:
        try:
            assert 0 < posicao <= len(self)
        except AssertionError:
            raise ListaException(f"Posição inválida. Os valores permitidos são de 1 a {len(self)}.")
        
        return self.__array[posicao-1]
    
    def busca(self, carga:any)->int:
        for i in range(0, len(self), 1):
            if self.__array[i] == carga:
                return i+1
        
        raise ListaException(f"A carga {carga} não está na lista.")
    
    def inserir(self, posicao:int, carga:any):
        try:
            assert not self.esta_cheia()
            assert 0 < posicao <= self.__ultimo+2
        except AssertionError:
            raise  ListaException(f"Informe uma posição válida. Os valores permitidos são de 1 a {self.__ultimo+2}.")
        
        for i in range(self.__ultimo+1, posicao-1, -1):
            self.__array[i] = self.__array[i-1]
        
        self.__array[posicao-1] = carga
        self.__ultimo+=1

    def insereFim(self, carga:any):
        self.inserir(len(self)+1, carga)

    def insereInicio(self, carga:any):
        self.inserir(1, carga)

    def remover(self, posicao: int):
        try:
            assert 0 < posicao <= len(self)
        except AssertionError:
            raise ListaException(f"Informe uma posição válida. Os valores permitidos são de 1 a {len(self)}")

        for i in range(posicao-1, len(self)):
            self.__array[i] = self.__array[i+1]

        self.__ultimo -= 1
    
    def removeInicio(self):
        self.remover(1)
    
    def removeFinal(self):
        self.remover(len(self))

    def removeOcorrencias(self, carga:any):
        try:
            for i in range(0, len(self)):
                value = self.__array[i]
                if value == carga:
                    self.remover(i+1)
        except:
            raise ListaException("Não há ocorrências deste elemento na lista.") 
    
    def modificar(self, posicao: int, carga:any)->str:
        try:
            assert 0 < posicao <= self.__ultimo+1
        except AssertionError:
            raise ListaException("Posição inexistente.")
        
        self.__array[posicao-1] = carga
        return "Posição modificada com sucesso."
    
    def esvaziar(self):
        self.__ultimo = -1

    def concatenar(self, L2:'Lista'): #concatenar self com L2
        resultado = Lista(len(L2)+len(self))

        for i in range(len(self)):
            resultado.insereFim(self.elemento(i+1))
        
        for i in range(len(L2)):
            resultado.insereFim(L2.elemento(i+1))
        
        return resultado

    def __str__(self) -> str:
        s = "Lista = ["

        for i in range(0, self.__ultimo+1):
            s += str(self.__array[i])
            if i != self.__ultimo:
                s+=", "
        s+="]\n"

        return s      