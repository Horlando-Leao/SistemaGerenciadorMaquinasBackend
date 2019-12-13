import sqlite3
from sqlite3.dbapi2 import OperationalError
from sqlite3.dbapi2 import ProgrammingError

#from user import menu_user
#INSERÇÃO DOS DADOS
#DML : manipulação de dados

#decorador para abrir e fechar conexão no banco, ele aceita o retorno das funções em que o decorador esta.

def comitar_e_fechar_conexao(func):
    def decorator(*args):
        try:
            con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/maquinas.db")
            cur = con.cursor()
            sql = func(*args)
            cur.execute(sql)
            con.commit()
        finally:
            con.close
    return decorator

@comitar_e_fechar_conexao
def inserir_maquina_no_banco(nome, tipo_maquina, manutencao_preventiva, manutencao_corretiva, maquina_operante):
    try:
        if(nome == None) or (tipo_maquina == None):
            print('Espações vazios não poderaão ser gravados no disco')
        else:
            return """ 
            INSERT INTO maquinas(nome, tipo_maquina, manutencao_preventiva, manutencao_corretiva, maquina_operante)
            VALUES('{}', '{}', '{}') """.format(nome, tipo_maquina, manutencao_preventiva, manutencao_corretiva, maquina_operante)
    except OperationalError:
        print("você digitou um campo com valor invalido")
    except ValueError:
        print('digite valores alfhanumericos')
  
@comitar_e_fechar_conexao
def atualizar_maquina_no_banco(id_maquina, maquina_operante):
    try:
        if (id_maquina == None) or if( maquina_operante == None):
            print('Campo de pesquisa vazio não pode ser atualizado')
            print('Campo de pesquisa em email, precisa estar preenchido')
        else:
            return """
            UPDATE maquinas SET maquina_operante = '{}' WHERE id_maquina = '{}'
            """.format(maquina_operante, id_maquina)#Mude o nome se o email for igual a esse(email passado no parametro)
    except OperationalError as e:
            print("você digitou um campo com valor invalido")
            print("dados do erro: "+e)
        
@comitar_e_fechar_conexao
def excluir_maquina_no_banco(id_maquina):
    try:
        if(id_maquina == None):
            print('Campo de pesquisa vazio não pode ser excluido')
        else:
            return """
            DELETE FROM maquinas WHERE email ='{}'""".format(id_maquina)
    except OperationalError:
            print("você digitou um campo com valor invalido")

#não possui decorador porque não tem commit
def pesquisar_maquina_no_banco(valor_pesquisa, campo_pesquisa):
    try:
        if(valor_pesquisa_valid == None ) and (campo_pesquisa_valid == None):
            print('Valores em branco não poderam ser pesquisado')
        else:
            con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/maquinas.db")
            cur = con.cursor()
            sql = """
            SELECT id, nome, tipo_maquina, manutencao_preventiva, manutencao_corretiva, maquina_operante FROM maquinas WHERE {} = {}""".format(valor_pesquisa, campo_pesquisa)
            cur.execute(sql)
            valor_pesquisa = cur.fetchall()
            print(list(valor_pesquisa)) #valor encontrados no banco MOSTRAR NA TELA

            if valor_pesquisa == []:
                print('VALOR NÃO ENCONTRADO NA BASE DE DADOS')
            else:
                return valor_pesquisa

    except OperationalError as erro:
        print("você digitou um campo com valor invalido: ERRO =", erro)
    except ProgrammingError as erro:
        print("Você digitou um simbolo que não é valido: ERRO =", erro)
    finally:
        con.close

def buscar_maquinas_com_defeito_ou_sem_defeitos(defeito, valor_pesquisa, campo_pesquisa = 'maquina_operante'):
    if (defeito == 'perfeita'):
        try:
            con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/maquinas.db")
            cur = con.cursor()
            sql = """
            SELECT maquina_operante FROM maquinas WHERE {}={}""".format(valor_pesquisa, campo_pesquisa)
            cur.execute(sql)
            valor_pesquisa = cur.fetchall()
            print(list(valor_pesquisa)) #valor encontrados no banco MOSTRAR NA TELA
            
            if valor_pesquisa == []:
                print('VALOR NÃO ENCONTRADO NA BASE DE DADOS')
            else:
                return valor_pesquisa
        except OperationalError as erro:
            print("você digitou um campo com valor invalido: ERRO =", erro)
        except ProgrammingError as erro:
            print("Você digitou um simbolo que não é valido: ERRO =", erro)
        finally:
            con.close
    elif (defeito == 'imperfeito'):
        try:
            con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/maquinas.db")
            cur = con.cursor()
            sql = """
            SELECT maquina_operante FROM maquinas WHERE {}={}""".format(valor_pesquisa, campo_pesquisa)
            cur.execute(sql)
            valor_pesquisa = cur.fetchall()
            print(list(valor_pesquisa)) #valor encontrados no banco MOSTRAR NA TELA
            if valor_pesquisa == []:
                print('VALOR NÃO ENCONTRADO NA BASE DE DADOS')
            return valor_pesquisa
        except OperationalError as erro:
            print("você digitou um campo com valor invalido: ERRO =", erro)
        except ProgrammingError as erro:
            print("Você digitou um simbolo que não é valido: ERRO =", erro)
        finally:
            con.close
    else:
        print('voce precisa selecionar uma opção')












