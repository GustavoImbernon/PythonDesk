# -*- coding: iso-8859-1 -*-
from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent='wazeyes')

endereco=input('Digite um endereço com número e cidade.\n Exemplo: avenida paulista,100 São Paulo: ')
resultado=str(geolocator.geocode(endereco)).split(',')

if resultado[0] !='None':
    print(f'Endereço completo.: {resultado[0]}')
    print(f'Bairro............: {resultado[1]}')
    print(f'Cidade............: {resultado[2]}')
    print(f'Regiao............: {resultado[3]}')