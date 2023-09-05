from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from collections import Counter
import re
import time
import pyautogui
import random
import winsound

pyautogui.PAUSE = 2

def entra_site_loja(link_preco):

    # Essa função é específica para o site "https://www.maisapato.com.br/"
    nome = navegador.find_element(By.XPATH, '//*[@id="product_addtocart_form"]/div[2]/div[2]/div[1]/h1').text
    # Extrai o texto do elemento e imprime
    codigo_element = navegador.find_element(By.XPATH, '//div[@class="std"]/p/strong[contains(text(), "CÓDIGO")]')
    cod = codigo_element.text

    print(f'\n**********   {nome}  /  {cod}  **********\n')

    # Localizar o elemento usando XPath
    elemento = navegador.find_element(By.XPATH, link_preco)

    # Obter o texto do elemento
    texto_elemento = elemento.text

    # Remover caracteres não numéricos
    valor_formatado = re.sub(r'[^\d.,]+', '', texto_elemento)
    # Converter para float
    valor_float = float(valor_formatado.replace(',', '.'))
    # Realizar o cálculo
    valor_float += 65.00
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<          MUDE O VALOR AQUI       >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    valor_final = valor_float * 1.25
    # Formatar o valor com duas casas decimais
    valor_formatado = '{:.2f}'.format(valor_final)
    # Imprimir o resultado
    print(f"VALOR COM 35% => R${valor_formatado}\n")

    # Aguardar um pouco para garantir que a página carregue completamente
    time.sleep(2)

    # Encontra o elemento select usando XPath
    select_element = navegador.find_element(By.XPATH, '//*[@id="attribute145"]')

    # Encontra todos os elementos option dentro do select
    opcoes = select_element.find_elements(By.TAG_NAME, 'option')

    # Criar listas para armazenar os tamanhos, saldos, números disponíveis e números indisponíveis
    tamanhos_saldos = []
    disponiveis = []
    indisponiveis = []
    todos_tamanho = []
    codigo = []
    estoque_total = 0
    # Extrair os tamanhos, saldos e separar em disponíveis e indisponíveis
    for opcao in opcoes:
        valor = opcao.get_attribute('value')
        if valor:
            tamanho_estoque = opcao.text.split(' - Estoque: ')
            if len(tamanho_estoque) == 2:
                tamanho = tamanho_estoque[0].split(': ')[1]
                estoque = int(tamanho_estoque[1])

                if estoque > 1:
                    tamanhos_saldos.append((tamanho, estoque))
                    estoque_total += estoque
                    disponiveis.append(tamanho)

                    todos_tamanho.append(tamanho)
    print(f"(Numero - saldo) {tamanhos_saldos}")
    print(f"Números listados: {todos_tamanho}")
    print(f"Saldo total {estoque_total}")

    return [valor_formatado, todos_tamanho, disponiveis,tamanhos_saldos,cod]


def fazer_login_yampi(email, senha):
    # servico = Service(ChromeDriverManager().install())
    # navegador = webdriver.Chrome(service=servico)
    navegador = webdriver.Chrome()
    navegador.get(url)
    navegador.find_element(By.XPATH, xpath1).send_keys(email)
    navegador.find_element(By.XPATH, xpath2).send_keys(senha)
    navegador.find_element(By.XPATH, xpath3).click()
    return navegador

# Função para alterar produto na Yampi
def entrar_pag_Yampi_produto(navegador_yampi, dados_produtos):
    pyautogui.click(x=978, y=22)
    # Entra na página de produtos
    wait = WebDriverWait(navegador_yampi, 20)
    link_produtos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu"]/li[6]/a')))
    link_produtos.click()

    # Clica no botão de páginas
    link_paginas = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/main/div/div[1]/div/div[3]/div/div[1]/div[1]/div/div/input')))
    link_paginas.click()
    time.sleep(2)  # Aguarda 2 segundos

    # Clica no botão 50 da página
    elemento_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="50"]')))
    elemento_dropdown.click()

    time.sleep(1)  # Aguarda 2 segundos



    for dados_produto in dados_produtos:
        valor_atualizado = dados_produto['valor']
        produto_xpath = dados_produto['produto_xpath']
        qtd_numeros = dados_produto['qtd_numeros']
        disponiveis = dados_produto['disponiveis']
        tamanho_saldo = dados_produto['tamanho_saldo']
        codigos = dados_produto['list_codigo']
        #time.sleep(2)
        # Clique no link do produto escolhido
        link_produto = wait.until(EC.presence_of_element_located((By.XPATH, produto_xpath)))
        #time.sleep(2)
        link_produto.click()

