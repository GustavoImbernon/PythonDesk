paciente = input('Insira o nome do paciente: ')
idade = int(input('Insira a idade do paciente: '))
if idade >=65:
    print(f'O paciente {paciente} possui atendimento prioritário!')
else:
    print(f'O paciente {paciente} não possui atendimento prioritário!')
    