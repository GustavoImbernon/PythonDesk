from funcoes import *
usuarios={}
opcao=perguntarMenu()
while opcao=='I' or opcao=='P' or opcao=='E' or opcao=='L':
    if opcao=='I':
        inserir(usuarios)
    if opcao=='P':
        pesquisar(usuarios, input('Digite o acesso que deseja pesquisar: '))
    if opcao=='E':
        excluir(usuarios, input('Digite o acesso que deseja excluir: '))
    if opcao=='L':
        listar(usuarios)
    opcao = perguntarMenu()