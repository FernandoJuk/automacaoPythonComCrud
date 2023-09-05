# Definindo um dicionário com opções e suas respectivas ações.
opcoes = {
    '1': {'descricao': 'Excluir variações indisponíveis', 'acao': 1 },
    '2': {'descricao': 'Atualizar Preço', 'acao': 2},
    '3': {'descricao': 'Atualizar Saldo', 'acao': 3}
}


# Definindo uma função para exibir o menu de opções.
def exibir_menu(opcoes):
    print("Escolha uma ou mais opções:")
    for key, value in opcoes.items():
        print(f"{key} - {value['descricao']}")
    print('0 - Sair')

# Iniciando um loop infinito para o menu.
op = 2
while True:
    if op == 1:
        break
    exibir_menu(opcoes)  # Chama a função para exibir o menu.
    opcoes_escolhidas = input('Digite as opções desejadas separadas por vírgulas (ou 0 para sair): ')

    if opcoes_escolhidas == '0':
        print("Operação cancelada.")
        break

    opcoes_escolhidas = opcoes_escolhidas.split(',')  # Divide as opções digitadas em uma lista.

    # Itera sobre as opções escolhidas pelo usuário.
    for opcao in opcoes_escolhidas:
        if opcao in opcoes:  # Verifica se a opção é válida.
            print(f'Voce escolheu: {opcoes[opcao]["descricao"]}')  # Exibe a ação correspondente à opção.
            op= 1
        else:
            print(f"Opção inválida: {opcao}")  # Informa que a opção é inválida.

for opcao in opcoes_escolhidas:
    if '1' in opcao:
        print('1 ok')
for opcao in opcoes_escolhidas:
    if '2' in opcao:
        print('2 ok')
for opcao in opcoes_escolhidas:
    if '3' in opcao:
        print('3 ok')


print('pulou')


# def funcao1():
#     print("Função 1 selecionada.")
#
# def funcao2():
#     print("Função 2 selecionada.")
#
# def funcao3():
#     print("Função 3 selecionada.")
#
# opcoes = {
#     '1': {'descricao': 'Função 1', 'funcao': funcao1},
#     '2': {'descricao': 'Função 2', 'funcao': funcao2},
#     '3': {'descricao': 'Função 3', 'funcao': funcao3}
# }
#
# def exibir_menu(opcoes):
#     print("Escolha uma ou mais opções:")
#     for key, value in opcoes.items():
#         print(f"{key} - {value['descricao']}")
#
# while True:
#     exibir_menu(opcoes)
#     opcoes_escolhidas = input('Digite as opções desejadas separadas por vírgulas (ou 0 para sair): ')
#
#     if opcoes_escolhidas == '0':
#         print("Operação cancelada.")
#         break
#
#     opcoes_escolhidas = opcoes_escolhidas.split(',')
#     opcoes_executadas = set()
#
#     for opcao in opcoes_escolhidas:
#         if opcao in opcoes:
#             opcoes_executadas.add(opcao)
#             opcoes[opcao]['funcao']()
#
#     if not opcoes_executadas:
#         print("Nenhuma opção válida selecionada. Retornando ao menu.")
#





# def funcao1():
#     print("Função 1 selecionada.")
#
# def funcao2():
#     print("Função 2 selecionada.")
#
# def funcao3():
#     print("Função 3 selecionada.")
#
# opcoes = {
#     '1': {'descricao': 'Função 1', 'funcao': funcao1},
#     '2': {'descricao': 'Função 2', 'funcao': funcao2},
#     '3': {'descricao': 'Função 3', 'funcao': funcao3}
# }
#
# def exibir_menu(opcoes):
#     print("Escolha uma ou mais opções:")
#     for key, value in opcoes.items():
#         print(f"{key} - {value['descricao']}")
#
# while True:
#     exibir_menu(opcoes)
#     opcoes_escolhidas = input('Digite as opções desejadas separadas por vírgulas (ou 0 para sair): ')
#
#     if opcoes_escolhidas == '0':
#         print("Operação cancelada.")
#         break
#
#     opcoes_escolhidas = opcoes_escolhidas.split(',')
#     opcoes_executadas = set()
#
#     for opcao in opcoes_escolhidas:
#         if opcao in opcoes:
#             opcoes_executadas.add(opcao)
#             opcoes[opcao]['funcao']()
#
#     if not opcoes_executadas:
#         print("Nenhuma opção válida selecionada. Retornando ao menu.")
#
#








# def funcao1():
#     print("Função 1 selecionada.")
#
# def funcao2():
#     print("Função 2 selecionada.")
#
# def funcao3():
#     print("Função 3 selecionada.")
#
# opcoes = {
#     '1': {'descricao': 'Função 1', 'funcao': funcao1},
#     '2': {'descricao': 'Função 2', 'funcao': funcao2},
#     '3': {'descricao': 'Função 3', 'funcao': funcao3}
# }
#
# def exibir_menu(opcoes):
#     print("Escolha uma ou mais opções:")
#     for key, value in opcoes.items():
#         print(f"{key} - {value['descricao']}")
#
# exibir_menu(opcoes)
# opcoes_escolhidas = input('Digite as opções desejadas separadas por vírgulas: ')
#
# opcoes_escolhidas = opcoes_escolhidas.split(',')
# opcoes_executadas = set()
#
# for opcao in opcoes_escolhidas:
#     if opcao in opcoes:
#         opcoes_executadas.add(opcao)
#         opcoes[opcao]['funcao']()
#
# if not opcoes_executadas:
#     print("Nenhuma opção válida selecionada.")