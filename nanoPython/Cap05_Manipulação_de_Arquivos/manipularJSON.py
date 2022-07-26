import json
inventario={}
opcao=int(input('Digite: \n "1" para registrar ativo\n "2" para exibir ativos armazenados: '))
while opcao>0 and opcao<3:
    if opcao==1:
        resp='S'
        while resp=='S':
            inventario[input('Digite o número patrimonial: ')]=[input('Digite a data da última atualização: '),input('Digite a descrição: '),input('Digite o departamento: ')]
            resp=input('Digite "S" para continuar: ').upper()
        with open('inventarioJSON.json','w')as arq_json:
            json.dump(inventario,arq_json)
        print('JSON gerado!')
    elif opcao==2:
        with open('inventarioJSON.json','r')as arq_json:
            resultado=json.load(arq_json)
            for chave,dado in resultado.items():
                print(f'Data.........: {dado[0]}')
                print(f'Descrição....: {dado[1]}')
                print(f'Departamento.: {dado[2]}')
    opcao=int(input('Digite: \n "1" para registrar ativo\n "2" para exibir ativos armazenados: '))