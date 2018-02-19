import sqlite3

con = sqlite3.connect('banco.db')
cur = con.cursor()

sql1 = """
CREATE TABLE IF NOT EXISTS pessoa(idpessoa INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  nome TEXT NOT NULL,
                                  peso REAL NOT NULL,
                                  altura REAL NOT NULL,
                                  sexo TEXT NOT NULL,
                                  tdee REAL NOT NULL
                                  )"""
sql2 ="""
CREATE TABLE IF NOT EXISTS alimenta(idalimenta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    descricao TEXT NOT NULL,
                                    caloria REAL NOT NULL,
                                    data TEXT NOT NULL,
                                    id_pessoa INT NOT NULL,
                                    FOREIGN KEY (id_pessoa) REFERENCES pessoa(idpessoa)
                                    )"""

cur.execute(sql1)
con.commit()
con.close()
