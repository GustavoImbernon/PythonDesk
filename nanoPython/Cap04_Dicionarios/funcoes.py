def perguntarMenu():
    resposta=input('O que deseja realizar?\n"I" - para inserir um usuário\n"P" - para pesquisar um usuário\n"E" - para Excluir um usuário\n"L" - para listar um usuário\n').upper()
    return resposta


def inserir(dicionario):
    dicionario[input('Insira o código do acesso: ').upper()] = [input('Digite o login do usuário: '),input("Digite o nome: ").upper(),input('Digite o nível do usuário: '),input("Digite a última data de acesso: "),input('Digite a hora do acesso: '),input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print('Login...........: ' + lista[0])
        print('Nome............: ' + lista[1])
        print('Nível...........: ' + lista[2])
        print('Último acesso...: ' + lista[3])
        print('Hora do acesso..: ' + lista[4])
        print('Última estação..: ' + lista[5])

def excluir(dicionario,chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print('Objeto eliminado!')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Objeto...')
        print('Código de acesso: ', chave)
        print('Dados: ', valor)