# ************************************** ATUALIZA  DISPONIBILIDADE ********************************************************************************************************
        for opcao in opcoes_escolhidas:
            if '1' in opcao:
                #tenho que fazer ele excluir os que não estão na lista
                time.sleep(2)
                # Encontrar a tabela pelo seletor CSS
                table = navegador_yampi.find_element("css selector", ".table-skus")

                # Encontrar todas as linhas da tabela
                rows = table.find_elements("tag name", "tr")

                # Excluir a primeira linha (cabeçalho) se necessário
                data_rows = rows[1:]

                # Contar o número de linhas de dados na tabela
                numero_de_linhas = len(data_rows)
                if numero_de_linhas < len(disponiveis):
                    print(f'\n<<<<<<<<  O PRODUTO {codigos} PRECISA SER VERIFICADO: >>>>>>>>:\n')
                    print("Número de variações na sua loja é:", numero_de_linhas)
                    print("Número de variações no fornecedor é", len(disponiveis))
                    print('Ou seja o fonecedor incluiu mais uma variações !!!')

                for i in range( numero_de_linhas -1):
                    # Pega o elemento de texto do número do calçado para comparar se está na lista de disponíveis
                    time.sleep(2)  # Aguarda 1 segundo
                    elemento_numero = navegador_yampi.find_element(By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[3]/div/span[2]')
                    numero_calçado = elemento_numero.text

                    if numero_calçado not in disponiveis:
                        # Clique no link de editar a opção
                        link_opcao = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[7]/div/a')))
                        time.sleep(2)  # Aguarda 1 segundo
                        link_opcao.click()
                        # clica no botão sim e não
                        time.sleep(2)  # Aguarda 1 segundo
                        pyautogui.click(x=816, y=411)
                        time.sleep(1)  # Aguarda 1 segundo
                        pyautogui.click(x=1350, y=143)

# ************************************** ATUALIZA  DISPONIBILIDADE ********************************************************************************************************

#************************************** ATUALIZA  PREÇO ********************************************************************************************************
        cont_para_x2 = 0
        tamanho = qtd_numeros
        num_caracteres = len(valor_atualizado) * -1
        for opcao in opcoes_escolhidas:
            if '2' in opcao:
                for i in range(tamanho):
                    price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[5]/div')))
                    price = price_element.text[num_caracteres:].replace(',', '.')

                    if price != valor_atualizado:
                        # Clique no link de editar a opção
                        link_opcao = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[7]/div/button')))
                        time.sleep(1)  # Aguarda 1 segundo
                        link_opcao.click()

                        # Supondo que 'valor_atualizado' seja uma string que contém o valor atualizado como '165.00'
                        valor1 = float(valor_atualizado)
                        x = round((valor1 - 65) / 1.25, 2)  # Arredonda para duas casas decimais
                        x = '{:.2f}'.format(x)
                        x = str(x)

                        campo_input = navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation-content"]/div[1]/div[3]/div/div[1]/div[1]/input')
                        campo_input.clear()  # Limpa o input
                        campo_input.send_keys((x).replace('.', ''))

                        if cont_para_x2 == 0:
                            cont_para_x2 += 1
                            # Gere um número aleatório entre 1.15 e 1.85
                            random_factor = random.uniform(1.15, 1.85)

                            # Calcule o resultado usando o valor aleatório
                            x2 = valor1 * random_factor

                            x2 = '{:.2f}'.format(x2)
                        #time.sleep(2)
                        campo_input = navegador_yampi.find_element(By.XPATH, '//*[@id="modal-variation-content"]/div[1]/div[3]/div/div[2]/div/input')
                        campo_input.clear()  # Limpa o input
                        campo_input.send_keys((x2).replace('.', ''))

                        campo_input = navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation-content"]/div[1]/div[3]/div/div[3]/div/input')
                        campo_input.clear()  # Limpa o input
                        campo_input.send_keys(valor_atualizado)

                        # Salva a opção
                        navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation"]/div/form/div/div[2]/p/button[2]').click()

# ************************************** ATUALIZA  PREÇO  ********************************************************************************************************

        # ************************************** CAMADA DA FUNÇÃO ATUALIZA  SALDO  ********************************************************************************************************
        for opcao in opcoes_escolhidas:
            if '3' in opcao:
                atuliza_saldo_yampi(tamanho_saldo,tamanho,navegador_yampi)

        # ************************************** CAMADA DA FUNÇÃO ATUALIZA  SALDO  ********************************************************************************************************

        navegador_yampi.back()
        global pag
        pag += 1
        # if pag % 6 == 0:
        #     pyautogui.click(x=84, y=51)
        #     time.sleep(5)
        if codigos == "CÓDIGO 8508":
            # Clica no botão 2  50 da página
            PAG2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/main/div/div[1]/div/div[3]/div/div[2]/div/div/ul/li[2]')))
            PAG2.click()
        elif codigos == "CÓDIGO 8604":
            # Clica no botão 3  50 da página
            PAG2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/main/div/div[1]/div/div[3]/div/div[2]/div/div/ul/li[3]')))
            PAG2.click()
        elif codigos == "CÓDIGO 8531":
            # Clica no botão 3  50 da página
            PAG2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/main/div/div[1]/div/div[3]/div/div[2]/div/div/ul/li[4]')))
            PAG2.click()
        time.sleep(5)
        print(f'Item {pag} com código {codigos} atualizado com sucesso !')
    navegador_yampi.quit()
    #time.sleep(3)


# ************************************** FUNÇÃO ATUALIZA  SALDO  ********************************************************************************************************
def atuliza_saldo_yampi(tamanho_saldo, tamanho,navegador_yampi):
    pyautogui.PAUSE = 1
    for _ in range(5):
        pyautogui.press('pgup')

    #time.sleep(2)
    pyautogui.click(x=574, y=332)


    pyautogui.click(x=587, y=687)
    pyautogui.hotkey('ctrl', 'a')
    # Apaga o texto selecionado (tecla DELETE)
    pyautogui.press('delete')

    for i in range(tamanho):
        pyautogui.PAUSE = 0.10
        texto_para_inserir = str(tamanho_saldo[i][1])
        # Digita o conteúdo no input
        pyautogui.typewrite(texto_para_inserir)

        for _ in range(7):
            pyautogui.press('tab')

    pyautogui.PAUSE = 1
    #time.sleep(2)
    pyautogui.click(x=1350, y=143)
    navegador_yampi.back()

# ************************************** FUNÇÃO ATUALIZA  SALDO  ********************************************************************************************************




def funcao_principal(produtos, link_preco, dados_produtos):
    for produto in produtos:
        produto_xpath = produto['produto_xpath']

        retorno = entra_site_loja(link_preco)
        valor35 = retorno[0]
        numeros = retorno[1]
        disponiveis = retorno[2]
        Tamanho_Saldo = retorno[3]
        codigo = retorno[4]
        qtd_numeros = len(numeros)

        dados_produto = {
            'valor': valor35,
            'produto_xpath': produto_xpath,
            'qtd_numeros': qtd_numeros,
            'disponiveis':  disponiveis,
            'tamanho_saldo': Tamanho_Saldo,
            'list_codigo': codigo
        }

        dados_produtos.append(dados_produto)
    return dados_produtos

# ************************************************************* INICIO DO PROGRAMA *************************************************************

#********************************* MENU ********************************************************************************

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


#********************************* MENU ********************************************************************************

# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)
navegador = webdriver.Chrome()

email = 'fernandojukcunha@gmail.com'
senha = input('Digite sua Senha')
url = "https://app.yampi.com.br/"
xpath1 = '//*[@id="app"]/div[2]/div/div/div/form/div[1]/input'
xpath2 = '//*[@id="app"]/div[2]/div/div/div/form/div[2]/input'
xpath3 = '//*[@id="app"]/div[2]/div/div/div/form/div[3]/button'
link_preco = '//*[@id="product_addtocart_form"]/div[2]/div[2]/div[4]/p[2]/span'
dados_produtos = []






pag = 0

# PROXIMO ->Maisapato **********   Sandália Salto Fino  /  CÓDIGO 8500  **********

#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-rosauva-lemon-carnelian-fivela')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-20375932"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->**********   Sandália Salto Fino  /  CÓDIGO 8549  **********
navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-branco-lemon')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20376175"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> **********   Sandália Salto Taça  /  CÓDIGO 8534  **********
navegador.get('https://www.maisapato.com.br/sandalia-salto-geometrico-cobra')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20377239"]/td[4]/a'
    }]

