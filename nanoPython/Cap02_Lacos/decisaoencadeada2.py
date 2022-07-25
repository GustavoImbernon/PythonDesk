#INSERINDO VARIÁVEIS
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_contagiosa = input("Suspeita de doença contagiosa? ").upper()

#PRIMEIRO PROLEMA A SER RESOLVIDO
if doenca_contagiosa == "SIM":
    print("Encaminhe o paciente para a sala amarela")
elif doenca_contagiosa == "NAO":
    print("Encaminhe o paciente para a sala branca")

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade>10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")