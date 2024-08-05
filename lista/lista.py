import lista_sequencial as l
#import lista_encadeada as l

def titulo():
    msg = "Editor de Listas"
    print(msg, "-"*len(msg), sep='\n')

def menu():
    print('''
1 - Tamanho
2 - Inserir
3 - Inserir no Início
4 - Inserir no Fim
5 - Remover
6 - Remover no Início
7 - Remover no Fim
8 - Remover Ocorrências
9 - Exibir elemento
10 - Procurar valor
11 - Modificar
12 - Esvaziar
13 - Maiores
14 - Sair 
''')
    
def main():
    lista = l.Lista()

    print(lista)
    titulo()
    menu()
    op = int(input('Digite sua opção: '))
    while(op!=14):
        if op == 1:
            print(f"O tamanho da lista é {len(lista)}.")
        elif op == 2:
            posicao = int(input("Em que posição deseja inserir?"))
            carga = input("Qual é a carga?")
            lista.inserir(posicao, carga)
        elif op==3:
            carga = input("Qual é a carga que você deseja inserir?")
            lista.insereInicio(carga)
        elif op==4:
            carga = input("Qual é a carga que você deseja inserir?")
            lista.insereFim(carga)
        elif op==5:
            posicao = int(input("Em qual posição deseja remover?"))
            lista.remover(posicao)
        elif op==6:
            lista.removeInicio()
        elif op==7:
            lista.removeFinal()
        elif op==8:
            carga = input("Qual é a carga que você deseja remover?")
            lista.removeOcorrencias(carga)
        elif op==9:
            posicao = int(input("Qual é a posição do elemento que deseja exibir?"))
            print(f"O elemento na posição {posicao} é {lista.elemento(posicao)}.")
        elif op==10:
            carga = input("Qual elemento deseja procurar?")
            print(f"{carga} está na posição {lista.busca(carga)}.")
        elif op==11:
            posicao = int(input("Qual posição deseja modificar?"))
            carga = input("Qual é a carga?")
            lista.modificar(posicao, carga)
        elif op==12:
            lista.esvaziar()
        elif op==13:
            n = int(input('Maiores do que quanto? '))
            print(f'Tem {lista.maiores(n)} nós com valores maiores do que {n}!')
            
        print()
        print(lista)
        titulo()
        menu()
        op = int(input('Digite sua opção: '))


if __name__ == "__main__":
    main()