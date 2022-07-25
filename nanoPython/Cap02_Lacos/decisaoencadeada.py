nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_contagiosa = input("Suspeita de doença contagiosa? ").upper()
if idade >= 65:
    print("Paciente com prioridade")
    if doenca_contagiosa == "SIM":
        print("Encaminhe o paciente para a sala amarela")
    elif doenca_contagiosa == "NAO":
        print("Encaminhe o paciente para a sala branca")
    else:
        print("Responda a doença contagiosa com SIM ou NAO")
else:
    print("Paciente sem prioridade")
    if doenca_contagiosa == "SIM":
        print("Encaminhe o paciente para a sala amarela")
    elif doenca_contagiosa == "NAO":
        print("Encaminhe o paciente para a sala branca")
    else:
        print("Responda a suspeita de doença contagiosa com SIM ou NAO")