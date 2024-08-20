import os
#atividade
def exibir():
    print('RESTAURANTE DA ADOLFO')
    
def opçoes():
    print('1.cadastrar restaurante')
    print('2.lista restaurante')
    print('3.ativar restaurante')
    print('4.sair/n')
        
#criando funcao
def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear') #usando o comando do sistema operacional de limpar o console
    print('finalizando app')
    
# def escolher_opcao():
#     opcao=int(input('escolher uma opçao'))
#     if opcao==1:
#         print('1.cadastrar restaurante')
#     elif opcao==2:
#         print('2.lista restaurante')
#     else:
#         finalizar_app()
            
def escolher_opcao():
    opcao=input('escolha uma opcao:')
    #e o switch
    match opcao:
        case '1':
            print('1.cadastrar restaurante')
        case '2':
            print('2.litar restaurante')
        case '3' :
            print('3.ativar restaurante')
        case _:#e o default do switch
             finalizar_app()  
             
             
def main():
    exibir()
    opçoes()
    escolher_opcao()
    
if __name__== '__main__':
    main()