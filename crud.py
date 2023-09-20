import mysql.connector

def cria_conexao():
    conexao = mysql.connector.connect(
        host= '108.167.132.244',
        user='nycofi04_nico',
        password='',  colocque sua senha
        database='nycofi04_banco1_nicofifer.com',
    )

    # Criar um cursor
    cursor = conexao.cursor()
    return conexao, cursor

# # *******************************  Exemplo de inserção de dados   *************************************
def inserir_dados(cursor,nome,saldo,valor):
    insercao = "INSERT INTO produto (nome,saldo,valor) VALUES (%s, %s, %s)"
    valores = (nome, saldo, valor)
    cursor.execute(insercao, valores)
    conexao.commit()  # Não esqueça de confirmar as alterações

# *******************************  Exemplo de consulta SELECT  *************************************
def select(cursor):
    consulta = "SELECT * FROM produto"
    cursor.execute(consulta)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()
    #for linha in resultados:
        #valor = linha[0]
        #print(linha)
        # linha_formatada = ', '.join(map(str, linha))
        # print(linha_formatada)
    # Iterar sobre os resultados e atribuir às variáveis
    for linha in resultados:
        id_produto = linha[0]
        nome = linha[1]
        saldo = linha[2]
        valor = linha[3]

        print("ID:", id_produto)
        print("Nome:", nome)
        print("Saldo:", saldo)
        print("Valor:", valor)
        print()  # Linha em branco entre os registros


# *******************************  Exemplo de atualização de dados  *************************************
def atulizar_dados(cursor,saldo,valor,id):
    novo_saldo = saldo
    novo_valor = valor
    id_produto_para_atualizar = id

    atualizacao = "UPDATE produto SET saldo = %s, valor = %s WHERE id = %s"
    valores_atualizacao = (novo_saldo, novo_valor, id_produto_para_atualizar)

    cursor.execute(atualizacao, valores_atualizacao)
    conexao.commit()

    print(f"Valores atualizados para o produto de ID {id_produto_para_atualizar}")


# *******************************  Exemplo de exclusão de dados *************************************
def exluir_pelo_id(cursor,id):
    exclusao = "DELETE FROM produto WHERE id = %s"
    valor_para_excluir = (f"{id}",)  # Adicione uma vírgula após o elemento
    cursor.execute(exclusao, valor_para_excluir)
    conexao.commit()

def excluir_todos_os_dados(cursor, tabela):
    exclusao = f"DELETE FROM {tabela}"
    cursor.execute(exclusao)
    conexao.commit()
    zera_auto_Incremente(cursor)

def zera_auto_Incremente(cursor):

    # Comando SQL para redefinir o auto incremento para 1
    comando_sql = "ALTER TABLE produto AUTO_INCREMENT = 1"

    # Executar o comando SQL
    cursor.execute(comando_sql)
    conexao.commit()


def fecha_conexao(conexao, cursor):
    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()


conexao, cursor = cria_conexao()


#zera_auto_Incremente(cursor)

inserir_dados(cursor, 'CALÇA JEANS', '20', '75.00')
#atulizar_dados(cursor,'50','200',1)
#exluir_pelo_id(cursor,4)
#excluir_todos_os_dados(cursor, 'produto')
select(cursor)

fecha_conexao(conexao, cursor)



#código para alterar o id para 1
#UPDATE `produto` SET `id` = '1' WHERE `produto`.`id` = 6;

#resetar o auto incremente
#ALTER TABLE nome_da_tabela AUTO_INCREMENT = 1;









#
# import mysql.connector
# from mysql.connector import Error
#
# try:
#     # Configurações de conexão com o banco de dados
#     conexao = mysql.connector.connect(
#             host= '108.167.132.244',
#             user='nycofi04_nico',
#             password='******',
#             database='nycofi04_banco1_nicofifer.com',
#     )
#
#     if conexao.is_connected():
#         print("Conexão bem-sucedida!")
#     else:
#         print("A conexão falhou.")
#
# except Error as e:
#     print("Erro ao conectar ao banco de dados:", e)
#
# finally:
#     # Certifique-se de fechar a conexão mesmo se ocorrer um erro
#     if conexao.is_connected():
#         conexao.close()
#         print("Conexão fechada.")
















#
#
#
# import mysql.connector
#
# conexao = mysql.connector.connect(
#     host= '108.167.132.244',
#     user='nycofi04_nico',
#     password='******',
#     database='nycofi04_banco1_nicofifer.com',
# )
#
# # Criar um cursor
# cursor = conexao.cursor()
# print(cursor)
# # Exemplo de consulta SELECT
# consulta = "SELECT * FROM produto"
# cursor.execute(consulta)
#
# # Recuperar os resultados da consulta
# resultados = cursor.fetchall()
# for linha in resultados:
#     print(linha)
#
#
#
# # Fechar o cursor e a conexão
# cursor.close()
# conexao.close()
#
#
#















# import mysql.connector
#
# # Configurações de conexão com o banco de dados
# conexao = mysql.connector.connect(
#     host='localhost',
#     user='seu_usuario',
#     password='sua_senha',
#     database='seu_banco_de_dados'
# )
#
# # Criar um cursor
# cursor = conexao.cursor()
#
# # Exemplo de consulta SELECT
# consulta = "SELECT * FROM nome_da_tabela"
# cursor.execute(consulta)
#
# # Recuperar os resultados da consulta
# resultados = cursor.fetchall()
# for linha in resultados:
#     print(linha)
#
# # Exemplo de inserção de dados
# insercao = "INSERT INTO nome_da_tabela (coluna1, coluna2) VALUES (%s, %s)"
# valores = ("valor1", "valor2")
# cursor.execute(insercao, valores)
# conexao.commit()  # Não esqueça de confirmar as alterações
#
# # Exemplo de atualização de dados
# atualizacao = "UPDATE nome_da_tabela SET coluna1 = %s WHERE coluna2 = %s"
# novos_valores = ("novo_valor", "valor_antigo")
# cursor.execute(atualizacao, novos_valores)
# conexao.commit()
#
# # Exemplo de exclusão de dados
# exclusao = "DELETE FROM nome_da_tabela WHERE coluna1 = %s"
# valor_para_excluir = ("valor_a_ser_excluido",)
# cursor.execute(exclusao, valor_para_excluir)
# conexao.commit()
#
# # Fechar o cursor e a conexão
# cursor.close()
# conexao.close()
