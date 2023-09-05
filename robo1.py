from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import time


def entra_site_loja(link_preco, cor):
    # Verifica se está disponível
    # Essa função é específica para o site "https://www.atacadobarato.com/"
    nome = navegador.find_element(By.ID, "product-name").text
    navegador.find_element(By.XPATH, cor).click()
    cor_selecionada = navegador.find_element(By.XPATH, cor)
    # Encontra o elemento h1 com o XPath
    elemento_h1 = navegador.find_element(By.XPATH, '//*[@id="product-name"]')
    nome_cor = cor_selecionada.get_attribute("data-name")
    # Extrai o texto do elemento e imprime
    print(f'**********   {elemento_h1.text} Cor: {nome_cor}   **********\n')


    elemento_div = navegador.find_element(By.XPATH, '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[2]/div')
    # print("Tag do elemento:", elemento_div.tag_name)
    # print("Texto do elemento:", elemento_div.text)
    # print("Atributos do elemento:", elemento_div.get_attribute("outerHTML"))
    links = elemento_div.find_elements(By.TAG_NAME, "a")

    numeros = []  # Lista vazia para armazenar os textos dos links
    indisponiveis = []
    disponiveis = []

    for link in links:
        link.click()
        texto_link = link.text
        numeros.append(texto_link)  # Adiciona o texto do link à lista

        elemento = navegador.find_element(By.XPATH,
                                          '//*[@id="single-product"]/div/div/div[3]/div[1]/div[1]/div[1]/div[2]')
        valor_display = elemento.value_of_css_property("display")

        if valor_display == "block":
            texto_link = link.find_element(By.TAG_NAME, "span").text
            indisponiveis.append(texto_link)  # Adiciona o texto do link à lista
        else:
            texto_link = link.find_element(By.TAG_NAME, "span").text
            disponiveis.append(texto_link)

    print(f"Dos números: {numeros}")
    print(f"Estão Indisponíveis: {indisponiveis}")
    print(f"Estão Disponíveis: {disponiveis}")


    # Localizar o elemento usando XPath
    elemento = navegador.find_element(By.XPATH, link_preco)

    # Obter o texto do elemento
    texto_elemento = elemento.text

    # Remover caracteres não numéricos
    valor_formatado = re.sub(r'[^\d.,]+', '', texto_elemento)
    # Converter para float
    valor_float = float(valor_formatado.replace(',', '.'))
    # Realizar o cálculo
    valor_final = valor_float * 1.35
    # Formatar o valor com duas casas decimais
    valor_formatado = '{:.2f}'.format(valor_final)

    # Imprimir o resultado
    print(f"VALOR COM 35% -> R${valor_formatado}\n")

    return [valor_formatado, nome_cor, numeros, indisponiveis, disponiveis, nome]


def fazer_login_yampi(email, senha):
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get(url)
    navegador.find_element(By.XPATH, xpath1).send_keys(email)
    navegador.find_element(By.XPATH, xpath2).send_keys(senha)
    navegador.find_element(By.XPATH, xpath3).click()
    return navegador

