import numpy as np

class FilaException(Exception):
    def __init__(self, msg:any):
        super().__init__(msg)

class Fila:
    def __init__(self, tamanho:int = 10):
        self.__array = np.full(tamanho,None)
        self.__fim = -1
        self.__inicio = 0 #indice do primeiro elemento
        self.__tamanho = 0

    def __len__(self) -> int:
        return self.__tamanho
    
    def esta_vazia(self):
        return len(self) == 0
    
    def esta_cheia(self):
        return self.__tamanho == len(self.__array)
    
    def frente(self)->any:
        if self.esta_vazia():
            raise FilaException('Fila está vazia')
        return self.__array[self.__inicio]
    
    def elemento(self, posicao:int)->any:
        try:
            assert 0 < posicao <= len(self)
            index = self.__inicio
            for _ in range(posicao -1):
                index = (index+1) % len(self.__array)
            return self.__array[index]

        except AssertionError:
            raise FilaException('Posição inválida.')
        
    def busca(self, chave:any) -> int:
        index = self.__inicio
        for i in range(1,self.__tamanho + 1 ):
            if chave == self.__array[index]:
                return i
            index = (index + 1) % len(self.__array)
        raise FilaException(f"Chave {chave} não encontrada")
    
    def enfileirar(self, valor:any ):
        if self.esta_cheia():
            raise FilaException(f'Fila cheia. Não é possível inserir elementos')

        self.__tamanho +=1
        self.__final = (self.__final + 1) % len(self.__array)
        self.__array[ self.__final ] = valor
        