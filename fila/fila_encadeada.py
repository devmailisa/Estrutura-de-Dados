class FilaException(Exception):
    def __init__(self, msg:any):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__proximo = None

class Descritor:
    def __init__(self):
        self.inicio = self.final = None
        self.tamanho = 0

class Fila:
    def __init__(self):
        self.__head = Descritor()

    def __len__(self) -> int:
        return self.__head.tamanho
    
    def esta_vazia(self) -> bool:
        return self.__head.tamanho == 0
    
    def frente(self)->any:
        if self.esta_vazia():
            raise FilaException('A fila está vazia')
        return self.__head.inicio.carga
    
    def elemento(self, posicao:int)->any:
        try:
            assert 0 < posicao <= len(self)
            cursor = self.__head.inicio

            for _ in range(len(self) - posicao):
                cursor = cursor.__proximo
            return cursor.__carga
        except AssertionError:
            raise FilaException(f'Posição inválida')
        
    def busca(self, chave:any):
        cursor = self.__inicio
        contador = 1
        while(cursor != None):
            if(cursor.__carga == chave):
                return contador
            cursor = cursor.proximo
            contador +=1
        raise FilaException(f'Chave {chave} inválida!')