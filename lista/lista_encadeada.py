class ListaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.proximo = None
    
    def __str__(self):
        return f'{self.carga}'


class Lista:
    '''
    Classe que implementa a estrutura de dados Lista usando a 
    técnica simplesmente encadeada
    '''
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def __len__(self)->int:
        return self.__tamanho

    def esta_vazia(self):
        return self.__head == None
    
    def elemento(self, posicao:int)->any:
        '''
        Método que recebe a posição de um elemento da pilha que deseja
        consultar. Retorna a carga armazenada na posição específica.
        A posicao retornada é em direição da base para o topo
        '''
        try:
            assert  0 < posicao <= len(self)
            cursor = self.__head
            for _ in range(posicao-1):
                cursor = cursor.proximo
            return cursor.carga
        except AssertionError:
            raise ListaError(f'Posicao invalida. A lista no momento possui {len(self)} elementos.')

    def busca(self, chave:any)->int:
        '''
        Método que recebe uma chave de busca e retorna a posição em
        que a carga foi encontrada na pilha
        '''
        cursor = self.__head
        contador = 1
        while(cursor != None):
            if cursor.carga == chave:
                return contador
            cursor = cursor.proximo
            contador +=1
        raise ListaError(f"Chave {chave} não encontrada")

    def inserir(self, posicao:int, carga:any):
        try:
            assert 0 < posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.esta_vazia()): #mexe com o head da lista
                if ( posicao != 1):
                    raise ListaError(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = No(carga)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = No(carga)
                novo.proximo = self.__head #recebe o primeiro elemento como próximo
                self.__head = novo #se coloca como primeiro elemento
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.proximo
                contador += 1

            novo = No(carga)
            novo.proximo = cursor.proximo
            cursor.proximo = novo
            self.__tamanho += 1

        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo ou 0 (zero)')


    def insereFim(self, carga:any):
        self.inserir(len(self)+1, carga)

    def insereInicio(self, carga: any):
        self.inserir(1,carga)

    def remover(self, posicao:int)->any:
        try:
            if( self.esta_vazia() ):
                raise ListaError(f'Não é possível remover de uma lista vazia')
            
            assert 0 < posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1

            while( contador <= posicao-1 ) :
                anterior = cursor
                cursor = cursor.proximo
                contador+=1

            carga = cursor.carga

            if( posicao == 1):
                self.__head = cursor.proximo
            else:
                anterior.proximo = cursor.proximo

            self.__tamanho -= 1
            return carga
        
        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo')
        
    def removeInicio(self):
        self.remover(1)
    
    def removeFinal(self):
        self.remover(len(self))

    def modificar(self, posicao:int, carga:any):
        try:
            assert 0 < posicao <= len(self)
        except AssertionError:
            raise ListaError(f'Esta posição é inválida. A lista tem {len(self)} elementos.')
        
        cursor = self.__head
        for _ in range(posicao-1):
            cursor = cursor.proximo
        
        cursor.carga = carga
        
    def esvaziar(self):
        while not self.esta_vazia():
            self.remover(1)

    def concatenar(self, L2:'Lista'): #concatenar self com L2
        resultado = Lista()

        for i in range(len(self)):
            resultado.insereFim(self.elemento(i+1))
        
        for i in range(len(L2)):
            resultado.insereFim(L2.elemento(i+1))
        
        return resultado
    
    def maiores(self, n:int)->int:
        contador = 0
        cursor = self.__head
        for _ in range(self.__tamanho):
            if int(cursor.carga) > n:
                contador+=1
            cursor = cursor.proximo

        return contador
    
    '''
    Uma maneira tradicional de se representar um conjunto é através da lista de seus elementos. Supondo esta representação, adicione métodos à sua classe Lista para executar as operações usuais de conjunto: interseção, união e diferença.

    Todos os métodos devem retornar a lista resultante.
    '''

    def intersecao(lista1:'Lista', lista2:'Lista')->'Lista': #O(n1*n2)
        resultado = Lista()
        cursor1 = lista1.__head
        cursor2 = lista2.__head
        for _ in range(len(lista1)):
            for _ in range(len(lista2)):
                if cursor1.carga == cursor2.carga:
                    resultado.insereFim(cursor1.carga)
                    break
                cursor2 = cursor2.proximo
            cursor1 = cursor1.proximo, cursor2 = lista2.__head

        return resultado

    def uniao(lista1:'Lista', lista2:'Lista')->'Lista': #O(n1+n2)
        resultado = Lista()
        cursor1 = lista1.__head
        cursor2 = lista2.__head

        for _ in range(len(lista1)):
            resultado.insereFim(cursor1.carga)
            cursor1 = cursor1.proximo

        for _ in range(len(lista2)):
            resultado.insereFim(cursor2.carga)
            cursor2 = cursor2.proximo

        return resultado

    def diferenca(lista1:'Lista', lista2:'Lista')->'Lista':
        resultado = Lista()
        cursor1 = lista1.__head, cursor2 = lista2.__head
        flag = True
        #todos os elementos que tem em lista1 e não tem em lista2
        for _ in range(len(lista1)):
            for _ in range(len(lista2)):
                if cursor1.carga == cursor2.carga:
                    flag = False
                cursor2 = cursor2.proximo
            if flag: 
                resultado.insereFim(cursor1.carga)
            
            cursor1 = cursor1.proximo, cursor2 = lista2.__head
        
        #Todos os elementos que tem em lista2 e não tem em lista1
        flag = True
        cursor1 = lista1.__head
        cursor2 = lista2.__head
        for _ in range(len(lista2)):
            for _ in range(len(lista1)):
                if cursor1.carga == cursor2.carga:
                    flag = False
                cursor1 = cursor1.proximo
            if flag: 
                resultado.insereFim(cursor2.carga)
            
            cursor1 = lista1.__head
            cursor2 = cursor2.proximo

        return resultado


    def __str__(self)->str:
        s = 'lista->[ '

        cursor = self.__head
        while( cursor != None):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo

        s = s.strip(', ')
        s += ' ]'
        return s