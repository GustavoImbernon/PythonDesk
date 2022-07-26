with open('economic-indicators.csv','r')as boston:
    total_voos=0
    maior=0
    total_passageiros=0
    maior_media_diaria=0
    ano_usuario=input('Insira o ano que deseja pesquisar: ')
    for linha in boston.readlines()[1:-1]:
        lista=linha.split(',')
        total_voos=total_voos+float(lista[3])
        if float(lista[2])>float(lista[3]):
            maior=lista[2]
            ano=lista[0]
            mes=lista[1]
        if ano_usuario==lista[0]:
            total_passageiros=total_passageiros+float(lista[2])
            if float(lista[5])>float(maior_media_diaria):
                maior_media_diaria=lista[5]
                mes_maior_diaria=lista[1]
    print(f'O total de voos é: {total_voos}')
    print(f'O mês/ano de maior movimento no aeroporto foi: {mes}/{ano}')
    print(f'O total de passageiros do ano {ano_usuario} foi de {total_passageiros}')
    print(f'O mês do ano {ano_usuario} com maior média para diária de hotel foi o mês {mes_maior_diaria}')