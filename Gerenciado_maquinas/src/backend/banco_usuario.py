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
            con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/funcionarios.db")
            cur = con.cursor()
            sql = func(*args)
            cur.execute(sql)
            con.commit()
        finally:
            con.close
    return decorator

@comitar_e_fechar_conexao
def inserir_usuario_no_banco(cpf, nome_funcionario, tipo_funcionario, trabalho_realizado):
    try:
        if(nome == "") or (telefone == "") or (email=="")or (nome == None) or (telefone == None) or (email== None):
            print('Espações vazios não poderaão ser gravados no disco')
        else:
            return """ 
            INSERT INTO usuarios(nome, telefone, email)
            VALUES('{}', '{}', '{}') """.format(nome, telefone, email)
    except OperationalError:
        print("você digitou um campo com valor invalido")
    except ValueError:
        print('digite valores alfhanumericos')
  
@comitar_e_fechar_conexao
def atualizar_usuario_no_banco(cpf, tipo_funcionario):
    try:
        nome_valid = True
        email_valid = True
        if(nome == ""):
            print('Campo de pesquisa vazio não pode ser atualizado')
            nome_valid = False
        if(email == ""):
            print('Campo de pesquisa em email, precisa estar preenchido')
            email_valid = False
        if(email_valid != False ) and (nome_valid != False):
            return """
            UPDATE usuarios SET nome = '{}' WHERE email = '{}'
            """.format(nome, email)#Mude o nome se o email for igual a esse(email passado no parametro)
    except OperationalError as e:
            print("você digitou um campo com valor invalido")
            print("dados do erro: "+e)
        
@comitar_e_fechar_conexao
def excluir_usuario_no_banco(cpf):
    try:
        if(email == ""):
            print('Campo de pesquisa vazio não pode ser excluido')
        else:
            return """
            DELETE FROM usuarios WHERE email ='{}'""".format(email)
    except OperationalError:
            print("você digitou um campo com valor invalido")

#não possui decorador porque não tem commit
def pesquisar_usuario_no_banco(valor_pesquisa, campo_solicitidao):
    
    try:
        if(valor_pesquisa == None ) or (campo == None):
            print(' Valor do Campo não pode estar em branco\n ou')
            print('Campo de pesquisa não pode estar vazio')
        else:
            try:
                con = sqlite3.connect(r"/home/horlando/Área de Trabalho/hack_cointer/base_dados/funcionarios.db")
                cur = con.cursor()
                sql = """
                SELECT id, nome, telefone, email FROM usuarios WHERE {}={}""".format(valor_pesquisa, campo)

                cur.execute(sql)
                valor_pesquisa = cur.fetchall()
                print(list(valor_pesquisa))

                if valor_pesquisa == []:
                    print('VALOR NÃO ENCONTRADO NA BASE DE DADOS')
                else:
                    return valor_pesquisa
            finally:
                con.close
                       
    except OperationalError as erro:
        print("você digitou um campo com valor invalido: ERRO =", erro)
    except ProgrammingError as erro:
        print("Você digitou um simbolo que não é valido: ERRO =", erro)