from comandos import bd_insert, bd_select_dados, bd_update_peso, bd_update_tdee
from comandos import insert_Alimento, select_cal, bd_delete
from comandos import alimento_delete, delete_alimento
from pprint import pprint
import os

def imprima_img(): # E so para acrentar imgs de interação  com o usuario#
    pass

def mostra_dados (lista_aux): # mostra os dados que recebeu#
    print('+--------------------------------------+')
    print('|            DADOS USUARIO             |')
    print('+--------------------------------------+')
    print('ID : {}'.format(lista_aux[0]))
    print('NOME : {}'.format(lista_aux[1]))
    print('PESO : {} KG'.format(lista_aux[2]))
    print('ALTURA : {} M'.format(lista_aux[3]))
    print('SEXO : {}'.format(lista_aux[4]))
    print('TDEE : {}'.format(lista_aux[5]))
    print('---------------------------------------')
    os.system('pause')
    os.system('cls')

def func_dados_usuario(): # Busca a tupla para mostra_dados #
    lista_aux = []
    id_pessoa = int(input('Digite o ID: '))
    pessoa = bd_select_dados(id_pessoa)
    if pessoa != None:
        for val in [0, 1, 2, 3, 4, 5]:
            lista_aux.append(pessoa[val])
        mostra_dados(lista_aux)
    else:
        imprima_img() # jaja implemento#
        print('ID: {} - [NAO TEM NENHUM USUARIO COM ESSE ID]'.format(id_pessoa))
        os.system('pause')
        os.system('cls')

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
        print(bd_select_dados(idpessoa))
        print('+--------------------------------------+')
        print('| DATA: {}                     |'.format(datas))
        print('| CALORIAS TOTAIS: {} KCAL         |'.format(total))
        print('+--------------------------------------+')
    else:
        print('+--------------------------------------+')
        print('| DATA: {}                     |'.format(datas))
        print('| DATA INFORMADA INVALIDA              |'.format(total))
        print('+--------------------------------------+')
    os.system('pause')
    os.system('cls')

def insert_a(): # Insere eu alimento de uma pessoa #
    print('+-----------------------------------+')
    print('|             ALIMENTO              |')
    print('+-----------------------------------+')
    descricao = input('DESCRICAO: ')
    calorias = float(input('CALORIAS: '))
    datas = input('DATA (xx/xx/xxxx): ')
    idpessoa = int(input('ID: '))
    insert_Alimento(descricao, calorias, datas, idpessoa)
    print('\n\n CONCLUIDO COM SUCESSO')
    os.system('pause')
    os.system('cls')

def func_update_usuario (): # jaja implemento#
    pass

def menu(): # menu #
    print('+----------------------------------------------------------------------+')
    print('|                              SYSTEM - MENU                           |')
    print('+----------------------------------------------------------------------+')
    print('|                 01 - Cadastrar                                       |')
    print('|                 02 - Alimenta-se                                     |')
    print('|                 03 - Consultar por Data                              |')
    print('|                 04 - Dados do usario                                 |')
    print('|                 05 - Editar                                          |')
    print('|                 06 - Deleta Alimento                                 |')
    print('|                 07 - Deletar Usuario                                 |')
    print('|                 08 - Sair                                            |')
    print('+----------------------------------------------------------------------+')

r = 0
while r != 8:
    menu()
    r = int(input('Digite: '))
    os.system('cls')
    if (r == 1):
        print('+-----------------------------------+')
        print('|       PAINEL DE CADASTRO          |')
        print('+-----------------------------------+')
        nome = input('NOME: ')
        peso = float(input('PESO: '))
        altura = float(input('ALTURA: '))
        sexo = input('SEXO: ')
        tdee = float(input('TDEE: '))
        bd_insert(nome, peso, altura, sexo, tdee)
        print('CADASTRO CONCLUIDO COM SUCESSO {}'.format(nome))
    elif (r == 2):
        insert_a()
    elif (r == 3):
        caloria_bd()
    elif (r == 4):
        func_dados_usuario()
    else:
        print('OPCAO INVALIDA OU INATIVA')

os.system('pause')

#bd_insert('JOSE MURILLO', 71.00, 1.73, 'MASC', 2000.00)
#insert_Alimento('FEIJOADA 220G', 650.00, '18/02/2018', 2)
#insert_Alimento('ARROZ 160G', 192.00, '18/02/2018', 1)
#insert_Alimento('OVO 2U', 90.00, '18/02/2018', 1)
#insert_Alimento('CHOCOLATE 90G', 200.00, '18/02/2018', 1)
#alimento_delete('SORVETE 200G', '19/02/2018')
#bd_delete(3)
#delete_alimento(2)
# deu tudo certo
