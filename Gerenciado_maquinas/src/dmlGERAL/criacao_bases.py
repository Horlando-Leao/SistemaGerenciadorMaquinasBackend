import sqlite3

path = r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/"

con = sqlite3.connect(path + r'maquinas.db')
cur = con.cursor()
sql = '''CREATE TABLE maquinas(
    id TEXT PRIMARY KEY,
    nome TEXT,
    tipo_maquina TEXT,
    manutencao_prenvetiva TEXT,
    manutencao_corretiva TEXT,
    maquina_operante TEXT
    )'''
cur.execute(sql)
con.commit()
con.close

#manutenção ** data e quem fez, separado por //
#
##=====================================================
#con = sqlite3.connect(path + r'funcionarios.db')
#cur = con.cursor()
#sql =  CREATE TABLE funcionarios(
#    cpf TEXT PRIMARY KEY,
#    nome_funcionario TEXT,
#    tipo_funcionario TEXT,
#    trabalho_realizado TEXT
#
#)
#
##manutenção ** data e quem fez, separado por //
#cur.execute(sql)
#con.commit()
#con.close
#