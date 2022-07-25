nome = input("Insira o nome: ")
idade = int(input("Insira a idade: "))
prioridade = "NÃO"
if idade >=65:
    prioridade ="SIM"
print(f"O paciente {nome} possui atendimento prioritário?\n{prioridade}")
