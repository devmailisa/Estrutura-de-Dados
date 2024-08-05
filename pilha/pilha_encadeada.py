class PilhaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.proximo = None
    
    def __str__(self):
        return f'{self.carga}'


class Pilha:
    '''
    Classe que implementa a estrutura de dados Pilha usando a 
    técnica sequencial
    '''
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def __len__(self)->int:
        return self.__tamanho

    def esta_vazia(self):
        return self.__topo == None
    
    def topo(self)->any:
        '''
        Método que retorna a carga armazenada no topo da pilha
        '''
        if self.esta_vazia():
            raise PilhaError('Pilha está vazia')
        return self.__topo.carga
    
    def sub_topo(self)->any:
        '''
        Operação para obtenção do conteúdo armazenado no subtopo da pilha.
        Retorno: o conteúdo armazenado no subtopo da pilha
        Exceções: PilhaExeption(), quando a pilha não tiver subtopo
        '''
        try:
            assert len(self) > 1
            return self.elemento(len(self)-1)
        except AssertionError:
            raise PilhaError('Não existe subtopo')

    def elemento(self, posicao:int)->any:
        '''
        Método que recebe a posição de um elemento da pilha que deseja
        consultar. Retorna a carga armazenada na posição específica.
        A posicao retornada é em direição da base para o topo
        '''
        try:
            assert  0 < posicao <= len(self)
            cursor = self.__topo
            for _ in range(len(self)-posicao):
                cursor = cursor.proximo
            return cursor.carga
        except AssertionError:
            raise PilhaError(f'Posicao invalida. A pilha no momento possui {len(self)} elementos.')

    def busca(self, chave:any)->int:
        '''
        Método que recebe uma chave de busca e retorna a posição em
        que a carga foi encontrada na pilha
        '''
        cursor = self.__topo
        contador = len(self)
        while(cursor != None):
            if cursor.carga == chave:
                return contador
            cursor = cursor.proximo
            contador -=1
        raise PilhaError(f"Chave {chave} não encontrada")

    def empilha(self, carga:any):
        no = No(carga)
        no.proximo = self.__topo
        self.__topo = no
        self.__tamanho += 1
            
    def desempilha(self)->any:
        if self.esta_vazia():
            raise PilhaError('Pilha está vazia')
        carga = self.__topo.carga
        self.__topo =  self.__topo.proximo
        self.__tamanho -= 1
        return carga
    
    def desempilha_n(self, n:int) -> bool:
        if len(self) - n < 0:
            return False
        for _ in range(n):
            self.desempilha()
        
        return True

    def esvaziar(self):
        while not self.esta_vazia():
            self.desempilha()

    def __str__(self)->str:
        s = 'topo->[ '

        cursor = self.__topo
        while( cursor != None):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo

        s = s.strip(', ')
        s += ' ]'
        return s