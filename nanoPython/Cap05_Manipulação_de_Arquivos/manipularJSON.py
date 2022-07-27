from funcoesJSON import *

inventario=lerArquivo('inventarioJSON.json')
opcao=chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario,'inventarioJSON.json'))
    elif opcao==2:
        exibir('inventarioJSON.json')
    opcao=chamarMenu