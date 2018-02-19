import sqlite3

'''
    Trabalhando com a tabela pessoa: INSERTS, UPDATES, SELECTS.
'''

def commit_close(func):
    def decorator(* agrs):
        con = sqlite3.connect('banco.db')
        cur = con.cursor()
        sql = func(*agrs)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def bd_insert(nome, peso, altura, sexo, tdee): # Insere no banco#
    return """
    INSERT INTO pessoa (nome, peso, altura, sexo, tdee)
        VALUES('{}', {}, {}, '{}', {})
    """.format(nome, peso, altura, sexo, tdee)

@commit_close
def bd_update_peso(peso, nome): # Altera o peso #
    return """ UPDATE pessoa SET peso = {} WHERE nome = '{}'
    """.format(peso, nome)

@commit_close
def bd_update_tdee(tdee, nome): # Altera o tdee #
    return """ UPDATE pessoa SET tdee = {} WHERE nome = '{}'
    """.format(tdee, nome)


def bd_select_dados (ide): # Traz um usuario pesquisado#
    con = sqlite3.connect('banco.db')
    cur = con.cursor()
    sql = 'SELECT * FROM pessoa WHERE idpessoa = ?'
    for val in cur.execute(sql, (ide, )):
        print(val)


'''
 Trabalahndo com a tabela alimentar: INSERTS, UPDATES, SELECTS.
'''


def insert_Alimento(descricao, caloria, datas, id_pessoa): # Usuario realiza refeição#
    con = sqlite3.connect('banco.db')
    cur = con.cursor()
    sql ="""
    INSERT INTO alimenta(descricao, caloria, datas, id_pessoa)
        VALUES('{}', {}, '{}', {})
    """.format(descricao, caloria, datas, id_pessoa)
    cur.execute(sql)
    con.commit()
    con.close()


def select_cal(datas, ide): # Procura todos os alimentos cosumidos no dia #
    listaRetorno = []
    con = sqlite3.connect('banco.db')
    cur = con.cursor()
    sql = 'SELECT * FROM alimenta WHERE datas = ? and id_pessoa = ?'
    for val in cur.execute(sql, (datas, ide)):
        listaRetorno.append(val)
    return listaRetorno