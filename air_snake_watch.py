from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import asyncio

import scrap_site

# Configurações do navegador com agente personalizado para o navegador
options = Options()
ua = UserAgent()
user_agent = ua.chrome
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--window-size=1550,1000')
options.add_argument("--incognito")
options.add_argument("--headless=new")

# Inicialização do serviço e do navegador
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)


async def main():
    print("Iniciando a configuração do proxy")

    await scrap_site.scrap_123milhas_by_url(browser)

asyncio.run(main())
