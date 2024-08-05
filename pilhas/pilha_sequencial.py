import numpy as np

class PilhaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class Pilha:
    '''
    Classe que implementa a estrutura de dados Pilha usando a 
    técnica sequencial
    '''
    def __init__(self, tamanho:int = 10):
        self.__array = np.full(tamanho,None)
        self.__topo = -1

    def __len__(self)->int:
        return self.__topo + 1

    def esta_vazia(self):
        return self.__topo == -1

    def topo(self)->any:
        '''
        Método que retorna a carga armazenada no topo da pilha
        '''
        if self.esta_vazia():
            raise PilhaError('Pilha está vazia')
        return self.__array[self.__topo]

    def esta_cheia(self):
        return self.__topo + 1 == len(self.__array)
    
    def elemento(self, posicao:int)->any:
        '''
        Método que recebe a posição de um elemento da pilha que deseja
        consultar. Retorna a carga armazenada na posição específica.
        A posicao retornada é em direição da base para o topo
        '''
        try:
            assert  0 < posicao <= self.__topo + 1
            return self.__array[posicao-1]
        except AssertionError:
            raise PilhaError(f'Posicao invalida. A pilha no momento possui {len(self)} elementos.')

    def busca(self, chave:any)->int:
        '''
        Método que recebe uma chave de busca e retorna a posição em
        que a carga foi encontrada na pilha
        '''
        for i in range(len(self)):
            if chave == self.__array[i]:
                return i + 1
        raise PilhaError(f"Chave {chave} não encontrada")

    def empilha(self, carga:any):
        if self.esta_cheia():
            raise PilhaError('Pilha está cheia')
        self.__topo += 1
        self.__array[self.__topo] = carga

    def desempilha(self)->any:
        if self.esta_vazia():
            raise PilhaError('Pilha está vazia')
        carga = self.__array[self.__topo] 
        self.__topo -= 1
        return carga
        
    def esvaziar(self):
        while not self.esta_vazia():
            self.desempilha()
            
    def __str__(self)->str:
        s = '[ '
        for i in range(len(self)):
            s += f'{self.__array[i]}, '
        s = s.strip(', ')
        s += ' ]<-topo'
        return s