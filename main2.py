import os #importo os comandos do sistema operacional

def exibir():
    print('RESTAURANTE DA ADOLFO')

def opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')

#criando funcao
def finalizar_app():
    os.system('clear') #usando o comando do sistema operacional de limpar o console
    print ('finalizando app...')


    def escolher_opcao():
        opcao = int(input('escolha uma opção:      '))
    if opcao == 1:
        print ('1. cadastrar restaurante')
    elif opcao == 2:
        print ('2. listar restaurante')
    elif opcao ==3:
        print ('3. ativar restaurante')

    else: 
        finalizar_app()

def escolher(): 
    opcao = int (input('escolha uma opcao:  '))
    # é o switch
    match opcao:
        case 1:
            print ('1. cadastrar restaurante')
        case 2:
            print ('2. listar restaurante')
        case 3:
             print ('3. ativar restaurante')
        case _: # é o default no switch
            finalizar_app()
    

def main(): 
    exibir()
    opcoes()
    escolher_opcao()

# abaixo vai dizer que o esse código nao vai ser importado e que ele é o principal e vai executar o main

if __name__ == '__main__':
    main()
