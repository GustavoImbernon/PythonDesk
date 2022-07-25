# INSERINDO VARIAVEIS
resposta = "SIM"
while resposta == "SIM":
    nivel_de_acesso = input(
        "Insira o nivel de acesso (ADM, USR ou GUEST): ").upper()
    if nivel_de_acesso == "ADM" or nivel_de_acesso == "USR":
        genero = input("Insira seu gênero: ").upper()
        if nivel_de_acesso == "ADM":
            if genero == "FEMININO":
                print("Olá administradora")
            else:
                print("Olá administrador")
        else:
            if genero == "FEMININO":
                print("Olá usuária")
            else:
                print("Olá usuário")
    elif nivel_de_acesso == "GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido")
    resposta = input("Digite SIM para continuar: ").upper()
