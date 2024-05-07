from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

ideal_price = os.getenv("IDEAL_PRICE")


async def scrap_site_by_google(selected_web_browser):
    # Visitar o site
    selected_web_browser.get("https://www.google.com")

    # Procurar o campo de pesquisa e inserir o termo "skyscanner"
    # O WebDriverWait é uma forma de esperar que certa coisa aconteça no timeout de 10 segundos
    search_box = WebDriverWait(selected_web_browser, 10).until(ec.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys("skyscanner")
    search_box.send_keys(Keys.ENTER)

    # Aguardar e clicar no primeiro resultado da pesquisa
    first_result = WebDriverWait(selected_web_browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'h3')))
    first_result.click()

    # Clica para selecionar o 1º campo de pesquisa do sky
    source_location_search = WebDriverWait(selected_web_browser, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="originInput-input"]')))

    source_location_search.send_keys('Recife')
    source_location_search.send_keys(Keys.ENTER)

    # Clica para selecionar o 2º campo de pesquisa do sky

    destination_location_search = WebDriverWait(selected_web_browser, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="destinationInput-input"]')))
    destination_location_search.send_keys('Floria')
    source_location_search.send_keys(Keys.ENTER)

    # Clicar na seleção da data de ida
    going_date_input = WebDriverWait(selected_web_browser, 10).until(ec.element_to_be_clickable(By.XPATH, '//*[@id="app-root"]/div[1]/div/div/main/div[1]/div/div[3]/div/div[3]/div[1]/div/button/span[2]'))
    # //*[@id="app-root"]/div[1]/div/div/main/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/button[1] XPath datas especificas
    # //*[@id="app-root"]/div[1]/div/div/main/div[1]/div/div[3]/div/div[3]/div[3]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[5]/div[2]/div/button XPath dia 30 de setembro

    # Clicar no botão de pesquisar
    # search_button = WebDriverWait(selected_web_browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="originInput-input"]')))
    # search_button.click()

    # Esperar o tempo necessário
    time.sleep(30)

    # Fechar o navegador
    selected_web_browser.quit()


async def scrap_123milhas_by_url(selected_browser):
    print(ideal_price, type(ideal_price))
    selected_browser.get('https://123milhas.com/v2/busca?de=REC&para=FLN&adultos=2&criancas=0&bebes=0&ida=31-08-2024&volta=04-10-2024&classe=3&is_loyalty=0&search_id=1840551711')

    print("Iniciando a verificação pelos elementos na página")

    first_result = WebDriverWait(selected_browser, 120).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'card-header__value')))

    for price in first_result[:3]:
        only_price = price.text.split()[1]
        is_ideal_price = only_price <= ideal_price

        if is_ideal_price:
            print(f"Chegou no preço que queremooooos {price}")
            # Aqui vamos mandar para o CSV, vamos mandar para whatsapp, etc...

    time.sleep(10)

    selected_browser.quit()