# Função para alterar produto na Yampi
def entrar_pag_Yampi_produto(navegador_yampi, dados_produtos):
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

    time.sleep(2)  # Aguarda 2 segundos

    for dados_produto in dados_produtos:
        valor_atualizado = dados_produto['valor']
        produto_xpath = dados_produto['produto_xpath']
        qtd_numeros = dados_produto['qtd_numeros']
        indisponiveis = dados_produto['indisponiveis']

        # Clique no link do produto escolhido
        link_produto = wait.until(EC.presence_of_element_located((By.XPATH, produto_xpath)))
        link_produto.click()

        tamanho = qtd_numeros
        num_caracteres = len(valor_atualizado) * -1
        for i in range(tamanho):

            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[5]/div')))
            price = price_element.text[num_caracteres:].replace(',', '.')

            if price != valor_atualizado:
                # Clique no link de editar a opção
                link_opcao = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[7]/div/button')))
                time.sleep(1)  # Aguarda 1 segundo
                link_opcao.click()

                campo_input = navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation-content"]/div[1]/div[2]/div/div[3]/div/input')
                campo_input.clear()  # Limpa o input
                campo_input.send_keys(valor_atualizado)

                # Salva a opção
                navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation"]/div/form/div/div[2]/p/button[2]').click()

            # Pega o elemento de texto do número do calçado para comparar se está na lista de disponíveis
            elemento_numero = navegador_yampi.find_element(By.XPATH,f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[3]/div/span[2]')
            numero_calçado = elemento_numero.text

            # Pega o texto do botão "SIM" ou "NÃO"
            elemento_botao = navegador_yampi.find_element(By.XPATH,f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[6]/div')
            texto_botao = elemento_botao.text
            time.sleep(1)  # Aguarda 1 segundo

            if numero_calçado in indisponiveis:
                if texto_botao == 'SIM':
                    # Clique no link de editar a opção
                    link_opcao = wait.until(EC.presence_of_element_located((By.XPATH,f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[7]/div/button')))
                    time.sleep(1)  # Aguarda 1 segundo
                    link_opcao.click()
                    # clica no botão sim e não
                    botao_sim = navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation-content"]/div[1]/div[1]/div[2]/div/div/label[2]/div')
                    botao_sim.click()
                    time.sleep(1)  # Aguarda 1 segundo
                    # Salva a opção
                    navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation"]/div/form/div/div[2]/p/button[2]').click()
            else:
                if texto_botao == 'NÃO':
                    # Clique no link de editar a opção
                    link_opcao = wait.until(EC.presence_of_element_located((By.XPATH,f'//*[@id="content-variation-skus"]/div[1]/table/tbody/tr[{i + 1}]/td[7]/div/button')))
                    time.sleep(1)  # Aguarda 1 segundo
                    link_opcao.click()
                    # clica no botão sim e não
                    botao_nao = navegador_yampi.find_element(By.XPATH,'//*[@id="modal-variation-content"]/div[1]/div[1]/div[2]/div/div/label[2]/div')
                    botao_nao.click()
                    time.sleep(1)  # Aguarda 1 segundo
                    # Salva a opção
                    navegador_yampi.find_element(By.XPATH, '//*[@id="modal-variation"]/div/form/div/div[2]/p/button[2]').click()
        navegador_yampi.back()
        time.sleep(5)
    navegador_yampi.quit()


def funcao_principal(produtos, link_preco, dados_produtos):
    for produto in produtos:
        cor = produto['cor']
        produto_xpath = produto['produto_xpath']

        retorno = entra_site_loja(link_preco, cor)
        valor35 = retorno[0]
        cor = retorno[1]
        numeros = retorno[2]
        indisponiveis = retorno[3]
        disponiveis = retorno[4]
        nome = retorno[5]
        qtd_numeros = len(numeros)

        dados_produto = {
            'Nome_do_tenis': nome,
            'cor': cor,
            'valor': valor35,
            'produto_xpath': produto_xpath,
            'qtd_numeros': qtd_numeros,
            'indisponiveis': indisponiveis
        }

        dados_produtos.append(dados_produto)
    return dados_produtos


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

email = 'fernandojukcunha@gmail.com'
senha = input('Digite sua Senha')
url = "https://app.yampi.com.br/"
xpath1 = '//*[@id="app"]/div[2]/div/div/div/form/div[1]/input'
xpath2 = '//*[@id="app"]/div[2]/div/div/div/form/div[2]/input'
xpath3 = '//*[@id="app"]/div[2]/div/div/div/form/div[3]/button'

link_preco = '//*[@id="single-product"]/div/div/div[3]/div[1]/div[1]/h2'
dados_produtos = []

# PROXIMO ->

# navegador.get('https://www.atacadobarato.com/produtos/tenis-iate-reserva/')
#
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[5]/span',  # bordo
#         'produto_xpath': '//*[@id="item-19637504"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',  # bege
#         'produto_xpath': '//*[@id="item-19637535"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[4]/span',  # preto/branco
#         'produto_xpath': '//*[@id="item-19637539"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',  # azul
#         'produto_xpath': '//*[@id="item-19637543"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[6]/span',  # preto/preto
#         'produto_xpath': '//*[@id="item-19637547"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[3]/span',  # cinza
#         'produto_xpath': '//*[@id="item-19637560"]/td[4]/a'
#     }
# ]
#
#
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos,link_preco,dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/tenis-olympikus-style/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',
#         'produto_xpath': '//*[@id="item-19685014"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/tenis-puma-ferrari-new/')
#
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[6]/span', #preto em cima e branco lado
#         'produto_xpath': '//*[@id="item-19685863"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',#Marinho
#         'produto_xpath': '//*[@id="item-19686711"]/td[4]/a'
#     },
# {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[5]/span',# Branco em cima Vermelho lado
#         'produto_xpath': '//*[@id="item-19686921"]/td[4]/a'
#     },
# {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[4]/span',#Preto lado branco em cima
#         'produto_xpath': '//*[@id="item-19687211"]/td[4]/a'
#     },
# {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',#Azul lado branco em cima
#         'produto_xpath': '//*[@id="item-19687230"]/td[4]/a'
#     },
# {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[7]/span',#Vermelho em cima branco lado
#         'produto_xpath': '//*[@id="item-19687240"]/td[4]/a'
#     }
# ]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)

# # PROXIMO ->
#
navegador.get('https://www.atacadobarato.com/produtos/tenis-mizuno-wave-prophecy-x-lancamento/')

produtos = [
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',#Preto com azul
        'produto_xpath': '//*[@id="item-19759955"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[3]/span',  # Marinho e Verde
        'produto_xpath': '//*[@id="item-19760000"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[7]/span',  # Preto com vermelho
        'produto_xpath': '//*[@id="item-19760257"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[4]/span',  # Preto e ouro
        'produto_xpath': '//*[@id="item-19760575"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[6]/span',  # Branco com Laranja
        'produto_xpath': '//*[@id="item-19760693"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',  # Preto com Prata
        'produto_xpath': '//*[@id="item-19760896"]/td[4]/a'
    },
    {
        'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[8]/span',  # Preto com verde
        'produto_xpath': '//*[@id="item-19760945"]/td[4]/a'
    }

]

#***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/tenis-feminino-casual-plataforma/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',
#         'produto_xpath': '//*[@id="item-19762088"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/sandalia-plataforma-nuvem-ortopedico/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[3]/span', #ROSA
#         'produto_xpath': '//*[@id="item-19762298"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',#BRANCO
#         'produto_xpath': '//*[@id="item-19762622"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[4]/span',#PRETO
#         'produto_xpath': '//*[@id="item-19762646"]/td[4]/a'
#     }
# ]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/sandalia-rasteira-multi-tiras-corda/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',
#         'produto_xpath': '//*[@id="item-19762955"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/sapatilha-hibrida-aquatica-feminina/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',
#         'produto_xpath': '//*[@id="item-19806058"]/td[4]/a'
#     }]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/chinelo-oakley-killer-poit/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span', #AZUL
#         'produto_xpath': '//*[@id="item-19806157"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[7]/span',#VERMELHO
#         'produto_xpath': '//*[@id="item-19806388"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',#LARANJA
#         'produto_xpath': '//*[@id="item-19806409"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[8]/span',#VERDE
#         'produto_xpath': '//*[@id="item-19806797"]/td[4]/a'
#     }
# ]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)
#
# # PROXIMO ->
#
# navegador.get('https://www.atacadobarato.com/produtos/chinelo-oakley-rest-2-0/')
# produtos = [
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[6]/span', #LARANJA
#         'produto_xpath': '//*[@id="item-19806831"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[5]/span',#AZUL
#         'produto_xpath': '//*[@id="item-19806913"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[1]/span',#VERMELHO
#         'produto_xpath': '//*[@id="item-19806918"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[2]/span',#PRETO BRANCO
#         'produto_xpath': '//*[@id="item-19806926"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[3]/span',#VERDE
#         'produto_xpath': '//*[@id="item-19806931"]/td[4]/a'
#     },
#     {
#         'cor': '//*[@id="single-product"]/div/div/div[3]/form/div[1]/div[1]/div/a[4]/span',#AMARELO
#         'produto_xpath': '//*[@id="item-19806944"]/td[4]/a'
#     }
# ]
#
# #***PRENCHE INFOMAÇÃO DOS PRODUTOS ACIMA***
# funcao_principal(produtos, link_preco, dados_produtos)

#\\\\\\\\\\\\\\\\\\\\\////////////////////////
            # fecha loja Tenis
navegador.quit()




#***************************************************************
#Abre a yampi e faz Loguin                                      #
navegador_yampi = fazer_login_yampi(email, senha)               #
time.sleep(3)                                                   #
                                                                #
#Atualiza os daods                                              #
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



