from comandos import bd_insert, bd_select_dados, bd_update_peso, bd_update_tdee
from comandos import insert_Alimento, select_cal
from pprint import pprint
import os

def caloria_bd(): # Total de calorias gasta no dia agrs #
    print('+--------------------------------------+')
    print('|           SYSTEM DATE                |')
    print('+--------------------------------------+')
    datas = input('Digite um data no modelo (xx/xx/xxxx): ')
    idpessoa = int(input('Digite o seu id: '))
    a = select_cal(datas, idpessoa)
    cont = 0
    total = 0
    for val in a:
        b = a[cont]
        calc = b[2]
        total += calc
        cont += 1
    if total > 0:
        bd_select_dados(idpessoa)
        print('+--------------------------------------+')
        print('| DATA: {}                     |'.format(datas))
        print('| CALORIAS TOTAIS: {} KCAL         |'.format(total))
        print('+--------------------------------------+')
    else:
        print('+--------------------------------------+')
        print('| DATA: {}                     |'.format(datas))
        print('| DATA INFORMADA INVALIDA              |'.format(total))
        print('+--------------------------------------+')


caloria_bd()

os.system('pause')

#bd_insert('JOSE MURILLO', 71.00, 1.73, 'MASC', 2000.00)
#insert_Alimento('FEIJOADA 220G', 650.00, '18/02/2018', 2)
#insert_Alimento('ARROZ 160G', 192.00, '18/02/2018', 1)
#insert_Alimento('OVO 2U', 90.00, '18/02/2018', 1)
#insert_Alimento('CHOCOLATE 90G', 200.00, '18/02/2018', 1)