# ***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO -> **********   SANDÁLIA SALTO FLARE  /  CÓDIGO 8634  **********
# navegador.get('https://www.maisapato.com.br/sandalia-vinil-flare-rouge')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-20377316"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> **********   Mocassim  /  CÓDIGO 8590  **********
navegador.get('https://www.maisapato.com.br/mocassim-tratorado-off-corrente')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20528068"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8633
navegador.get('https://www.maisapato.com.br/sandalia-vinil-flare-ouro')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20647621"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

# PROXIMO ->8508

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-jeans')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20647651"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#************************pagina2****************7**************************************************************************************



# PROXIMO ->8550

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-preto-brilho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20647713"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8612

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-preto-laco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20647736"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8617

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-jeans-azul-elastico')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20647789"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8565
#
# navegador.get('https://www.maisapato.com.br/coturno-alto-off-ziper')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-20647950"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8532

navegador.get('https://www.maisapato.com.br/sandalia-salto-geometrico-cobre')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648028"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8615

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-elastico-offwhite')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648154"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8583
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-skinny-rosa-24263')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-20648196"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8596

navegador.get('https://www.maisapato.com.br/sandalia-salto-espelhada-roxo')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648211"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8506

navegador.get('https://www.maisapato.com.br/sandalia-taca-fivela-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648229"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8533

navegador.get('https://www.maisapato.com.br/sandalia-salto-geometrico-prata')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648694"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8633

navegador.get('https://www.maisapato.com.br/sandalia-vinil-flare-ouro')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20648714"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO ->8614
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-strass-vinil-preto-suede')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-20649415"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8620

navegador.get('https://www.maisapato.com.br/sandalia-fisherman-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20649668"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8621

navegador.get('https://www.maisapato.com.br/sandalia-fisherman-off')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20649709"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8051

navegador.get('https://www.maisapato.com.br/salto-corrente-vinil-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20649736"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->5000

navegador.get('https://www.maisapato.com.br/sandalia-salto-vinil-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20650126"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8640

navegador.get('https://www.maisapato.com.br/sandalia-3cm-flesh')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20650197"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8609

navegador.get('https://www.maisapato.com.br/sandalia-fivela-rosa-marfim-bloco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20650410"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8033

navegador.get('https://www.maisapato.com.br/salto-fino-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20650446"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8331

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-rosa-22421')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20650518"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#05-08-23

# PROXIMO ->8044

navegador.get('https://www.maisapato.com.br/sandalia-corrente-5-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20956257"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> 8199

navegador.get('https://www.maisapato.com.br/scarpin-azul')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20956285"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> 8052

navegador.get('https://www.maisapato.com.br/salto-corrente-vinil-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20956332"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> 8089

navegador.get('https://www.maisapato.com.br/sandalia-copinho-corrente-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20956535"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> 8061

navegador.get('https://www.maisapato.com.br/sandalia-aluminio-dourado-midi')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20957245"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

# PROXIMO -> 8431

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-spike-preto-dourado')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20957276"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO -> 8403

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-dourado')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20957349"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->7724

navegador.get('https://www.maisapato.com.br/scarpin-vinil-medio-vermelho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20957425"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

# PROXIMO ->8607

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-mint')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20957507"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8035

navegador.get('https://www.maisapato.com.br/salto-fino-bege')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20965067"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8150

navegador.get('https://www.maisapato.com.br/salto-corrente-preto-21164')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20965268"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8371

navegador.get('https://www.maisapato.com.br/sandalia-salto-apito-mogito-creme')
produtos = [
    {
        'produto_xpath': '//*[@id="item-20965352"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->7949

navegador.get('https://www.maisapato.com.br/saltofino-vermelho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21088138"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->7946

navegador.get('https://www.maisapato.com.br/sandalia-salto-vinil-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21088537"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8604

navegador.get('https://www.maisapato.com.br/coturno-off-brilho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21088782"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


#                                             ITEM    /*43/*

#PAGINA 3 ***********************************************************************************************************

# PROXIMO ->8432

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-spike-lemon')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21088867"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8501
#
# navegador.get('https://www.maisapato.com.br/scarpin-vinil-spike-lemon')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21089005"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8416

navegador.get('https://www.maisapato.com.br/scarpin-salto-vermelho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21089170"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8555    /*/*/*/*/*/*/*/*/*/ VER COMO SE COMPORTA POIS NÃO MARCA 36
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxssssssssssssssswwwwww----------------------------******************************')
navegador.get('https://www.maisapato.com.br/scarpin-pink-fino')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21089343"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO ->8599
#
# navegador.get('https://www.maisapato.com.br/sandalia-saltofino-laco-deserto')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21089379"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)

# PROXIMO ->8570

navegador.get('https://www.maisapato.com.br/sandalia-salto-grosso-cortica-laranja-amarrar')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21089761"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8034

navegador.get('https://www.maisapato.com.br/salto-fino-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21089809"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO ->8619
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-apito-preto-laco')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21089825"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)

# PROXIMO ->8349

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-grosso-lilas')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21090391"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8497

navegador.get('https://www.maisapato.com.br/scarpin-medio-verde-napa')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21090404"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8361

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-verniz-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21090438"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8618
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-apito-creme-laco')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21090455"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#

# PROXIMO ->8383

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-amarrar-rosa-pitaya')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21090505"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO ->8498
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-cortica-branco-fivela')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21090525"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#

# PROXIMO ->8540

navegador.get('https://www.maisapato.com.br/scarpin-aberto-rosa-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21090614"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8372

navegador.get('https://www.maisapato.com.br/sandalia-salto-apito-rosa-pitaya')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21527965"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8487

navegador.get('https://www.maisapato.com.br/sandalia-salto-skinny-vinil-rosa-lilas')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21528324"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#
# # PROXIMO ->8458
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-vulcao-rosa-23355')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21528559"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8580

navegador.get('https://www.maisapato.com.br/sandalia-bloco-azul')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21528623"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8452

navegador.get('https://www.maisapato.com.br/sandalia-triangulo-azul')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21528640"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8569

navegador.get('https://www.maisapato.com.br/sandalia-salto-grosso-cortica-rosa-amarrar')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529100"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8547

navegador.get('https://www.maisapato.com.br/sandalia-cilindro-blush-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529222"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8408

navegador.get('https://www.maisapato.com.br/sandalia-rasteira-amarrar-branco-22971')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529242"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

############################################################################################################################################################
# # PROXIMO ->8427

navegador.get('https://www.maisapato.com.br/sandalia-croco-salto-fino-verde')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529284"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#**************************inativo *********************************************
## # PROXIMO ->7741
#
# navegador.get('https://www.maisapato.com.br/sapatilha-franzida-branco')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21529365"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#**************************inativo *********************************************

# # PROXIMO ->8460
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-vulcao-azul')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21529544"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8491

navegador.get('https://www.maisapato.com.br/bota-meiapata-rust')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529666"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8451

navegador.get('https://www.maisapato.com.br/sandalia-salto-triangulo-mostarda')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529676"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8478

navegador.get('https://www.maisapato.com.br/sandalia-salto9-nude')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529698"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8587

navegador.get('https://www.maisapato.com.br/mocassim-tratorado-jeans-corrente')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529717"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8588

navegador.get('https://www.maisapato.com.br/mocassim-tratorado-jeans-brilho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529882"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8573

navegador.get('https://www.maisapato.com.br/scarpin-branco-petala')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529904"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8366

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-amarrar-vinil-verde-gisele')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529947"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8537

navegador.get('https://www.maisapato.com.br/bota-canoalto-jeans')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21529966"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8385

navegador.get('https://www.maisapato.com.br/sandalia-salto-flare-preto-verde')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530514"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8485

navegador.get('https://www.maisapato.com.br/coturno-salto6-marfim')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530533"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8373

navegador.get('https://www.maisapato.com.br/sandalia-salto-apito-deserto-marfim')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530557"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8582

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-sun')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530606"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


#**************************inativo *********************************************
# # PROXIMO ->8641
#
# navegador.get('https://www.maisapato.com.br/sandalia-3cm-candy')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21530703"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#**************************inativo *********************************************

# PROXIMO ->8362

navegador.get('https://www.maisapato.com.br/sandalia-rasteira-amarrar-preto-rafia')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530720"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8465

navegador.get('https://www.maisapato.com.br/bota-salto-grosso-rosa-bicofino')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530747"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8287

navegador.get('https://www.maisapato.com.br/sandalia-salto-skinny-rosa')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530948"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8246

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-vinil-amarrar-verde')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21530963"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8444

navegador.get('https://www.maisapato.com.br/sandalia-salto-triangulo-rosa')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21531185"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8637

navegador.get('https://www.maisapato.com.br/scarpin-medio-verniz-rosa-barbie')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21531197"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8567

navegador.get('https://www.maisapato.com.br/bota-meiapata-coturno-offwhite')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21531240"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8592

navegador.get('https://www.maisapato.com.br/sandalia-dregrade-preto-prata')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21531318"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8480

navegador.get('https://www.maisapato.com.br/bota-bicofino-salto9-croco-caramelo')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21531337"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)




#**************************inativo *********************************************
# # PROXIMO ->8548
#
# navegador.get('https://www.maisapato.com.br/sandalia-cilindro-rust-rosa-laranja-verde-metalizado')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21531490"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#**************************inativo *********************************************

# PROXIMO ->8531

navegador.get('https://www.maisapato.com.br/sandalia-gisele-roxo-iris')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532032"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)

#************************************************************ pag4 ****************************************************************
# PROXIMO ->8622

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-off-verniz')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532046"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8611

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-jeans-laco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532059"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8440

navegador.get('https://www.maisapato.com.br/sandalia-salto-taca-acrilico-rosa-bale')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532077"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8428

navegador.get('https://www.maisapato.com.br/sandalia-croco-salto-fino-branco')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532090"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8576

navegador.get('https://www.maisapato.com.br/sandalia-salto-grosso-holografico-dourado')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532100"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8608

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-off-white-escama')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532116"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8495

navegador.get('https://www.maisapato.com.br/scarpin-medio-lilas-napa')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532196"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8520

navegador.get('https://www.maisapato.com.br/scarpin-salto-fino-pink-vermelho')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532207"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8610

navegador.get('https://www.maisapato.com.br/sandalia-bloco-preto-suede')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532234"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8603

navegador.get('https://www.maisapato.com.br/coturno-brilho-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532320"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8499
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-cortica-rosa-dourado-fivela')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21532334"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#


# PROXIMO ->8426

navegador.get('https://www.maisapato.com.br/sandalia-croco-salto-fino-rosa')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21532351"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8585

navegador.get('https://www.maisapato.com.br/sandalia-cortica-vinil-ouro')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21551475"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8546

navegador.get('https://www.maisapato.com.br/sandalia-cilindro-cherry-azaleia-shock-iris')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21551589"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8577

navegador.get('https://www.maisapato.com.br/sandalia-salto-grosso-holografico-prata')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21551617"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# # PROXIMO ->8600
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-branco-zebra-laco')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21551637"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#


# PROXIMO ->8384

navegador.get('https://www.maisapato.com.br/sandalia-salto-bloco-amarrar-amarelo')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21551907"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)



# PROXIMO ->8050

navegador.get('https://www.maisapato.com.br/salto-corrente-vinil-dourado')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552183"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8161

navegador.get('https://www.maisapato.com.br/scarpin-medio-verniz-nude')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552197"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8605

navegador.get('https://www.maisapato.com.br/sandalia-salto-taca-fivela-nude')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552268"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8430

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-branco-cobre')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552586"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8598
#
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-zebra-laco-aloha')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21552602"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)


#PROXIMO ->8536

navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-holografico')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552654"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# PROXIMO ->8047

navegador.get('https://www.maisapato.com.br/sandalia-corrente-5-preto')
produtos = [
    {
        'produto_xpath': '//*[@id="item-21552691"]/td[4]/a'
    }]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)


# # PROXIMO ->8584
#
# navegador.get('https://www.maisapato.com.br/sandalia-skinny-branco')
# produtos = [
#     {
#         'produto_xpath': '//*[@id="item-21552701"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)

#\\\\\\\\\\\\\\\\\\\\\////////////////////////
            # fecha loja Tenis
navegador.quit()




def fazer_bip():
    frequency = 1000  # Frequência do som em Hz
    duration = 1000   # Duração do som em milissegundos
    winsound.Beep(frequency, duration)

# Chame a função para emitir um bip
fazer_bip()

# Continue com o restante do seu código
#***************************************************************
#Abre a yampi e faz Loguin                                      #
navegador_yampi = fazer_login_yampi(email, senha)               #
time.sleep(2)                                                   #
                                                                #
#Atualiza os daods
entrar_pag_Yampi_produto(navegador_yampi, dados_produtos)       #
                                                                #
#***************************************************************

#fecha o navegador Yampi
navegador_yampi.quit()


# Itera sobre os elementos da lista
# for produto in dados_produtos:
#     print("Dados do Produto:")
#     # Itera sobre as chaves e valores de cada dicionário
#     for chave, valor in produto.items():
#         print(f"{chave}: {valor}")
#     print()


