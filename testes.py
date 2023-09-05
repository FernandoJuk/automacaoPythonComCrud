from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pyautogui

time.sleep(5)
print(pyautogui.position())


# # Configuração do driver do Chrome
# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)
#
# # Navegar até a página desejada
# navegador.get('https://www.maisapato.com.br/sandalia-salto-fino-rosauva-lemon-carnelian-fivela')
#
# # Aguardar um pouco para garantir que a página carregue completamente
# time.sleep(2)
#
# # Encontra o elemento select usando XPath
# select_element = navegador.find_element(By.XPATH, '//*[@id="attribute145"]')
#
# # Encontra todos os elementos option dentro do select
# opcoes = select_element.find_elements(By.TAG_NAME, 'option')
#
# # Criar listas para armazenar os tamanhos, saldos, números disponíveis e números indisponíveis
# tamanhos_saldos = []
# numeros_disponiveis = []
# indisponiveis = []
#
# # Extrair os tamanhos, saldos e separar em disponíveis e indisponíveis
# for opcao in opcoes:
#     valor = opcao.get_attribute('value')
#     if valor:
#         tamanho_estoque = opcao.text.split(' - Estoque: ')
#         if len(tamanho_estoque) == 2:
#             tamanho = tamanho_estoque[0].split(': ')[1]
#             estoque = int(tamanho_estoque[1])
#             tamanhos_saldos.append((tamanho, estoque))
#             if estoque > 0:
#                 numeros_disponiveis.append(tamanho)
#             else:
#                 indisponiveis.append(tamanho)
#
# # Update stock for available sizes
# for tamanho in numeros_disponiveis:
#     checkbox_locator = f'//span[contains(text(), "{tamanho}")]/../..//input[@type="checkbox"]'
#     checkbox = navegador.find_element(By.XPATH, checkbox_locator)
#     if not checkbox.is_selected():
#         checkbox.click()
#
# # Update stock for unavailable sizes
# for tamanho in indisponiveis:
#     checkbox_locator = f'//span[contains(text(), "{tamanho}")]/../..//input[@type="checkbox"]'
#     checkbox = navegador.find_element(By.XPATH, checkbox_locator)
#     if checkbox.is_selected():
#         checkbox.click()
#
# # Aguardar um pouco to ensure the page updates
# time.sleep(2)
#
# # Close the browser
# navegador.quit()
